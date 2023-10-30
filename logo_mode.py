from pico2d import load_image, clear_canvas, update_canvas, get_events, get_time
import game_framework

def init():
    global image
    global running
    global logo_start_time

    running = True
    image = load_image('tuk_credit.png')
    logo_start_time = get_time()

def finish():
    pass

def update():
    if get_time() - logo_start_time >= 2.0:
        game_framework.quit()

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()