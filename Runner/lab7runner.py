# Клас для запуску програми
from BLL.Lab7.APIApp import APIApp
from BLL.Lab7.APIClient import APIClient
from BLL.Lab7.DataSaver import DataSaver
from BLL.Lab7.InputParser import InputParser
from Shared.ReaderWriter import ReaderWriter
from Shared.Validator import Validator
from BLL.Lab7.History import History
from BLL.Lab7.ErrorHandler import ErrorHandler
from BLL.Lab7.ResultsDisplay import ResultsDisplay
from UI.MenuLab7 import MenuLab7


class RunnerLab7:
    def run_program(self):
        api_client = APIClient(api_url='https://jsonplaceholder.typicode.com/users')
        reader_writer = ReaderWriter()
        input_parser = InputParser()  # Creating an instance of the InputParser class
        validator = Validator()  # Passing the instance of the InputParser class to the Validator class
        history = History()
        error_handler = ErrorHandler()
        results_display = ResultsDisplay()
        data_saver = DataSaver()

        api_app = APIApp(api_client, reader_writer, validator, history, error_handler, results_display, input_parser,
                         data_saver)

        menu_lab7 = MenuLab7(api_app, validator, reader_writer)
        menu_lab7.run()


if __name__ == "__main__":
    RunnerLab7().run_program()


