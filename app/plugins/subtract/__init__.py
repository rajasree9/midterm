from app.commands import Command

class SubtractCommand(Command):
    def execute(self, history_manager):
        value1 = float(input('Enter the first value: '))
        value2 = float(input('Enter the second value: '))
        result = value1 - value2
        print(f"The result of subtraction: {result}")
        history_manager.add_record('subtract', value1, value2)
