import flet as ft
from components.sidebar import Sidebar
from components.videoplayer import VideoPlayer


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Flet Video"
    page.window.always_on_top = True
    page.spacing = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    Sidebar(page)
    VideoPlayer(page)


app = ft.app(main, export_asgi_app=True)
