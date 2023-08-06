from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
# from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.button import Button
from kivy.uix.video import Video
# from kivy.uix.boxlayout import BoxLayout
import webbrowser
# from kivy.uix.webview import WebView

class WidgetsExample(Screen):
     pass
class Secondscreen(Screen):
    def open_percentage(self,video_id):
          url = f"https://www.youtube.com/watch?v={video_id}"
          webbrowser.open(url)
class Thirdscreen(Screen):
     def open_percentage(self,video_id):
          url = f"https://www.youtube.com/watch?v={video_id}"
          webbrowser.open(url)

class ForthScreen(Screen):
     def open_percentage(self,video_id):
          url = f"https://www.youtube.com/watch?v={video_id}"
          webbrowser.open(url)

class fifthscreen(Screen):
      def open_percentage(self,video_id):
          url = f"https://www.youtube.com/watch?v={video_id}"
          webbrowser.open(url)


class windowmanager(ScreenManager):
     pass


class MainWidget(Widget):
     pass
class labApp(App):
     pass
labApp().run()