from image_capture import ImageCapture
from image_processor import ImageProcessor
from image_ocr import ImageOCR
from enums import OCRError


def main():

    # App is opened
    # Detect for PUBG open
    # Start Img Cap
    # Yield out result to do pre-processing
    # Get result
    # Pass up to Electron

    img_cap = ImageCapture()
    img_processor = ImageProcessor()
    img_ocr = ImageOCR()
    for img in img_cap.yield_image_capture():
        # Pre-process image
        processed_img = img_processor.run_preprocesing(img)

        # OCR Image
        value = img_ocr.predict_value(processed_img)

        if type(value) != OCRError:
            print(f'In main: predicted value: {value}')
        elif value == OCRError.NO_CONF:
            print('In main: No conf level.')
        elif value == OCRError.LOW_CONF:
            print('In main: No conf was too low.')
        elif value == OCRError.EMPTY_VAL:
            print('In main: Value was empty.')
        elif value == OCRError.BAD_PRED:
            print('In main: Received bad prediction')


if __name__ == '__main__':
    main()
