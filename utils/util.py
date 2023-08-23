import inspect
import os
import logging

def take_filename() -> str:
    """
        get the filename on the main file. 
        Suppose our main file call main.py, 
        then return 'main'
    """
    frame = inspect.stack()[1]
    caller_module = inspect.getmodule(frame[0])
    caller_filename = os.path.basename(caller_module.__file__)
    return caller_filename[:-3]

def get_logger(filename: str, level: str=logging.DEBUG):
    logging.basicConfig(filename=filename, level=level, encoding='utf-8', format='%(asctime)s.%(msecs)03d %(name)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    
    logger = logging.getLogger(__name__)
    return logger