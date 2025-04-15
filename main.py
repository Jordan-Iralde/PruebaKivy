'''
Crear una aplicación móvil simple que muestre un número en pantalla y permita incrementarlo o
reducirlo con botones.
Requisitos:
Usar solo main.py (no usar archivos .kv).
Crear una interfaz con:
Una MDToolbar con el título “Contador KivyMD”.
Un número centrado (MDLabel) que comience en 0.
Dos botones (MDRaisedButton) con los signos "+" y "–".
El botón "+" debe sumar 1 al número cada vez que se presiona.
El botón "–" debe restar 1 al número.
El número debe actualizarse en pantalla.

PD: Adjunto un archivo .zip que contiene una posible solución con errores.
'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label





class MyBoxLayout(BoxLayout):
    
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        self.numeros = 0
        self.orientation = 'vertical'
        self.label = Label(text=str(0))
        
        self.button = Button(text='Sumar 1')
        self.button.bind(on_press=self.add)
        
        self.button2 = Button(text='Restar 1')
        self.button2.bind(on_press=self.sub)
        
        self.add_widget(self.label)
        self.add_widget(self.button)
        self.add_widget(self.button2)
    
    def add(self, instance):
        self.numeros += 1
        self.label.text = str(self.numeros)
        
    def sub(self, instance):
        self.numeros -= 1
        self.label.text = str(self.numeros)

class TestApp(App):
    def build(self):
        return MyBoxLayout()        

if __name__ == '__main__':
    TestApp().run()