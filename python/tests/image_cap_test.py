import os
import pyscreenshot as ImageGrab
import unittest
from datetime import datetime


class TestScreenshots(unittest.TestCase):

    # Test methods

    def test_take_x_screenshots(self):
        im_folder_path = 'image_cap_images'
        # Helpers

        def folder_item_count():
            files = os.listdir(im_folder_path)
            return len(files)

        def do_cleanup():
            im_list = os.listdir(im_folder_path)

            for im_file in im_list:
                im_file_path = os.path.join(im_folder_path, im_file)
                try:
                    if os.path.isfile(im_file_path):
                        os.unlink(im_file_path)
                except Exception as e:
                    print(e)

        # Will need to create an object that will handle starting and stopping of this interval process

        def do_capture_loop(trigger):
            while not folder_item_count() == 5:
                trigger()

            do_cleanup()
            self.assertTrue(True)

        def take_screenshot():
            # grab screenshot
            im = ImageGrab.grab()
            datetime_str = str(datetime.now())

            # Save screenshot and add dir
            im.save(f'{im_folder_path}/{datetime_str}.png')
            print('Added screenshot to folder')

        do_capture_loop(take_screenshot)
