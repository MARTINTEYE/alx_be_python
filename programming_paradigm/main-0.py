# main-0.py

import sys 
from bank_account import BankAccount  # Import your BankAccount class

def main():
    # Create a new BankAccount instance with GHS 100 initial balance
    account = BankAccount(100)

    # Check if the user has provided a command
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Get command and optional parameters by splitting the first argument at ":"
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Handle deposit
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: GHS {amount:.2f}")

    # Handle withdrawal
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: GHS {amount:.2f}")
        else:
            print("Insufficient funds.")

    # Handle balance display
    elif command == "display":
        account.display_balance()

    # Handle invalid command
    else:
        print("Invalid command.")



