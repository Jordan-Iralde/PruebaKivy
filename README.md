# PruebaKivy
Desarrollo de Apps con Kivy, Prueba de Kivy del 15/04/2025

Crear una aplicación móvil simple que muestre un número en pantalla y permita incrementarlo o reducirlo con botones.
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


# El main con errores ya esta arreglado

Funciona correctamente el contador usando BoxLayout, Label y Button, con inicialización en __init__ y binding a eventos; para mejorar, adáptalo a KivyMD (MDToolbar, MDLabel, MDRaisedButton), emplea nombres más descriptivos (contador, incrementar/decrementar).