from bottle import route, run

@route('/<top:int>/<bottom:int>')
def danger(top, bottom):
    try:
        result = {'result':top/bottom}
    except ZeroDivisionError:
        result = {'resuld':'Division by Zero'}

    return result

run(host = 'localhost', port='8080')