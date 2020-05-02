#!/usr/bin/env python3
import random

board_size=3
board=[[0 for j in range(board_size)] for i in range(board_size)]
from enum import Enum

## transform numbers to letters for printed board
printable = {-1: "O", 0: " ",1: "X"}

class GameState(Enum):
    IN_PROGRESS = 0
    DRAW = 1
    X_WINS = 2
    O_WINS = 3

def transform(value):
    return printable[value]

def print_board(board):
    print()
    for row in board:
        print([transform(element) for element in row])
    print()

def player_wins(player):
    if player == 1:
        result = GameState.X_WINS
    else:
        result = GameState.O_WINS
    return result

def make_move(board,move,player):
    i, j = move
    board[i][j]=player

def legal_moves(board):
    result = []
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 0:
                result.append((i,j))        
    random.shuffle(result)
    return result

def get_game_state(board,player):
    result = GameState.IN_PROGRESS

    ## no moves left
    if len(legal_moves(board)) == 0:
        result = GameState.DRAW

    ## horizonal win
    for row in board:
        if row.count(player) == board_size:
            result = player_wins(player)
    
    ## vertical win
    for j in range(board_size):
        column = [board[i][j] for i in range(len(row))]
        if column.count(player) == board_size:
            result = player_wins(player)
    
    ## forward diagonal wins
    diag = [board[i][i] for i in range(board_size)]
    if diag.count(player) == board_size:
        result = player_wins(player)
    
    ## backward diagonal wins
    diag = [board[i][i] for i in reversed(range(board_size))]
    if diag.count(player) == board_size:
        result = player_wins(player)

    return result

def next_turn(player):
    return -player

player=1

game_state = GameState.IN_PROGRESS

while game_state == GameState.IN_PROGRESS:
    moves = legal_moves(board)
    next_move = moves[0]
    make_move(board,next_move,player)
    game_state = get_game_state(board,player)
    player = next_turn(player)
    print_board(board)

print("Game over",game_state)
