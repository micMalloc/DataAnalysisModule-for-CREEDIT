import logging
import os
import datetime


class SingletonType(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingletonType, cls).__call__(*args, **kwargs)

        return cls._instance[cls]


class Logger(metaclass=SingletonType):
    __logger = None

    def __init__(self):
        self.__logger = logging.getLogger("CREEDIT_BATCH")
        self.__logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter('%(asctime)s  [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s')

        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)

        self.__logger.addHandler(streamHandler)
    
    def get_logger(self):
        return self.__logger

    def info(self, msg):
        self.__logger.info(msg)
    
    def debug(self, msg):
        self.__logger.debug(msg)

    @classmethod
    def get_instance(cls):
        return cls.__call__()
