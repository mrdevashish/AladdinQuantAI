from kivy.app import App
from kivy.uix.label import Label


class AladdinApp(App):

    def build(self):
        return Label(text="AladdinQuantAI Mobile Dashboard")


if __name__ == "__main__":
    AladdinApp().run()
