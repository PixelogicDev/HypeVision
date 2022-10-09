import cv2
import pytesseract
import psutil
import pyautogui
import time
import numpy as np
import helpers.handler as handler


def crop(image, controller):
    x1_ratio = 0.915
    x2_ratio = 0.933
    y1_ratio = 0.046
    y2_ratio = 0.075

    # Just using this to test on macos rn
    macos_toolbar_height = 78

    print('cropping')

    # Get current image size
    (height, width, _) = image.shape

    # Create ratio'ed heights
    x1_ratio_width = round(width * x1_ratio)
    x2_ratio_width = round(width * x2_ratio)
    y1_ratio_height = round(height * y1_ratio)
    y2_ratio_height = round(height * y2_ratio)

    if controller.is_dev:
        print('In dev mode, using macbook bar height')
        y1_ratio_height = y1_ratio_height + macos_toolbar_height
        y2_ratio_height = y2_ratio_height + macos_toolbar_height

    # Crop image
    cropped_image = image[y1_ratio_height: y2_ratio_height,
                          x1_ratio_width: x2_ratio_width]

    # Return cropped image
    return cropped_image


def clean(cropped_image, current_index):
    print('cleaning image')

    # Convert to grayscale
    gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

    # Remove noise
    # gray_no_noise = cv2.medianBlur(gray, 5)

    # Threshold
    gray_no_noise_threshold = cv2.threshold(
        gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Saved cleaned image
    cv2.imwrite(
        f'captures/cleaned-{current_index}.png', gray_no_noise_threshold)

    return gray_no_noise_threshold


# TODO: Adding conf score checks
def predict(clean_image):
    print('Predicting player count')
    config = r'--oem 3 --psm 6 outputbase digits'
    return pytesseract.image_to_string(clean_image, config=config)


def capture_screen(current_index):
    program = 'QuickTime Player'

    found = program in (i.name() for i in psutil.process_iter())

    if found == False:
        print(f'{program} is not running')
        return ([], current_index)

    # Capture screen and modify
    print(f'{program} is running -- capturing screenshot')
    time.sleep(5)

    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Write to disk for reference (testing only)
    cv2.imwrite(f'captures/screenshot-{current_index}.png', screenshot)

    return (screenshot, current_index + 1)


current_index = 1

# Start capturing
controller = handler.Controller(is_dev=True)
controller.start_capturing()

while (controller.is_capturing):
    # Take screenshot
    (screenshot, next_index) = capture_screen(current_index)

    if len(screenshot) == 0:
        print('Application not open, checking in 5 seconds')
        time.sleep(5)
        continue

    # Load & crop image
    # test_image1 = cv2.imread('test.png')
    cropped_image = crop(screenshot, controller)
    print('cropping complete')

    # Clean image
    clean_image = clean(cropped_image, current_index)
    print('image cleaned')

    # Run through OCR
    value = predict(clean_image)

    # Send off to client
    print(f'#{current_index}: {value}')

    if current_index == 10:
        controller.stop_capturing()
    else:
        current_index = next_index
        # Cool down for 5 seconds
        time.sleep(5)
