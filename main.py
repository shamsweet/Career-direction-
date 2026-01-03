from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CareerDirection(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(Label(text="Career Direction", font_size=28))
        layout.add_widget(Button(text="Start Learning"))
        layout.add_widget(Button(text="Quiz"))
        layout.add_widget(Button(text="Earn"))
        return layout

CareerDirection().run()