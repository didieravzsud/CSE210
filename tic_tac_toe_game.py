"""Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, a column, or a diagonal
 with either three x's or three o's drawn in the spaces of a grid of nine squares.
 Autor: Didier Virguez
"""
def main():
    array = interface
    print(array)
    print(display_interface)

    player = next_player("")
    board = interface()
    while not (has_winner(board) or is_a_draw(board)):
        display_interface(board)
        make_move(player, board)
        player = next_player(player)
    display_interface(board)
    print("Good game. Thanks for playing!") 



def interface():
    numbers = []
    for square in range(9):
        numbers.append(square + 1)
    return numbers

def display_interface(interface):
    print()
    print(f"{interface[0]} {interface[1]} {interface[2]}")
    print(f"-+-+")
    print(f"{interface[3]} {interface[4]} {interface[5]}")
    print(f"-+-+")
    print(f"{interface[6]} {interface[7]} {interface[8]}")
    print()

def is_a_draw(interface):
    for square in range(9):
        if interface[square] != "x" and interface[square] != "o":
            return False
    return True 

def has_winner(interface):
    return (interface[0] == interface[1] == interface[2] or
            interface[3] == interface[4] == interface[5] or
            interface[6] == interface[7] == interface[8] or
            interface[0] == interface[3] == interface[6] or
            interface[1] == interface[4] == interface[7] or
            interface[2] == interface[5] == interface[8] or
            interface[0] == interface[4] == interface[8] or
            interface[2] == interface[4] == interface[6])


def make_move(player, interface):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    interface[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()