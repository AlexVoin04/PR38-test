from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', 'false')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from datetime import datetime
import time
import os

class MainScreen(Screen):
    pass

class CameraScreen(Screen):
    def screen_shot(self,):
        camera = self.ids.camera
        camera.export_to_png("./" + datetime.now().strftime("Camera_"+"%Y%m%d_%H%M%S%f") + ".png")

class ScreensManager(ScreenManager):
    def build(self):
        self.current = "Main screen"


class MainApp(App):
    def build(self):
        return ScreensManager.build(self)
        
if __name__=="__main__":
    MainApp().run()