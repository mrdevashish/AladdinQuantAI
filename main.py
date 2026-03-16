from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import requests


SERVER_URL = "http://127.0.0.1:8000/signals"


class Dashboard(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.status = Label(text="AladdinQuantAI Mobile Dashboard")
        self.price = Label(text="Price: loading...")
        self.gamma = Label(text="Gamma: loading...")
        self.liquidity = Label(text="Liquidity: loading...")

        self.add_widget(self.status)
        self.add_widget(self.price)
        self.add_widget(self.gamma)
        self.add_widget(self.liquidity)

        Clock.schedule_interval(self.update_data, 5)

    def update_data(self, dt):
        try:
            r = requests.get(SERVER_URL, timeout=3)
            data = r.json()

            self.price.text = f"Price: {data.get('price')}"
            self.gamma.text = f"Gamma: {data.get('gamma')}"
            self.liquidity.text = f"Liquidity: {data.get('liquidity')}"

        except Exception as e:
            self.status.text = f"Server error: {e}"


class AladdinApp(App):

    def build(self):
        return Dashboard()


if __name__ == "__main__":
    AladdinApp().run()
