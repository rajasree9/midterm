from app.commands import Command

class LoadHistoryCommand(Command):
    def execute(self, history_manager):
        loaded_data= history_manager.load_history()
        print("Calculation history loaded successfully.", loaded_data)
