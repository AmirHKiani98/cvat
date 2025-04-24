from django.shortcuts import render
import base64
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import io
# Create your views here.



@csrf_exempt  # We'll use proper CSRF protection in production #TODO don't forget about this
def process_image(request):
    if request.method == "POST":
        try:
            import json
            data = json.loads(request.body)
            base64_image = data.get("image")

            if not base64_image:
                return JsonResponse({"error": "No image provided"}, status=400)

            # Remove base64 prefix if present
            if "," in base64_image:
                base64_image = base64_image.split(",")[1]

            image_bytes = base64.b64decode(base64_image)
            image = Image.open(io.BytesIO(image_bytes))

            # Example: save the image or process it
            image.save("cropped_upload.png")  # or do OCR, etc.

            return JsonResponse({"message": "Image processed successfully"})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid method"}, status=405)
