#encoding: utf-8
from bottle import route, run
from my_math import careful_devision

import logging

logger = logging.getLogger('divider')
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s -- %(name)s::%(levelname)s %(message)s'
)
#handler = logging.StreamHandler()              #логирование идет в поток в консоль

handler = logging.FileHandler('my_app.log')     #теперь логирование идет в файл
handler.setLevel(logging.INFO) 
handler.setFormatter(formatter)
logger.addHandler(handler)

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