# This file will contain APIs that client can call to interact with Python script
class Controller:
    def __init__(self, is_dev=False):
        self._is_capturing = False
        self._is_dev = is_dev
        self._screen_height = 0

    # is_capturing
    def get_is_capturing(self):
        return self._is_capturing

    def start_capturing(self):
        self._is_capturing = True

    def stop_capturing(self):
        self._is_capturing = False

    # is_dev
    def get_is_dev(self):
        return self._is_dev

    def set_is_dev(self, is_dev):
        self._is_dev = is_dev

    # screen_height
    def get_screen_height(self):
        return self._screen_height
    
    def set_screen_height(self, height):
        self._screen_height = height

    # Properties
    is_capturing = property(get_is_capturing, start_capturing, stop_capturing)
    is_dev = property(get_is_dev, set_is_dev)
    screen_height = property(get_screen_height, set_screen_height)
