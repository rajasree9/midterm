from app.commands import Command

class ClearHistoryCommand(Command):
    def execute(self, history_manager):
        history_manager.clear_history()
        print("Calculation history cleared successfully.")
