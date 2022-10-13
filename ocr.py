import cv2
import pytesseract
import psutil
import pyautogui
import time
import numpy as np
import helpers.handler as handler
import os

def create_dir(path):
    dir_exists = os.path.exists(path)

    if not dir_exists:
        os.mkdir(path)

def get_ratio(screen_height, controller):
    print('getting screen ratio')

    # Set controller screen height
    if controller.screen_height != screen_height:
        controller.screen_height = screen_height

    # Supported heights = 2160, 1440, 1200, 1080
    if screen_height == 2160:
        # x1, y1, x2, y2
        return (0.866, 0.138, 0.908, 0.227)
    elif screen_height == 1440:
        # x1, y1, x2, y2
        return (0.911, 0.09, 0.936, 0.15)
    elif screen_height == 1080 or screen_height == 1200:
        # x1, y1, x2, y2
        return (0.932, 0.069, 0.953, 0.113)
    else:
        print(f'Screen height of {screen_height} not configured yet')

def crop(image, controller, current_index):
    # No matter what screensize we have, we want to crop the top right corner of the screen at 720p
    # From here we can use the same ratio every time (hopefully)
    print('cropping')

    # Get current image size
    (height, width, _) = image.shape

    # Return proper ratio based on height of screen
    x1_ratio, y1_ratio, x2_ratio, y2_ratio = get_ratio(height, controller)

    # Crop image to 720p
    crop_x1 = width - 1280
    crop_y1 = 0
    crop_x2 = width
    crop_y2 = 720

    cropped_720p = image[crop_y1: crop_y2, crop_x1: crop_x2]
    create_dir(f'captures/{current_index}')
    cv2.imwrite(f'captures/{current_index}/720p.png', cropped_720p)

    # Take 720p image and crop based on ratio
    (cropped_height, cropped_width, _) = cropped_720p.shape
    x1_ratio_width = round(cropped_width * x1_ratio)
    x2_ratio_width = round(cropped_width * x2_ratio)
    y1_ratio_height = round(cropped_height * y1_ratio)
    y2_ratio_height = round(cropped_height * y2_ratio)

    player_count_crop = cropped_720p[y1_ratio_height: y2_ratio_height, x1_ratio_width: x2_ratio_width]

    # Return cropped image
    return player_count_crop


def clean(cropped_image, current_index):
    print('cleaning image')

    # Convert to grayscale
    gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

    # Threshold
    gray_no_noise_threshold = cv2.threshold(
        gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Saved cleaned image
    create_dir(f'captures/{current_index}')
    cv2.imwrite(
        f'captures/{current_index}/cleaned-{current_index}.png', gray_no_noise_threshold)

    return gray_no_noise_threshold


# TODO: Adding conf score checks
def predict(clean_image):
    print('Predicting player count')
    config = r'--oem 3 --psm 6 outputbase digits'
    return pytesseract.image_to_string(clean_image, config=config)


def capture_screen(current_index):
    # program = 'QuickTime Player'
    program = "r5apex.exe"

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
    create_dir(f'captures/{current_index}')
    cv2.imwrite(f'captures/{current_index}/screenshot-{current_index}.png', screenshot)

    return (screenshot, current_index + 1)


current_index = 1
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# Start capturing
controller = handler.Controller()
controller.start_capturing()

while (controller.is_capturing):
    # Take screenshot
    screenshot, next_index = capture_screen(current_index)

    if len(screenshot) == 0:
        print('Application not open, checking in 5 seconds')
        time.sleep(5)
        continue

    # Load & crop image
    cropped_image = crop(screenshot, controller, current_index)
    print('cropping complete')

    # Clean image
    clean_image = clean(cropped_image, current_index)
    print('image cleaned')

    # Run through OCR
    value = predict(clean_image)

    # Send off to client
    print(f'#{current_index}: {value}')

    current_index = next_index

    # Cool down for 5 seconds
    time.sleep(5)
