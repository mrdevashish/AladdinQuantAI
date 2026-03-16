from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import requests

SERVER = "http://127.0.0.1:9500/signals"


class Dashboard(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(orientation="vertical", **kwargs)

        self.price = Label(text="Price")
        self.gamma = Label(text="Gamma")
        self.liquidity = Label(text="Liquidity")
        self.signal = Label(text="Signal")

        self.add_widget(self.price)
        self.add_widget(self.gamma)
        self.add_widget(self.liquidity)
        self.add_widget(self.signal)

        Clock.schedule_interval(self.update,2)

    def update(self,dt):

        try:

            r = requests.get(SERVER)
            data = r.json()

            self.price.text = "Price: " + str(data["price"])
            self.gamma.text = "Gamma: " + data["gamma"]
            self.liquidity.text = "Liquidity: " + data["liquidity"]
            self.signal.text = "Signal: " + data["signal"]

        except:

            self.price.text = "Server offline"


class AppMain(App):

    def build(self):

        return Dashboard()


AppMain().run()
