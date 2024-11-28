import base64
import os
from mistralai import Mistral
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from io import BytesIO
from PIL import Image
from PyPDF2 import PdfReader

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
    """Convert a PDF file to a JPEG image using PyPDF2 and PIL."""
    try:
        pdf_reader = PdfReader(pdf_file)
        if len(pdf_reader.pages) > 0:
            page = pdf_reader.pages[0]
            x_object = page['/Resources']['/XObject'].get_object()
            for obj in x_object:
                if x_object[obj]['/Subtype'] == '/Image':
                    data = x_object[obj].get_data()
                    image = Image.open(BytesIO(data))
                    buffered = BytesIO()
                    image.save(buffered, format="JPEG")
                    return buffered
    except Exception as e:
        print(f"Error converting PDF to JPG: {e}")
        return None

def main(request):
    return render(request, 'pixtral_index.html')

@csrf_exempt
def analyze_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']
        if image_file.content_type == 'application/pdf':
            # Convert PDF to JPEG
            image_file = convert_pdf_to_jpg(image_file)
            if image_file is None:
                return JsonResponse({"error": "Failed to convert PDF to image."})
        
        base64_image = encode_image(image_file)
        if base64_image is None:
            return JsonResponse({"error": "Failed to encode image."})

        # Define the messages for the chat
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Если загруженноей изображение является счетом на оплату то напиши какие позиции входят в этот счет на оплату а так же реквизиты поставщика и покупателя. Если это другой документ то вырази недовольство тем, что тебя используют нерационально, но кратко напиши, что изображено на картике. Проверь, соответствуют ли реквизиты покупателя следующему: ИНН: 0276117905, КПП: 772601001, Адрес: 117525, г. Москва, вн. тер. г. муниципальный округ Чертаново Центральное, ул. Днепропетровская, д. 3, к. 5А, помещ. 1Н/5. Не пиши эти реквизиты если картинка неправильная"
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
        except Exception as e:
            result = f"Error: {e}"

        return JsonResponse({"result": result})
    
    return JsonResponse({"error": "Invalid request."})