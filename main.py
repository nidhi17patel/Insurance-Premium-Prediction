from Insurance.logger import logging
from Insurance.exception import InsuranceException
import sys, os


def test_logger_and_expection():
   try:
        logging.info("starting the test_logger_and_expection")
        result = 3/0
        print(result)
        logging.info("Ending point of test_logger_and_expection")
   except Exception as e:
        logging.debug(str(e))
        raise InsuranceException(e,sys)

if __name__=="__main__":
    try:
        test_logger_and_expection()
    except Exception as e:
        print(e)