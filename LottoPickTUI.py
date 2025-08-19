# Import textual app
from textual.app import App
# Import textual widgets
from textual.widgets import Button, Header
from textual import events
# Import the LottoPickMain module
import LottoPickMain
# Import GenerateLottoNumbers
import GenerateLottoNumbers

class LottoPickApp(App):
    def action_set_background(self, color: str) -> None:
        self.screen.styles.background = color

    def on_key(self, event: events.Key) -> None:
        if event.key == "r":
            self.action_set_background("green")

    def compose(self):
        yield Header("Welcome to LottoPick!")

    def action_button_clicked(self) -> None:
        print("Generating Lotto Numbers...")

    def compose(self) -> GenerateLottoNumbers.generate_lotto_numbers_colorado_lotto:
        button = Button("Generate Lotto Numbers for Colorado Lottery")
        button.on_click(self.GenerateLottoNumbers.generate_lotto_numbers_colorado_lotto)
        yield button


if __name__ == "__main__":
    app = LottoPickApp()
    app.run()