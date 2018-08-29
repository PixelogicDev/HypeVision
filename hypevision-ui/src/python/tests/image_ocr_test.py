import pytesseract
from PIL import Image
import unittest
import cv2
import os


class TestImageOCR(unittest.TestCase):
    def test_img_ocr(self):
        im_folder_path = 'crop_test_images/crop_test_output'

        def assertValue(im_file, ocr_val):
            val = int(ocr_val)
            if im_file == 'PUBG-720-cropped.png':
                self.assertEqual(val, 50)
            elif im_file == 'PUBG-1080-cropped.png':
                self.assertEqual(val, 33)
            elif im_file == 'PUBG-2160-cropped.png':
                self.assertEqual(val, 46)
            elif im_file == 'PUBG-4K-cropped.png':
                self.assertEqual(val,  77)
            else:
                return 'nope'

        def do_cleanup():
            im_list = os.listdir(im_folder_path)

            for im_file in im_list:
                im_file_path = os.path.join(im_folder_path, im_file)
                try:
                    if os.path.isfile(im_file_path):
                        os.unlink(im_file_path)
                except Exception as e:
                    print(e)

        # start directory loop
        im_list = os.listdir(im_folder_path)

        for im_file in im_list:
            im_file_path = os.path.join(im_folder_path, im_file)
            print(f'OCR-ing {im_file}...')

            # check for file
            if os.path.isfile(im_file_path):
                # Read and resize image
                img = cv2.imread(im_file_path)

                img_resized = cv2.resize(img, None, fx=2, fy=2,
                                         interpolation=cv2.INTER_CUBIC)

                # Blur for smoothing
                blur = cv2.blur(img_resized, (5, 5))

                # Convert to gray scale
                img_gray = cv2.cvtColor(blur, cv2.COLOR_RGB2GRAY)

                # Threshold
                img_bw = cv2.threshold(
                    img_gray, 128, 255, cv2.THRESH_BINARY_INV)[1]

                # Save final image to path for visual check
                cv2.imwrite(im_file_path, img_bw)

                # Convert to Image type from PIL
                img_from_arr = Image.fromarray(img_bw)

                # OCR image
                # MAD PROPS http://ocr7.com/

                # Get data
                data = pytesseract.image_to_data(img_from_arr,
                                                 lang='pubg', config='outputbase digits', output_type=pytesseract.Output.DICT)
                # Get Text & Conf
                text = data['text'][4]

                # Assert Test
                assertValue(im_file, text)

            do_cleanup()
