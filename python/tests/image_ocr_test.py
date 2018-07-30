import tesserocr
import unittest
import cv2
import os


class TestImageOCR(unittest.TestCase):
    def test_img_ocr(self):
        # start directory loop
        im_folder_path = 'crop_test_images/crop_test_output'
        im_list = os.listdir(im_folder_path)

        for im_file in im_list:
            im_file_path = os.path.join(im_folder_path, im_file)
            print(f'OCR-ing {im_file}...')

            # check for file
            if os.path.isfile(im_file_path):
                # Convert to grayscale
                img = cv2.imread(im_file_path)
                img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

                # Binarize
                thresh = cv2.threshold(
                    img_gray_denoise, 128, 255, cv2.THRESH_OTSU)[0]

                im_bw = cv2.threshold(
                    img_gray, thresh, 255, cv2.THRESH_BINARY)[1]
                cv2.imwrite(im_file_path, im_bw)

                # OCR image
                print(tesserocr.file_to_text(im_file_path))


if __name__ == '__main__':
    unittest.main()
else:
    print('Not main, not running tests.')
