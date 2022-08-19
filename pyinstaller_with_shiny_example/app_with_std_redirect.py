import sys
from datetime import datetime
logfile = open('myapp2.log', 'a', 1)
sys.stdout = logfile
sys.stderr = logfile
# old_f = sys.stdout
# class F:
#     def write(self, x):
#         old_f.write(x.replace("\n", " [%s]\n" % str(datetime.now())))
# sys.stdout = F()
# sys.stderr = F()
from shiny import App, ui, reactive
# import logging

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


def server(input, output, session):
    @reactive.Effect
    @reactive.event(input.btn)
    def _():
        print("Trying a divide by 0")
        12/0

def create_app():
    return App(app_ui, server)

app = create_app()
app.run()
