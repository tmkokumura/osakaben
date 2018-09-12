# coding: utf-8

from abc import ABCMeta, abstractmethod


class BaseTranslator(metaclass=ABCMeta):

    @abstractmethod
    def translate(self, in_msg):
        pass
