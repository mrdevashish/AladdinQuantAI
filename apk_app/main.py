import threading
from kivy.app import App
from kivy.uix.label import Label

import sys
sys.path.append("..")

from run_quant_pipeline import run_engines


class AladdinApp(App):

    def build(self):

        t = threading.Thread(target=run_engines)
        t.daemon = True
        t.start()

        return Label(text="AladdinQuantAI Running")


if __name__ == "__main__":
    AladdinApp().run()
