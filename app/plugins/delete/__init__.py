from app.commands import Command

class deleteHistoryCommand(Command):
    def execute(self, history_manager):
        index = int(input('entered the index to delete:'))
        history_manager.delete_record(index)
        print("Calculation history cleared successfully.")
