from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout


class GridLayoutExample(GridLayout):
    pass


class StackLayoutExample(StackLayout):
    def __init__(self, kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        b = Button(text="Push Me", size_hint=(.5, .5))
        self.add_widget(b)


class BoxLayoutExample(BoxLayout):
    pass


class MainWidget(Widget):
    pass

class KivyLayout(BoxLayout):
    pass
class BoxLayoutOne(BoxLayout):
    pass
class BoxLayoutTwo(BoxLayout):
    pass
class GridLayout1(GridLayout):
    pass

class WidgetLayoutApp(App):
    pass


WidgetLayoutApp().run()