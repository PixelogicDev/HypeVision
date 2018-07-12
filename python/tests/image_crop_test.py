import unittest


class TestScreenshots(unittest.TestCase):

    # Test methods
    def test_crop_720(self):
        print('Testing 720p crop')

    def test_crop_1080(self):
        print('Testing 1080p crop')

    def test_crop_1440(self):
        print('Testing 1440p crop')

    def test_crop_2160(self):
        print('Testing 2160p crop')


# MAD PROPS DontCallMeLateForDinner
if __name__ == '__main__':
    unittest.main()
else:
    print('Not main, not running tests.')
