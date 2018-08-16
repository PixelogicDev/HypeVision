from image_capture import ImageCapture
from image_processor import ImageProcessor
from image_ocr import ImageOCR


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
    count = 0
    for img in img_cap.yield_image_capture():
        print('Start img pre-processing...')

        # Pre-process image
        processed_img = img_processor.run_preprocesing(img)

        # OCR Image
        img_ocr.predict_value(processed_img)

        count += 1
        if count == 5:
            img_cap.stop_image_capture()


if __name__ == '__main__':
    main()
