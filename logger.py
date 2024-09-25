"""
logger

Description:
"""
import time
import sys
import os

"""Logger init function.

Keyword arguments:
Return: prints initialization information and writes to log
"""
def logger_init():
    with open("logs.txt", "r") as f:
        lines = f.readlines()
        if len(lines) > 200:
            os.remove("logs.txt")
            f = open("logs.txt", "w")   

    # All time data
    named_tuple = time.localtime()
    
    # Full time string: year-month-day hour:minute:second
    time_string = time.strftime("%Y-%m-%d %H:%M:%S", named_tuple)
    # Current function ran in
    function_name = sys._getframe(1).f_code.co_name
    # Line number where function was called
    line_number = sys._getframe(1).f_lineno
    # Current file name
    filename = sys._getframe(1).f_code.co_filename
    
    # Full string: year-month-day hour:minute:second | INIT | filename:function_name:line_number - LOGGER INITIALIZED
    full_string = f"{time_string} | INIT | {filename}:{function_name}:{str(line_number)} - LOGGER INITIALIZED \n"
    
    # Writes full string to logs
    with open("logs.txt", "a") as f:
        f.write(full_string)
        
    # Prints full string in console
    print(full_string)
        
    

"""Log function

Keyword arguments:
message -- log message: string
log_file -- where to write log: string (file, console, both)
Return: prints the debug message in console or in log based on log_file variable
"""
def log(message):
    # All time data
    named_tuple = time.localtime()
    
    # Full time string: year-month-day hour:minute:second
    time_string = time.strftime("%Y-%m-%d %H:%M:%S", named_tuple)
    
    # Current function ran in
    function_name = sys._getframe(1).f_code.co_name
    
    # Line number where function was called
    line_number = sys._getframe(1).f_lineno
    
    # Current file name
    filename = sys._getframe(1).f_code.co_filename
    
    # Full string: year-month-day hour:minute:second | DEBUG | filename:function_name:line_number - LOGGER INITIALIZED
    full_string = f"{time_string} | DEBUG | {filename}:{function_name}:{str(line_number)} - {message} \n"
    
    with open("logs.txt", "a") as f:
        f.write(full_string+"\n")
            
        print(full_string)
    
    

    