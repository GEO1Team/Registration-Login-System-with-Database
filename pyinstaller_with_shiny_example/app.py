import signal
from shiny import App, render, ui
import webbrowser
import os
import pick_port

app_ui = ui.page_fluid(
    ui.h2("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
)
port = pick_port.get_unused_port()

url = f'http://localhost:{port}'
def server(input, output, session):
    print("New connection open!")
    def session_opened():
        print("New Session Opened -Chandler")
    
    def close_server():
        print("Session ended so stopping server.")
        os.kill(os.getpid(), signal.SIGINT)
        print("Finished")

    session.on_ended(close_server)

    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"

webbrowser.open(url)
app = App(app_ui, server)
app.run(port=port)
