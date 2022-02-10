import re

input = open('input.txt', 'r').read().split('\n')


def check(str):
    if str not in " ":
        return True
    else:
        return False


def format_input(arr):
    answer = list(map(int, arr.pop(0).split(',')))

    boards = []
    board_arr = []

    for str in arr:
        row = list(map(int, list(filter(check, str.split(' ')))))
        if len(row) > 0:
            board_arr.append(row)
            if(len(board_arr) == 5):
                boards.append(board_arr)
                board_arr = []
    return {
        "answer": answer,
        "boards": boards
    }


def check_arr(n, arr):
    check = False
    for row in arr:
        if n in row:
            check = True
    return check


def check_boards(answer, boards):
    winners = []
    for board in boards:
        board_sum = sum([sum(row) for row in board])
        result = False
        winner = {
            "rounds": len(answer),
            "points": 0
        }

        for n in range(len(answer)):
            answer_slice = answer[:n+1]
            answer_sum = 0

            for x in range(5):
                check_row = 0
                check_col = 0

                for y in range(5):
                    if not result:
                        check_row += 1 if board[x][y] in answer_slice else 0
                        check_col += 1 if board[y][x] in answer_slice else 0

                        if check_row == 5 or check_col == 5:
                            for n in answer_slice:
                                if check_arr(n, board):
                                    answer_sum += n

                            if n < winner["rounds"]:
                                winner["points"] = (
                                    board_sum - answer_sum) * answer_slice[len(answer_slice)-1]
                                winner["rounds"] = len(answer_slice)
                            result = True
        winners.append(winner)
        lower = winners[0]
        for player in winners:
            if player["rounds"] > lower["rounds"]:
                lower = player

    return lower["points"]


formatted_input = format_input(input)


print(check_boards(formatted_input['answer'], formatted_input['boards']))
