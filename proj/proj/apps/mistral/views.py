from django.shortcuts import render
from django.http import JsonResponse
from mistralai import Mistral
import os

def home(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        response = get_mistral_response(prompt)
        return JsonResponse({"response": response})
    return render(request, "index.html")

def get_mistral_response(prompt):
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        return "API-ключ Mistral не установлен."

    client = Mistral(api_key=api_key)
    try:
        response = client.chat.complete(
            model="mistral-large-latest",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Ошибка при обращении к Mistral API: {str(e)}"
