import tkinter as tk
from tkinter import messagebox

# Variables
currPlayer = False
refresher = 0
board = [["" for _ in range(3)] for _ in range(3)]

# Function to check for a winner
def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return True
    return False

# Function to reset the board
def reset_board():
    global refresher
    refresher = 0
    for button in app.winfo_children():
        if isinstance(button, tk.Button):
            button.config(text="")
    for row in range(3):
        for col in range(3):
            board[row][col] = ""

# Function to update the button text
def update_button(btn, row, col):
    global currPlayer
    global refresher

    if btn["text"]:
        print(btn["text"])
    else:
        print("Button can't be accessed")
    
    if btn["text"] == "":  
        text = "O" if currPlayer else "X"
        btn.config(text=text)
        board[row][col] = text
        refresher += 1

        # Check for a winner
        if check_winner():
            winner = "O" if currPlayer else "X"
            messagebox.showinfo("Winner", f"Player {winner} wins!")
            reset_board()
        elif refresher == 9:  # Check for a tie
            messagebox.showinfo("Tie", "It's a tie!")
            reset_board()
    
    else:
        messagebox.showwarning("Invalid Move", "This button is already used. Please choose another one.")
    
    currPlayer = not currPlayer  # Toggle the player

# Initialize the main app
app = tk.Tk()
app.title("Tic-Tac-Toe Game")
app.geometry("590x630")
app.resizable(False, False)

# Button configuration
buttons = [
    ('', 1, 0), ('', 1, 1), ('', 1, 2), 
    ('', 2, 0), ('', 2, 1), ('', 2, 2), 
    ('', 3, 0), ('', 3, 1), ('', 3, 2), 
]

# Add buttons to the grid
for (text, row, column) in buttons:
    button = tk.Button(app, text=text, bg="grey", cursor="hand2", width=5, height=3, fg="white", font=("Arial", 40, "bold"))
    button.config(command=lambda b=button, r=row-1, c=column: update_button(b, r, c))
    button.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)

# Run the app
app.mainloop()

