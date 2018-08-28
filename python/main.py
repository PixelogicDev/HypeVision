import json
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
        value, conf = img_ocr.predict_value(processed_img)

        # {
        #   predict: float,
        #   conf: int,
        #   error: {
        #       type: Enum
        #       message: string
        #   }
        # }
        data = {}
        error = {}

        if type(value) != OCRError:
            data['predict'] = value
            data['conf'] = conf
            data['error'] = None

            json_data = json.dumps(data)
            print(json_data)
        elif value == OCRError.NO_CONF:
            data['predict'] = None
            data['conf'] = conf
            error['type'] = 'NO_CONF'
            error['message'] = 'No conf level was found.'
            data['error'] = error

            json_data = json.dumps(data)
            print(json_data)
        elif value == OCRError.LOW_CONF:
            data['predict'] = None
            data['conf'] = conf
            error['type'] = 'LOW_CONF'
            error['message'] = 'Conf level was too low.'
            data['error'] = error

            json_data = json.dumps(data)
            print(json_data)
        elif value == OCRError.EMPTY_VAL:
            data['predict'] = None
            data['conf'] = conf
            error['type'] = 'EMPTY_VAL'
            error['message'] = 'No value was found.'
            data['error'] = error

            json_data = json.dumps(data)
            print(json_data)
        elif value == OCRError.BAD_PRED:
            data['predict'] = None
            data['conf'] = conf
            error['type'] = 'BAD_PRED'
            error['message'] = 'A bad prediction was found.'
            data['error'] = error

            json_data = json.dumps(data)
            print(json_data)


if __name__ == '__main__':
    main()
