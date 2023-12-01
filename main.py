import socketio
from socketio.exceptions import ConnectionError
from rover import Rover

sio = socketio.Client()
rover = Rover()

SERVER_URL = 'http://localhost:8000/'


try:
    sio.connect(SERVER_URL, transports=['websocket'])
    print(f'Conexão estabelecida: {SERVER_URL}')

    @sio.event
    def move_forward(data):
        rover.move_forward()

    @sio.event
    def move_backward(data):
        rover.move_backward()

    @sio.event
    def move_left(data):
        rover.move_left()

    @sio.event
    def move_right(self):
        rover.move_right()

    @sio.event
    def stop(data):
        rover.stop()

    # If the application does not have anything to do in the main thread and just wants to wait until the connection with the server ends, it can call the wait() method:
    sio.wait()
except ConnectionError as err:
    print(f'Falha ao se comunicar com o servidor: {SERVER_URL}')
    print(err)
    raise SystemExit
