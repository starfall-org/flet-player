import flet as ft


class Navbar:
    def __init__(self, page: ft.Page):
        self.page = page
        self.navbar_popup_items = []
        self.navbar_actions = [
            ft.PopupMenuButton(items=self.navbar_popup_items, icon=ft.Icons.MORE_VERT),
        ]
        self.page.appbar = ft.AppBar(
            leading=ft.Icon(ft.Icons.PALETTE),
            leading_width=40,
            title=ft.Text(self.page.title),
            center_title=False,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            actions=self.navbar_actions,
        )

    def check_item_clicked(self, e):
        e.control.checked = not e.control.checked
        self.page.update()

    def add_navbar_action(self, control: ft.Control, position: int = -1):
        self.navbar_actions.insert(position, control)
        self.page.update()

    def add_navbar_popup_item(self, popup_item: ft.PopupMenuItem):
        self.navbar_popup_items.append(popup_item)
        self.page.update()
