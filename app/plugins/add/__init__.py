from app.commands import Command

class AddCommand(Command):
    def execute(self, history_manager):
        value1 = float(input('Enter the first value: '))
        value2 = float(input('Enter the second value: '))
        result = value1 + value2
        print(f"The result of addition: {result}")
        history_manager.add_record('add', value1, value2)
