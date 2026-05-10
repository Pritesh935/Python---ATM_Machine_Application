import tkinter as tk
from tkinter import messagebox, simpledialog


# ATM Class
class ATM:
    def __init__(self, pin=1234, balance=5000):
        self.pin = pin
        self.balance = balance
        self.history = []

    def check_balance(self):
        self.history.append(f"Checked Balance: ${self.balance}")
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited: ${amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrawn: ${amount}")
            return True
        return False

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            self.history.append("PIN Changed")
            return True
        return False


# Create ATM Object
atm = ATM()


# Main Window
root = tk.Tk()
root.title("Advanced Python ATM")
root.geometry("450x650")
root.configure(bg="#dff6ff")


# Title
title = tk.Label(
    root,
    text="ATM Machine",
    font=("Arial", 24, "bold"),
    bg="#dff6ff",
    fg="#003566"
)
title.pack(pady=20)


# PIN Entry
pin_label = tk.Label(
    root,
    text="Enter PIN",
    bg="#dff6ff",
    font=("Arial", 12)
)
pin_label.pack()

pin_entry = tk.Entry(root, show="*", font=("Arial", 12))
pin_entry.pack(pady=5)


# Amount Entry
amount_label = tk.Label(
    root,
    text="Enter Amount",
    bg="#dff6ff",
    font=("Arial", 12)
)
amount_label.pack()

amount_entry = tk.Entry(root, font=("Arial", 12))
amount_entry.pack(pady=5)


# Result Label
result_label = tk.Label(
    root,
    text="Welcome!",
    font=("Arial", 12, "bold"),
    bg="#dff6ff",
    fg="green"
)
result_label.pack(pady=10)


# Transaction History Box
history_box = tk.Text(
    root,
    height=10,
    width=40,
    font=("Arial", 10)
)
history_box.pack(pady=10)


# Login Status
logged_in = False


# Update Transaction History
def update_history():

    history_box.delete(1.0, tk.END)

    for item in atm.history:
        history_box.insert(tk.END, item + "\n")


# Login Function
def login():

    global logged_in

    try:
        entered_pin = int(pin_entry.get())

        if entered_pin == atm.pin:

            logged_in = True

            result_label.config(
                text="Login Successful!",
                fg="green"
            )

            enable_buttons()

            messagebox.showinfo(
                "Success",
                "Login Successful"
            )

        else:

            result_label.config(
                text="Incorrect PIN",
                fg="red"
            )

            messagebox.showerror(
                "Error",
                "Incorrect PIN"
            )

    except ValueError:

        messagebox.showerror(
            "Error",
            "PIN must be numeric"
        )


# Check Balance
def check_balance():

    if logged_in:

        balance = atm.check_balance()

        result_label.config(
            text=f"Current Balance: ${balance}",
            fg="blue"
        )

        update_history()


# Deposit Money
def deposit_money():

    if logged_in:

        try:
            amount = float(amount_entry.get())

            if atm.deposit(amount):

                result_label.config(
                    text=f"Deposited ${amount}",
                    fg="green"
                )

                update_history()

                amount_entry.delete(0, tk.END)

            else:

                messagebox.showerror(
                    "Error",
                    "Invalid Amount"
                )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter valid amount"
            )


# Withdraw Money
def withdraw_money():

    if logged_in:

        try:
            amount = float(amount_entry.get())

            if atm.withdraw(amount):

                result_label.config(
                    text=f"Withdrawn ${amount}",
                    fg="green"
                )

                update_history()

                amount_entry.delete(0, tk.END)

            else:

                messagebox.showerror(
                    "Error",
                    "Insufficient funds or invalid amount"
                )

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter valid amount"
            )


# Change PIN
def change_pin():

    if logged_in:

        old_pin = simpledialog.askinteger(
            "Change PIN",
            "Enter Old PIN"
        )

        new_pin = simpledialog.askinteger(
            "Change PIN",
            "Enter New PIN"
        )

        if old_pin and new_pin:

            if atm.change_pin(old_pin, new_pin):

                messagebox.showinfo(
                    "Success",
                    "PIN Changed Successfully"
                )

                update_history()

            else:

                messagebox.showerror(
                    "Error",
                    "Incorrect Old PIN"
                )


# Mini Statement
def mini_statement():

    if logged_in:

        if len(atm.history) == 0:

            messagebox.showinfo(
                "Mini Statement",
                "No Transactions Available"
            )

        else:

            statement = "\n".join(atm.history[-5:])

            messagebox.showinfo(
                "Mini Statement",
                f"Last 5 Transactions:\n\n{statement}"
            )


# Enable Buttons After Login
def enable_buttons():

    balance_btn.config(state="normal")
    deposit_btn.config(state="normal")
    withdraw_btn.config(state="normal")
    pin_btn.config(state="normal")
    statement_btn.config(state="normal")


# Buttons
login_btn = tk.Button(
    root,
    text="Login",
    width=20,
    bg="#003566",
    fg="white",
    font=("Arial", 11, "bold"),
    command=login
)
login_btn.pack(pady=10)


balance_btn = tk.Button(
    root,
    text="Check Balance",
    width=20,
    state="disabled",
    bg="green",
    fg="white",
    command=check_balance
)
balance_btn.pack(pady=10)


deposit_btn = tk.Button(
    root,
    text="Deposit",
    width=20,
    state="disabled",
    bg="orange",
    fg="white",
    command=deposit_money
)
deposit_btn.pack(pady=10)


withdraw_btn = tk.Button(
    root,
    text="Withdraw",
    width=20,
    state="disabled",
    bg="red",
    fg="white",
    command=withdraw_money
)
withdraw_btn.pack(pady=10)


pin_btn = tk.Button(
    root,
    text="Change PIN",
    width=20,
    state="disabled",
    bg="purple",
    fg="white",
    command=change_pin
)
pin_btn.pack(pady=10)


statement_btn = tk.Button(
    root,
    text="Mini Statement",
    width=20,
    state="disabled",
    bg="brown",
    fg="white",
    command=mini_statement
)
statement_btn.pack(pady=10)


exit_btn = tk.Button(
    root,
    text="Exit",
    width=20,
    bg="black",
    fg="white",
    command=root.destroy
)
exit_btn.pack(pady=20)


# Run Window
root.mainloop()
