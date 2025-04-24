import os
import platform
import paddle
from paddleocr import PaddleOCR
import tempfile
from PIL import Image

# Determine whether GPU should be used
system = platform.system()
use_gpu = False if system == "Darwin" else paddle.is_compiled_with_cuda()

ocr = PaddleOCR(lang='en', use_gpu=use_gpu, show_log=False)

def ocr_image_text(img):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
        img.save(tmp.name, format="PNG")
        tmp.close()
        
        result = ocr.ocr(tmp.name, cls=False)
        print("ocr result:", result)
        os.remove(tmp.name)

    result = result[0] if result else []
    if result is None:
        return []
    return [line[1][0] for line in result]
