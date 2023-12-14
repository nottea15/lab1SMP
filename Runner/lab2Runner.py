from BLL.Lab2.Calculator import Calculator


class RunnerLab2:
    def __init__(self, calc):
        self.calc = calc

    def run(self):
        self.calc.start_calculator()


if __name__ == '__main__':
    calculator = Calculator()
    runner = RunnerLab2(calculator)
    runner.run()
