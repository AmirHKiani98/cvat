from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from PIL import Image
import io
import json
import base64
from . import utils

@csrf_exempt # We'll use proper CSRF protection in production #TODO don't forget about this
@require_http_methods(["POST", "OPTIONS"])
def get_image_txt_list(request):
    if request.method == 'OPTIONS':
        # Handle CORS preflight
        response = JsonResponse({'detail': 'CORS preflight success'})
        response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
        response['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        return response

    try:
        data = json.loads(request.body)
        base64_image = data.get("image")

        if not base64_image:
            return JsonResponse({"error": "No image provided"}, status=400)

        if "," in base64_image:
            base64_image = base64_image.split(",")[1]

        image_bytes = base64.b64decode(base64_image)
        image = Image.open(io.BytesIO(image_bytes))
        txts = utils.ocr_image_text(image)


        return JsonResponse({"message": "Image processed successfully", "texts": txts}, status=200)

    except Exception as e:
        print("Error processing image:", e)
        return JsonResponse({"error": str(e)}, status=500)
