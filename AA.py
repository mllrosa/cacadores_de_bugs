import flet as ft

def main(page: ft.Page):
    page.title = 'AA'
    page.theme_mode = "dark"
    page.window.height = 900
    page.window.width = 500
    page.window.max_width = 500
    
    entrada = ft.TextField(label="BB")
    page.add(entrada)

ft.app(target=main)

