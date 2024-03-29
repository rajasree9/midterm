import logging
from app.commands import Command

class MultiplyCommand(Command):
    def execute(self, history_manager):
        value1 = float(input('Enter the first value: '))
        value2 = float(input('Enter the second value: '))
        result = value1 * value2
        print(f"The result of multiplication: {result}")
        history_manager.add_record('multiply', value1, value2)
