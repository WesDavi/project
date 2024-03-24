from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Main(App):
    def build(self):
        return Tarefas(['fazer compras', 'buscar filhos', 'lavar louça'], orientation = 'horizontal')

class Tarefas(BoxLayout):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.add_widget(Label(text= tarefa))

Main().run()