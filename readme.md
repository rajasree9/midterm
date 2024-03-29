# Calculator program

## DEMONSTRATION VIDEO :  

## Clone the Repository:
git clone [repository_link]

## Navigate to the Project Directory:
cd calculator_project

## Install Dependencies: 
pip install -r requirements.txt

## Run the Application:
python main.py

## Calculator Commands:

Use commands like add, subtract, multiply, and divide to perform arithmetic operations.
Use the menu command to list all available commands.
Use the load command to view calculation history.
Use the clear command to clear the entire history.
Use the delete command to delete specific records from history.

## example usage

Addition Operation:

Type the command 'add' in the REPL command interface.
Enter the numbers when asked in the interface.
It computes and prints the result.

>>> add
Enter the first number: 5
Enter the second number: 4
Result: 9.0

Other Operations:

subtract for subtraction
multiply for multiplication
divide for division

## Commands for Calculation History

load : 
It retrieves all the data from the .csv file

>>> load
Data history of calculator:  Operation  Value1  Value2
1   multilpy     3.0     2.0
2   divide     6.0     2.0
3   divide     6.0     0.0

Clear:

It deletes the stored history
 
>>> clear
Calculation history cleared successfully

Delete:

It deletes a particular row in the history by the ID field

>>> delete
entered the index to delete: 1
Record at index 1 deleted from history. Operation  Value1  Value2
2   multiply     3.0     2.0
3   divide     6.0     2.0
4   divide     6.0     0.0

## Testing with Pytest:

Run pytest to execute the unit tests:
pytest

## Command Pattern:

The Command pattern is utilized to encapsulate each operation (addition, subtraction, multiplication, division) as a separate command object.
Each command object has an execute method that performs the corresponding operation when invoked.
This pattern allows you to decouple the requester (user input or menu selection) from the concrete operations, promoting flexibility and extensibility.

## Facade Pattern:

The Facade pattern is applied in the CalculationHistory class, which acts as a simplified interface for managing calculation history.
The class provides high-level methods such as add_record, clear_history, delete_record, etc., hiding the complexity of interacting with the underlying data structures (e.g., CSV files managed using pandas).
By encapsulating the logic for history management, the Facade pattern promotes code readability and maintainability.

## Factory Method Pattern:

The Factory Method pattern is employed in dynamically loading and integrating plugins without modifying the core application code.
The load_plugin method in the application's initialization dynamically loads new plugins based on configuration or external input.
This pattern allows for the addition of new functionality (e.g., new calculator operations) without the need to modify existing code, enhancing the application's scalability.

## Singleton Pattern:

The Singleton pattern ensures that there is only one instance of the MenuCommand class throughout the application.
This pattern restricts the instantiation of the class to a single instance, providing a global point of access to the menu command functionality.
Singleton pattern ensures that the application's menu command remains consistent and coherent across different parts of the system.

## EAFP (Easier to Ask for Forgiveness than Permission) 
Is a programming philosophy or approach commonly associated with Python programming. The EAFP principle emphasizes writing code that assumes the validity of operations and handles exceptions when they occur, rather than explicitly checking for conditions before performing an action.





