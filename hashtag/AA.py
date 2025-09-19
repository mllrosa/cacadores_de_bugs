import flet as ft


def main(page: ft.Page):
    page.bgcolor = "#D3D3D3"
    page.title = "MENU APP"
    page.window.width = 500
    page.window.height = 900
    page.window.max_width = 500
    page.window.max_height = 900
    

    def gaveta_fechada(e):
        print(f"Gaveta Fechada")
    
    def gaveta_aberta(e):
        index = e.control.selected_index
        labels = ["INICIO","NOTIFICAÇÕES","DESEMPENHO","AMIGOS","SUPORTE","CONFIGURAÇÕES","SAIR"]

        if index is not None and 0 <= index < len(labels):
            print(f"Item {index + 1} - {labels[index]} foi selecionado no menu")

        page.close(gaveta_principal)

        

    gaveta_principal = ft.NavigationDrawer(
        on_dismiss=gaveta_fechada,
        on_change=gaveta_aberta,
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="INICIO",
                icon=ft.Icons.HOME_ROUNDED,
                selected_icon=ft.Icon(ft.Icons.HOME_ROUNDED),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.NOTIFICATIONS_ACTIVE),
                label="NOTIFICAÇÕES",
                selected_icon=ft.Icons.NOTIFICATIONS_ACTIVE,
            ),ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.ALIGN_VERTICAL_BOTTOM_SHARP),
                label="DESEMPENHO",
                selected_icon=ft.Icons.ALIGN_VERTICAL_BOTTOM_SHARP,
            ),ft.NavigationDrawerDestination(
                label="AMIGOS",
                icon=ft.Icons.MESSENGER,
                selected_icon=ft.Icon(ft.Icons.MESSENGER),
            ),ft.NavigationDrawerDestination(
                label="SUPORTE",
                icon=ft.Icon(ft.Icons.LIVE_HELP_ROUNDED),
                selected_icon=ft.Icon(ft.Icons.LIVE_HELP_ROUNDED),
            ),ft.NavigationDrawerDestination(
                label="CONFIGURAÇÕES",
                icon=ft.Icon(ft.Icons.SETTINGS),
                selected_icon=ft.Icon(ft.Icons.SETTINGS),
            ),ft.NavigationDrawerDestination(
                label="SAIR",
                icon=ft.Icon(ft.Icons.APP_BLOCKING),
                selected_icon=ft.Icon(ft.Icons.APP_BLOCKING),
            ),
        ],
    )


    gaveta_final = ft.NavigationDrawer(
        position=ft.NavigationDrawerPosition.END,
        on_dismiss=gaveta_fechada,
        on_change=gaveta_aberta,
        controls=[
            ft.NavigationDrawerDestination(
                icon=ft.Icons.ADD_TO_HOME_SCREEN_SHARP, label="Item 1"
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.ADD_COMMENT), label="Item 2"
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.ADD_LOCATION), label="Item 3",
            ),
        ],
    )

    botao_menu = ft.IconButton(
        icon=ft.Icons.MENU,
        icon_color=ft.Colors.BLUE_900, 
        icon_size=40,
        tooltip="Abrir menu",
        on_click=lambda e: page.open(gaveta_principal),
    )


    page.add(botao_menu)

   
ft.app(target=main)
