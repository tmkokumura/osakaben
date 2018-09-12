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
input_text = "なぜですか"
logger.info('input text: ' + input_text)

""" translate """
output_text = translator.translate(input_text)
logger.info('output text: ' + output_text)

""" save text """
sql = 'insert into TT_TEXT (INPUT_TEXT, INPUT_DT, OUTPUT_TEXT, OUTPUT_DT) values (?,?,?,?)'

