from app.commands import Command

class MenuCommand(Command):
    def execute(self, command_handler):
        # Your command execution logic goes here
        print("menu",command_handler.commands.keys())

