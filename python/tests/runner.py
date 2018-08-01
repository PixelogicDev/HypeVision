import unittest
# Tests
import image_cap_test
import image_crop_test
import image_ocr_test

loader = unittest.TestLoader()
suite = unittest.TestSuite()
runner = unittest.TextTestRunner(verbosity=2)

suite.addTests(loader.loadTestsFromModule(image_cap_test))
suite.addTests(loader.loadTestsFromModule(image_crop_test))
suite.addTests(loader.loadTestsFromModule(image_ocr_test))

print(runner.run(suite))
