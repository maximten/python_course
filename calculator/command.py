from typing import Type
from tokens import NumberToken

class Operand:
    def __init__(self, value: None):
        if hasattr(value, 'get_value'): 
            self._value = value.get_value()
        else:
            self._value = value

    def get_value(self) -> float:
        return self._value

class Context:
    def __init__(self):
        self.__is_running = False
        self.__left_operand = None
        self.__right_operand = None 

    def set_run_state(self, state: bool) -> None:
        self.__is_running = state

    def is_running(self) -> bool:
        return self.__is_running

    def get_operands(self) -> [Operand]:
        return [self.__left_operand, self.__right_operand]

    def get_left_operand(self) -> Operand:
        return self.__left_operand

    def get_right_operand(self) -> Operand:
        return self.__right_operand

    def get_variables(self):
        pass

    def set_variable(self, var) -> None:
        pass

    def set_left_operand(self, op: Operand):
        self.__left_operand = op

    def set_right_operand(self, op: Operand):
        self.__right_operand = op

class Command:
    def execute(self, context: Context) -> None:
        pass

class CommandConstructor:
    def __init__(self):
        self.__command_dict = {}

    def register(self, name: str, command_class: Type[Command]) -> None:
        self.__command_dict[name] = command_class

    def create(self, name: str) -> Command:
        command_class = self.__command_dict[name]
        return command_class()

class ExitCommand(Command):
    def execute(self, context: Context):
        context.set_run_state(False)

class PlusCommand(Command):
    def execute(self, context: Context):
        left_operand_value = context.get_left_operand().get_value() 
        right_operand_value = context.get_right_operand().get_value()
        result_value = left_operand_value + right_operand_value
        result_operand = Operand(result_value)
        context.set_left_operand(result_operand)
        
