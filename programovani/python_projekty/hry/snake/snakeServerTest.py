from bottle import Bottle, run, request
import snakeEditTest4 as snake

app = Bottle()

DX_DY_DICT = {
    dx: snake.dx,
    dy: snake.dy,
    dx2: snake.dx2,
    dy2: snake.dy2
}

@app.post('/dx_dy_dict/add')
def add_dx_dy():
    return {
        DX_DY_DICT[dx],
        DX_DY_DICT[dy],
        DX_DY_DICT[dx2],
        DX_DY_DICT[dy2]
    }

@app.get('/get')
def get_messages():
    return {
        DX_DY_DICT[dx],
        DX_DY_DICT[dy],
        DX_DY_DICT[dx2],
        DX_DY_DICT[dy2]
    }    

@app.get('/status') # HTTP GET na http://localhost:8181/status
def status():
    return "OK"

run(app, host='localhost', port=8181, debug=True)
