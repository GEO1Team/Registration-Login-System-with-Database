import signal
from shiny import App, ui, reactive
import webbrowser
import os
import pick_port
import logging


logging.basicConfig(filename='myapp.log', level=logging.INFO, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


def wrap_try_catch(f):
    def wrapper():
        try:
            f()
        except:
            logging.exception("Something went wrong")
            raise
    return wrapper


def ui_card(title, *args):
    return (
        ui.div(
            {"class": "card mb-4"},
            ui.div(title, class_="card-header"),
            ui.div({"class": "card-body"}, *args),
        ),
    )

app_ui = ui.page_fluid(
    ui_card(
        "This button will attempt a divide by zero",
        ui.input_action_button("btn", "Push to Crash"),
    ),
)

port = pick_port.get_unused_port()
url = f'http://localhost:{port}'


def server(input, output, session):
    print("New connection open!")    
    def close_server():
        print("Session ended so stopping server.")
        os.kill(os.getpid(), signal.SIGINT)
        print("Finished")

    session.on_ended(close_server)

    @reactive.Effect
    @reactive.event(input.btn)
    @wrap_try_catch
    def _():
        print("You pushed me!")
        10/0

def create_app():
    return App(app_ui, server)


webbrowser.open(url)
app = create_app()
app.run(port=port)
