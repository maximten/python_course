from tokens import Token, Parser, CommandToken
from command import Context, CommandConstructor, Command, Operand

class Controller:
    def __init__(
            self,
            parser: Parser,
            constructor: CommandConstructor,
    ) -> None:
        self.__parser = parser
        self.__constructor = constructor

    def run(self) -> None:
        context = self.__create_context()

        context.set_run_state(True)
        while context.is_running():
            # Читаем строку пользователя
            raw_line = self.__read_raw_line()

            # Разбиваем строку на токены
            tokens = self.__parse_tokens(raw_line)

            # Из первого токена понимаем какая команда
            command = self.__construct_command(tokens)

            # Загружаем операнды из остальных токенов в контекст
            context = self.__update_context(context, tokens)

            # Берем операнды и выполняем над ними операцию,
            # результат команды кладем в левый операнд
            self.__execute_command(command, context)

            # Печатаем левый операнд
            self.__write_result(context)

    def __create_context(self) -> Context:
        return Context()

    def __read_raw_line(self) -> str:
        return input("> ")

    def __parse_tokens(self, line: str) -> [Token]:
        return self.__parser.process(line)

    def __update_context(self, context: Context, tokens: [Token]) -> Context:
        # Загружаем левый операнд в контекст
        if (len(tokens) > 1):
            context.set_left_operand(Operand(tokens[1]))
        # Загружаем правый операнд в контекст
        if (len(tokens) > 2):
            context.set_right_operand(Operand(tokens[2]))        
        return context

    def __construct_command(self, tokens: [Token]) -> Command:
        command_token = self.__get_command_token(tokens)
        command_name = command_token.get_value()
        command = self.__constructor.create(command_name)
        return command

    def __get_command_token(self, tokens: [Token]) -> CommandToken:
        return tokens[0]

    def __execute_command(self, command: Command, context: Context) -> bool:
        command.execute(context)
        return True

    def __write_result(self, context: Context) -> None:
        left_operand_value = context.get_left_operand().get_value()
        print(left_operand_value)
