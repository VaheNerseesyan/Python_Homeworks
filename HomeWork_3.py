# EXTRA TASK
def remove_duplicates_direct(input_list: list) -> list:
    i = 0
    while i < len(input_list):
        print("i: ", i, "len inp list: ", len(input_list))
        j = i + 1
        while j < len(input_list):
            print("j: ", j, "len inp list: ", len(input_list))
            print("input_list[i]: ", input_list[i], "input_list[j]: ", input_list[j])
            if input_list[i] == input_list[j]:
                print(
                    "input_list[i]: ", input_list[i], "input_list[j]: ", input_list[j]
                )
                for k in range(j, len(input_list) - 1):
                    #                  ^ this range is given like range(j, len(input_list) -1) because we want to push the
                    #                    duplicate num to the end of list, for using .pop() function and delete the duplicate
                    #                    from the end of list. For this example list_input[i] = 1 and the list_input[j] = 1 too,
                    #                    so we use j in for loop, because we are keeping in mind the i index of num(that's 1), and
                    #                    then we are checking that with the next elems, here it is the elem with j index of the list
                    print("k: ", k)
                    input_list[k] = input_list[k + 1]
                    print(
                        "input_list[k]: ",
                        input_list[k],
                        "input_list[k + 1]: ",
                        input_list[k + 1],
                    )
                input_list.pop()
                print("input_list: ", input_list)
            else:
                j += 1
        i += 1
    return input_list


# input_list = [0, 1, 1, 2, 2, 3, 4, 5, 5, 2]
# print(remove_duplicates_direct(input_list))


# TIC TAC TOE


def print_board(board):
    """
    Board printing with rows
    """
    row1 = f"| {board[0]} | {board[1]} | {board[2]} |"
    row2 = f"| {board[3]} | {board[4]} | {board[5]} |"
    row3 = f"| {board[6]} | {board[7]} | {board[8]} |"
    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def player_move(player, board):
    """
    Move player with indexed places
    checking taken places
    """
    while True:
        print()
        print(f"Your turn player {player}")
        try:
            place = int(input("Enter your move (1-9): "))
            if board[place - 1] == " ":
                board[place - 1] = player
                break
            else:
                print()
                print("That space is already taken!")
        except ValueError:
            print("Please enter a valid place index!!")


def is_victory(player, board):
    """
    eight victory combinations checker
    """
    if (
        (board[0] == player and board[1] == player and board[2] == player)
        or (board[3] == player and board[4] == player and board[5] == player)
        or (board[6] == player and board[7] == player and board[8] == player)
        or (board[0] == player and board[3] == player and board[6] == player)
        or (board[1] == player and board[4] == player and board[7] == player)
        or (board[2] == player and board[5] == player and board[8] == player)
        or (board[0] == player and board[4] == player and board[8] == player)
        or (board[2] == player and board[4] == player and board[6] == player)
    ):
        return True
    else:
        return False


def is_draw(board):
    """
    checking draw combinations by the available places
    """
    if " " not in board:
        return True
    else:
        return False


def win_count():
    try:
        k = int(input("Input the count of wins ! "))
        if k <= 0 or not isinstance(k, int):
            print("Invalid input !")
            print()
            return win_count()
        print()
        return k
    except ValueError:
        print("Invalid input !")
        print()
        return win_count()


def printer():
    print()
    print("Welcome to game Tic-Tac-Toe 3x3 by Vahe !")
    row11 = "| 1 | 2 | 3 |"
    row22 = "| 4 | 5 | 6 |"
    row33 = "| 7 | 8 | 9 |"
    print()
    print(row11)
    print(row22)
    print(row33)
    print()
    print("REMEMBER, THIS IS THE MAKET OF INDEXES IN THE GAME !")
    print()
    print()


def tic_tac_toe():
    printer()
    while True:
        score_x = 0
        score_o = 0
        n = 0
        k = win_count()
        while n <= k:
            board = [" " for x in range(9)]
            while True:
                first_player = input("First Player, what do you want to be X or O? ")
                if first_player == "x" or first_player == "X":
                    second_player = "O"
                    first_player = "X"
                    print()
                    print(
                        f"Well, First Player you are {first_player}, and the Second Player is {second_player} !"
                    )
                    print()
                elif first_player == "o" or first_player == "O":
                    second_player = "X"
                    first_player = "O"
                    print()
                    print(
                        f"Well, First Player you are {first_player}, and the Second Player is {second_player} !"
                    )
                    print()
                else:
                    print("Invalid player option !")
                    print()
                    break
            while True:
                print(f"Score | First player:{score_x} Second player:{score_o}")
                player_move(first_player, board)
                print_board(board)
                if is_victory(first_player, board):
                    n += 1
                    score_x += 1
                    print("X wins! Congratulations!")
                    print()
                    print(f"Score | First player:{score_x} Second player:{score_o}")
                    break
                elif is_draw(board):
                    print("It's a draw!")
                    break
                print(f"Score | First player:{score_x} Second player:{score_o}")
                player_move(second_player, board)
                print_board(board)
                if is_victory(second_player, board):
                    n += 1
                    score_o += 1
                    print("O wins! Congratulations!")
                    print()
                    print(f"Score | First player:{score_x} Second player:{score_o}")
                    break
                elif is_draw(board):
                    print("It's a draw!")
                    break
            n += 1


if __name__ == "__main__":
    tic_tac_toe()
