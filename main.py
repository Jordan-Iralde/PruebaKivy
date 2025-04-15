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
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label

numero = 0
Builder.load_string("""
<PaginaUno>:
    
    BoxLayout:
        Button:
            text: 'Sumar 1'
            on_press: root.ids.numero.value = self.value + 1
            
        Label:
            id: numero
            value: 2
 
        Button:
            text: 'Restar 1'
            on_press: root.ids.numero.text = 'Texto cambiado'
            
        Label:
            id: valor
            text = 'h'
            halign: 'center'
            valign: 'center'
    
    

""")

class PaginaUno(Screen):
    pass

class TestApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(PaginaUno(name='uno'))
        return sm

if __name__ == '__main__':
    TestApp().run()
    