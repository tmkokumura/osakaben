# coding: utf-8

from abc import ABCMeta, abstractmethod


class DatabaseHandler(metaclass=ABCMeta):

    @abstractmethod
    def execute(self, sql):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass
