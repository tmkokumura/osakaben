# -- coding: utf-8 --

import csv
from .base_translator import BaseTranslator
from logging import getLogger


class RuleTranslator(BaseTranslator):

    """ constants """
    _DEFAULT_FILE_NAME = 'resources/rule/rule.csv'
    _IDX_BEFORE = 0
    _IDX_AFTER = 1
    _FILE_MODE_READONLY = 'r'

    """ private methods """
    @classmethod
    def _read_rules(cls, file_name):
        with open(file_name, cls._FILE_MODE_READONLY) as f:
            reader = csv.reader(f)
            rules = [[row[cls._IDX_BEFORE], row[cls._IDX_AFTER]] for row in reader]
        return rules

    """ constructors """
    def __init__(self, file_name=_DEFAULT_FILE_NAME):
        self._logger = getLogger('main')

        self._logger.info('reading: ' + file_name)
        self._rules = RuleTranslator._read_rules(file_name)

    """ public methods """
    def translate(self, in_txt):
        self._logger.info('input text: ' + in_txt)
        out_txt = in_txt
        # ログを詳細に出力するためreplaceで実装しているが、
        # 性能面が課題となるならstr.translateで実装すべき。
        for rule in self._rules:
            self._logger.debug('rule: {}'.format(rule))
            out_txt = out_txt.replace(rule[RuleTranslator._IDX_BEFORE], rule[RuleTranslator._IDX_AFTER])
            self._logger.debug('current text: ' + out_txt)

        self._logger.info('output text: ' + out_txt)
        return out_txt

