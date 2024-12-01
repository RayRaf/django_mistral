import base64
import os
from mistralai import Mistral
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from io import BytesIO
from PIL import Image
from pdf2image import convert_from_bytes
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import UserStatistics

# Retrieve the API key from environment variables
api_key = os.environ.get("MISTRAL_API_KEY")

# Specify model
model = "pixtral-large-latest"

# Initialize the Mistral client
client = Mistral(api_key=api_key)

def encode_image(image_file):
    """Encode the image to base64."""
    try:
        return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        print(f"Error: {e}")
        return None

def convert_pdf_to_jpg(pdf_file):
    """Convert a PDF file to a JPEG image using pdf2image."""
    try:
        images = convert_from_bytes(pdf_file.read(), dpi=400)
        if images:
            buffered = BytesIO()
            images[0].save(buffered, format="JPEG")
            buffered.seek(0)
            return buffered
    except Exception as e:
        print(f"Error converting PDF to JPG: {e}")
        return None
    

@login_required
def main(request):
    return render(request, 'pixtral_index.html')

@csrf_exempt
def analyze_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        if image_file.content_type == 'application/pdf':
            # Convert PDF to JPEG
            image_file = convert_pdf_to_jpg(image_file)
            if image_file is None:
                return JsonResponse({"error": "Failed to convert PDF to image."})
        
        base64_image = encode_image(image_file)
        if base64_image is None:
            return JsonResponse({"error": "Failed to encode image."})

        # Check if 'prompt' is provided in the POST request
        prompt = request.POST.get('prompt', "Если этот документ является счетом на оплату то напиши реквизиты покупателя и продавца")

        # Define the messages for the chat
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": f"data:image/jpeg;base64,{base64_image}"
                    }
                ]
            }
        ]

        # Get the chat response
        try:
            chat_response = client.chat.complete(
                model=model,
                messages=messages
            )
            result = chat_response.choices[0].message.content

            # Increment the successful analyses count for the user
            if request.user.is_authenticated:
                user_statistics = UserStatistics.objects.get(user=request.user)
                user_statistics.successful_image_analyses += 1
                user_statistics.save()
        except Exception as e:
            return JsonResponse({"error": f"Error: {e}"}, status=500)

        return JsonResponse({"result": result})
    
    return JsonResponse({"error": "Invalid request."}, status=400)