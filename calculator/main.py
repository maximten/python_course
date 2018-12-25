from tokens import Parser
from command import *
from controller import Controller

command_constructor = CommandConstructor()
command_constructor.register("EXIT", ExitCommand)
command_constructor.register("ADD", PlusCommand)

controller = Controller(
    parser=Parser(),
    constructor=command_constructor,
)

controller.run()