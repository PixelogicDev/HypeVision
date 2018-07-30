import os
import unittest
import cv2


class TestImageCrop(unittest.TestCase):
    def test_img_crop(self):
        # Helper
        def run_assert_test(crop_img):
            # test for proper size
            crop_h, crop_w, _ = crop_img.shape
            if im_file == 'PUBG-720.png':
                self.assertEqual(crop_h, 50)
                self.assertEqual(crop_w, 103)
            elif im_file == 'PUBG-1080.png':
                self.assertEqual(crop_h, 75)
                self.assertEqual(crop_w, 154)
            elif im_file == 'PUBG-2160.png':
                self.assertEqual(crop_h, 151)
                self.assertEqual(crop_w, 308)
            else:
                return 'nope'

        width_multiplier = 0.92
        height_multiplier = 0.07
        im_folder_path = 'crop_test_images'
        im_folder_out_path = 'crop_test_images/crop_test_output'

        # start directory loop
        im_list = os.listdir(im_folder_path)

        for im_file in im_list:
            im_file_path = os.path.join(im_folder_path, im_file)
            print(f'Cropping {im_file}...')

            # check for file
            if os.path.isfile(im_file_path):
                # read image
                img = cv2.imread(im_file_path)

                # get dimensions
                height, width, _ = img.shape
                x = int(width * width_multiplier)
                y = int(height * height_multiplier)

                # crop & save
                crop_img = img[0:y, x:]

                out_filename = f'{os.path.splitext(im_file)[0]}-cropped.png'
                cv2.imwrite(
                    f'{im_folder_out_path}/{out_filename}', crop_img)

                # run test
                run_assert_test(crop_img)


# MAD PROPS DontCallMeLateForDinner
if __name__ == '__main__':
    unittest.main()
else:
    print('Not main, not running tests.')
