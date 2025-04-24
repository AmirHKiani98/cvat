import os
import platform
import paddle
from paddleocr import PaddleOCR
from PIL import Image

# Determine whether GPU should be used
system = platform.system()
use_gpu = False if system == "Darwin" else paddle.is_compiled_with_cuda()

ocr = PaddleOCR(lang='en', use_gpu=use_gpu, show_log=False)

def ocr_image_text(img_path):
    img_path = str(img_path)
    result = ocr.ocr(img_path, cls=False)

    result = result[0]
    txts = [line[1][0] for line in result]
    return txts
