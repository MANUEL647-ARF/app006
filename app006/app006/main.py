import flet as ft
#se importan la libreta random
import random


def main(page: ft.Page):
    #se crean las variables globales
    global numero_secreto,entrada_numero,text_resultado,button_adivinar

    page.title="adivina el numero"
    
    #se genera un numero aleatorio entre 1 y 100
    numero_secreto=random.randint(1.100)
    
    #se genera la interfaz grafica
    titulo=ft.Text("adivina el numero",size=25,color="white")
    entrada_numero=ft.TextField(label="tu adivinanza entre 1 y 100",width=300)
    button_adivinar=ft.ElevatedButton("adivinar")
    text_resultado=ft.Text("",color="white")
    
    #se crea el conteneor de la interfaz grafica
    contenedor_principal=ft.Container(
        context=ft.Column(
            controls=[
                titulo,
                entrada_numero,
                button_adivinar,
                text_resultado,
                ft.Imagen(
                    src="https://i.ibb.co/Gxgryg9/laser.gif"
                    fit=ft.ImageFit.COVER,
                    width=350
                    height=300
                )
            ],aligment="CENTER",
            horinzontal_aligment="CENTER"
            spacing=20
        ),
        bgcolor="black",
        widht=page.window.width,
        height=page.window,height,
        padding=20
    )

    page.add(contenedor_principal)
ft.app(main)
