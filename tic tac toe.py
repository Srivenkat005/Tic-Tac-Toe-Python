import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [' ']*9
        self.current_player = 'X'

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text='', width=10, height=3,
                                   command=lambda row=i, col=j: self.make_move(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def make_move(self, row, col):
        index = 3 * row + col
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state='disabled', disabledforeground=self.get_player_color())
            if self.check_winner():
                messagebox.showinfo("Winner!", f"Player {self.current_player} wins!")
                self.reset_board()
            elif ' ' not in self.board:
                messagebox.showinfo("Draw!", "The game ends in a draw!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_player_color(self):
        return 'red' if self.current_player == 'X' else 'blue'

    def check_winner(self):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return True
        return False

    def reset_board(self):
        self.board = [' ']*9
        for button in self.buttons:
            button.config(text='', state='normal')


def main():
    root = tk.Tk()
    ttt_gui = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
