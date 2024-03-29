from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name, command):
        self.commands[command_name] = command

    def execute_command(self, command_name, instance):
        if command_name in self.commands:
            self.commands[command_name].execute(instance)  # Assuming execute() method exists in your command object
        else:
            raise KeyError(f"Command '{command_name}' not found.")
