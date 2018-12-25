class Token:
    def __init__(self, value):
        self._value = value

    def get_value(self):
        raise NotImplementedError

class NumberToken(Token):
    # Введенное значение пробуем перевести в float, 
    # чтобы проверить числовое ли это значени
    def __init__(self, value):
        self._value = float(value)

    def get_value(self) -> float:
        return self._value

class VariableToken(Token):
    def get_value(self) -> str:
        return self._value

class CommandToken(Token):
    def get_value(self) -> str:
        return self._value

class Parser:
    def process(self, line: str) -> [Token]:
        # Делим сторку на слова 
        words = line.split(' ')
        # Если слов больше трех, то выбрасываем ошибку
        if (len(words) > 3):
            raise RuntimeError('More than three tokens')
        tokens = []
        # Из слов создаем токены
        if (len(words) > 0):
            tokens.append(CommandToken(words[0]))
        if (len(words) > 1):
            tokens.append(NumberToken(words[1]))
        if (len(words) > 2):
            tokens.append(NumberToken(words[2]))
        return tokens