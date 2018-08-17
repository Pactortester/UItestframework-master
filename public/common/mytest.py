#coding=utf-8
import time
import unittest
from public.common import pyselenium
from config import globalparam
from public.common.log import Log


class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    def setUp(self):
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        self.dr = pyselenium.PySelenium(globalparam.browser)
        self.dr.max_window()

    def tearDown(self):
        time.sleep(5)
        self.dr.quit()
        self.logger.info('###############################  End  ###############################')
