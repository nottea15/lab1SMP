class ReaderWriter:
    def read_input(self, prompt):
        try:
            return input(prompt)
        except Exception as e:
            print(f"An error occurred while reading user input: {e}")
            return None

    def write_output(self, filename, content):
        try:
            with open(filename, 'w') as f:
                f.write(content)
        except Exception as e:
            print(f"An error occurred while writing to the file {filename}: {e}")