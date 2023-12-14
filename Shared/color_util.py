# Utility class for adding color to text in a terminal
class ColorUtil:
    # Define color codes as ANSI escape sequences
    colors = {
        'white': '\033[1;37m',  # Білий текст
        'grey': '\033[1;30m',  # Сірий текст
        'reset': '\033[0m'  # Скидання кольору
    }

    @classmethod
    def colorize(cls, text, color='white'):
        color_code = cls.colors.get(color)
        if color_code:
            return f"{color_code}{text}{cls.colors['reset']}"
        else:
            return text