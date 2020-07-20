import logging
import os
import datetime


class LogStream(object):
    
    def __init__(self):
        self.logs = ''

    def write(self, log):
        self.logs += log

    def flush(self):
        pass

    def __str__(self):
        return self.logs


class SingletonType(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingletonType, cls).__call__(*args, **kwargs)

        return cls._instance[cls]


class Logger(metaclass=SingletonType):
    __logger = None

    def __init__(self):
        self.__log_stream = LogStream()
        _format = '%(asctime)s  [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s'
        logging.basicConfig(stream=self.__log_stream, level=logging.DEBUG, format=_format)

        self.__logger = logging.getLogger("CREEDIT_BATCH")

        formatter = logging.Formatter(_format)

        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)

        self.__logger.addHandler(streamHandler)
    
    def get_logger(self):
        return self.__logger

    def get_log_stream(self):
        return self.__log_stream

    def upload_issue_to_github(self):
        pass

    def send_email(self):
        pass

    @classmethod
    def get_instance(cls):
        return cls.__call__()
