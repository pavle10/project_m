class Response:

    def __init__(self, status, message, data=None):
        self._status = status
        self._message = message
        self._data = data

    def get_status(self):
        return self._status

    def set_status(self, value):
        self._status = value

    def get_message(self):
        return self._message

    def set_message(self, value):
        self._message = value

    def get_data(self):
        return self._data

    def set_data(self, value):
        self._data = value

