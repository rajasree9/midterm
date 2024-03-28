from app.commands import Command

class LoadHistoryCommand(Command):
    def execute(self, history_manager):
        history_manager.load_history()
        print("Calculation history loaded successfully.")
