# coding: utf-8

from logging import getLogger, StreamHandler, Formatter, FileHandler, DEBUG, INFO
from translator.rule_translator import RuleTranslator

""" constants """
LOG_DIR = 'log/'
LOG_FILE = 'data_prep_custom2.py.log'

""" Log Settings """
logger = getLogger('main')
log_fmt = Formatter('%(asctime)s %(name)s %(lineno)d [%(levelname)s][%(funcName)s] %(message)s')
log_handler = StreamHandler()
log_handler.setLevel(INFO)
log_handler.setFormatter(log_fmt)
logger.addHandler(log_handler)
log_handler = FileHandler(LOG_DIR + LOG_FILE, 'a')
log_handler.setFormatter(log_fmt)
logger.setLevel(DEBUG)
logger.addHandler(log_handler)

""" init RuleTranslator """
logger.info('init RuleTranslator')
translator = RuleTranslator()

""" read text """
txt = "なぜですか"
logger.info('input text: ' + txt)

""" translate """
txt = translator.translate(txt)
logger.info('output text: ' + txt)

