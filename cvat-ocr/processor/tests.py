from django.test import TestCase
from django.conf import settings
from . import utils
# Create your tests here.

class ExampleTestCase(TestCase):
    
    def test_example(self):
        # Example test case
        self.assertEqual(1 + 1, 2)
    
    def test_another_example(self):
        # Another example test case
        self.assertTrue(True)

    def test_utils_image_ocr(self):
        img_path = settings.BASE_DIR / 'processor/test_assets/receipt_example.jpeg'
        txts = utils.ocr_image_text(img_path)
        assert isinstance(txts, list)