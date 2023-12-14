from Shared.ReaderWriter import ReaderWriter
from Shared.Validator import Validator
from UI.Lab5UI import Lab5UI


class Runner5Lab:
    def __init__(self):
        self.reader_writer = ReaderWriter()
        self.validator = Validator()
        self.menu = Lab5UI(self.reader_writer, self.validator)

    def run(self):
        self.menu.run()

if __name__ == "__main__":
    runner = Runner5Lab()
    runner.run()

