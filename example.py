#encoding: utf-8
from bottle import route, run
from my_math import careful_devision

from my_logging import get_logger

logger = get_logger(__name__)

def danger(top, bottom):
    return {
        'result': careful_devision(top, bottom),
        'error': None,
    }

if __name__ == '__main__':
    for x in range(1, 5, 2):
        for y in range(-4, 2, 4):
            print(f'x = {x}, y = {y}')
            if y == 0 or x ==0:
                logger.info('Кто-то пытается делить на ноль!')
            print(danger(x,y))