import sys
from src.logger import logging

def error_message_detail(error, error_details:sys):
    _,_,exec_tb=error_details.exc_info()
    file_name= exec_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name[{0}] line number [{1}] error message ".format(file_name, exec_tb.tb_lineno,str(error)
                                                                                                     )
    return error_message
    
#Exception is the base class for most built-in exceptions in Python (like ValueError, TypeError, etc.).    
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details=error_detail)

    def __str__(self):
        '''__str__ is a special (dunder) method in Python that defines how an object is represented as a string when you use print() or str().'''
        return self.error_message