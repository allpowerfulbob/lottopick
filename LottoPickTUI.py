# Import textual app
from textual.app import App, ComposeResult
# Import textual widgets
from textual.widgets import Button, Header, Static
from textual.screen import Screen
from textual import events
# Import the LottoPickMain module
import LottoPickMain
# Import GenerateLottoNumbers
import GenerateLottoNumbers

class LottoPickAppScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Static(id="LottoPick")

class LottoPickApp(App):
    SCREENS = {"LottoPick": LottoPickAppScreen}

    def on_mount(self) -> None:
        self.push_screen("LottoPick")

    def action_set_background(self, color: str) -> None:
        self.screen.styles.background = color

    def on_key(self, event: events.Key) -> None:
        if event.key == "r":
            self.action_set_background("green")

    def compose(self):
        yield Header("Welcome to LottoPick!")

    def action_button_clicked(self) -> None:
        print("Generating Lotto Numbers...")

    def compose(self) -> ComposeResult:
        button = Button("Generate Lotto Numbers for Colorado Lottery")
        button._on_click(GenerateLottoNumbers.generate_lotto_numbers_colorado_lotto)
        yield button

    def compose(self) -> ComposeResult:
        button = Button("Generate Lotto Numbers for Power Ball.")
        button._on_click(GenerateLottoNumbers.generate_lotto_numbers_power_ball)
        yield button

    def compose(self) -> ComposeResult:
        button = Button("Generate Lotto Numbers for Mega Millions.")
        button._on_click(GenerateLottoNumbers.generate_lotto_numbers_mega_millions)
        yield button


if __name__ == "__main__":
    app = LottoPickApp()
    app.run()