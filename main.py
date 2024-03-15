import flet as ft
import requests
from time import sleep

def main(page: ft.Page):
    count = 0
    def get_api():
        api = 'https://kovadev.pythonanywhere.com'
        response = requests.get(api)
        if response.status_code==200:
            data = response.json()
            count = data["count"]
        else:
            count = 'Servicio no disponible'
        return count
    
    def post_api():
        api = 'https://kovadev.pythonanywhere.com'
        response = requests.post(api)
        if response.status_code==200:
            data = response.json()
            count = data["count"]
        elif response.status_code==429:
            subt = "Pará un poco, chango"
            return subt
        else:
            count = 'Servicio no disponible'
        return count
    
    count=get_api()
        
    page.title = "Trastorno del EDET postraumático"
    fe = ft.Text(value='EDET y la concha de tu madre',size=52, font_family="Aptos",no_wrap=False)
    text = ft.Text(value=f'{count}', size=120, weight='bold')
    
    def increment_count(e):
        count=post_api()
        if count == "Pará un poco, chango":
            subtext.value=f'{count}'
        else:
            text.value=f'{count}'           
        page.update()
        
    subtext = ft.Text(value='',size=16,color='red')
    button = ft.ElevatedButton(content=ft.Text(value="Putear",size=30), on_click=increment_count,autofocus=True,icon='exclamation_mark',icon_color='red',width=150,height=60, color='red')    
    credits = ft.Text(value='©2024 Kovadev - Brindando catarsis no resposive desde 1998',color='#4f4f4f',weight='bold')
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    d1 = ft.Container(
        content=ft.Image(src='https://raw.githubusercontent.com/gamartin23/electrones/main/descarga.png',width=500),
        alignment=ft.alignment.center,
        padding=60)
    page.add(d1)
    arow=ft.Row([fe], alignment=ft.MainAxisAlignment.CENTER)
    brow=ft.Row([text], alignment=ft.MainAxisAlignment.CENTER)
    crow=ft.Row([subtext], alignment=ft.MainAxisAlignment.CENTER)
    drow=ft.Row([button], alignment=ft.MainAxisAlignment.CENTER)
    page.add(ft.Column([arow,brow,crow,drow],alignment=ft.MainAxisAlignment.CENTER,expand=True))
    rowk = ft.Row(([credits]),alignment=ft.MainAxisAlignment.CENTER)
    page.add(ft.Column([rowk],alignment=ft.alignment.bottom_center))
    while True:
        get_api()
        sleep(5)

ft.app(target=main)
