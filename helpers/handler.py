# This file will contain APIs that client can call to interact with Python script
class Controller:
    def __init__(self, is_dev):
        self._is_capturing = False
        self._is_dev = is_dev

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

    # Properties
    is_capturing = property(get_is_capturing, start_capturing, stop_capturing)
    is_dev = property(get_is_dev, set_is_dev)
