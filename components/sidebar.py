import flet as ft


class Sidebar:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.drawer = ft.NavigationDrawer(
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    label="Item 1",
                    icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                    selected_icon=ft.Icon(ft.Icons.DOOR_BACK_DOOR),
                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    icon=ft.Icon(ft.Icons.MAIL_OUTLINED),
                    label="Item 2",
                    selected_icon=ft.Icons.MAIL,
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icon(ft.Icons.PHONE_OUTLINED),
                    label="Item 3",
                    selected_icon=ft.Icons.PHONE,
                ),
            ],
        )

        self.page.add(
            ft.IconButton(
                icon=ft.icons.MENU,
                icon_color=ft.colors.BLACK,
                icon_size=30,
                tooltip="Menu",
                on_click=self.toggle_drawer,
                padding=0,
            )
        )

    def toggle_drawer(self, e):
        self.page.open(self.drawer)
