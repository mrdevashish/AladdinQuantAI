from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import requests


SERVER_URL = "http://127.0.0.1:8000/signals"


class Dashboard(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(orientation="vertical", **kwargs)

        self.title = Label(text="AladdinQuantAI")
        self.price = Label(text="Price loading...")
        self.gamma = Label(text="Gamma loading...")
        self.liquidity = Label(text="Liquidity loading...")
        self.signal = Label(text="Signal loading...")

        self.add_widget(self.title)
        self.add_widget(self.price)
        self.add_widget(self.gamma)
        self.add_widget(self.liquidity)
        self.add_widget(self.signal)

        Clock.schedule_interval(self.update_data,2)

    def update_data(self,dt):

        try:

            r = requests.get(SERVER_URL)
            data = r.json()

            self.price.text = "Price: " + str(data["price"])
            self.gamma.text = "Gamma: " + data["gamma"]
            self.liquidity.text = "Liquidity: " + data["liquidity"]
            self.signal.text = "AI Signal: " + data["signal"]

        except:

            self.price.text = "Server not running"


class AladdinApp(App):

    def build(self):

        return Dashboard()


if __name__ == "__main__":
    AladdinApp().run()
