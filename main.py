import flet as ft
from components.nav_bar import Navbar
from components.video_player import VideoPlayer


class Main:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.title = "Flet Video"
        self.page.window.always_on_top = True
        self.page.spacing = 20
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.navbar = Navbar(page)
        self.vp = VideoPlayer(page)
        self.banner = ft.Banner(
            ft.ListView(
                [
                    title := ft.TextField(label="Title", hint_text="Enter title"),
                    url := ft.TextField(label="Video URL", hint_text="Enter video URL"),
                ],
            ),
            bgcolor=ft.colors.AMBER_100,
            content_padding=10,
            actions=[
                ft.TextButton(
                    "Submit",
                    on_click=lambda e: self.vp.add_video(
                        url.value, {"title": title.value}
                    ),
                ),
                ft.TextButton("Close", on_click=self.close_banner),
            ],
        )

        self.navbar.add_navbar_action(
            ft.IconButton(ft.icons.ADD_CIRCLE_OUTLINE, on_click=self.open_banner),
            0,
        )

    def open_banner(self, e):
        self.page.open(self.banner)

    def close_banner(self, e):
        self.page.close(self.banner)


app = ft.app(target=Main, export_asgi_app=True)
