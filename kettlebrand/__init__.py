
class MagicWorld:
    def __init__(self, app: str):
        self.app = app

    def say_hi(self) -> None:
        print(f"{self.app}: Hello world")
