from pico2d import load_image, clear_canvas, update_canvas, get_events


def init():
    global image
    global running

    running = True
    image = load_image('tuk_credit.png')

def finish():
    pass

def update():
    pass

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()