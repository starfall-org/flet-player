import flet as ft


class VideoPlayer:
    def __init__(self, page: ft.Page):
        self.page = page
        self.playlist = []

        self.page.add(
            ft.Video(
                expand=True,
                playlist=self.playlist,
                playlist_mode=ft.PlaylistMode.LOOP,
                fill_color=ft.Colors.BLACK,
                aspect_ratio=16 / 9,
                volume=100,
                autoplay=False,
                filter_quality=ft.FilterQuality.HIGH,
                muted=False,
                on_loaded=self.change_title,
            ),
        )

    def change_title(self, e):
        self.page.title = f"Flet Video - {e}"
        self.page.update()

    def add_video(self, video_url: str, metadata: dict):
        self.playlist.append(
            ft.VideoMedia(
                video_url,
                extras=metadata,
            )
        )
        self.page.update()
