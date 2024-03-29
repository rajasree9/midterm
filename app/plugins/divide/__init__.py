from app.commands import Command

class DivideCommand(Command):
    def execute(self, history_manager):
        value1 = float(input('Enter the first value: '))
        value2 = float(input('Enter the second value: '))
        if value2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = value1 / value2
            print(f"The result of division: {result}")
            history_manager.add_record('divide', value1, value2)
