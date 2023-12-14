from Shared.ascii_art_library import ascii_art
from UI.Lab4UI import Lab4UI
from Shared.ReaderWriter import ReaderWriter
from Shared.Validator import Validator
from BLL.Lab4.ASCIIArtGenerator import ASCIIArtGenerator


class Runner:
    def __init__(self):
        self.reader_writer = ReaderWriter()
        self.validator = Validator()
        self.generator = ASCIIArtGenerator(ascii_art, self.reader_writer)
        self.menu = Lab4UI(self.generator, self.reader_writer, self.validator)

    def run(self):
        self.menu.run()

if __name__ == "__main__":
    runner = Runner()
    runner.run()