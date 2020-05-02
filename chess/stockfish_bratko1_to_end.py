#!/usr/bin/python

import chess
import chess.engine
import chess.pgn

position = "1k1r4/pp1b1R2/3q2pp/4p3/2B5/4Q3/PPP2B2/2K5 b - - 0 1"

engine = chess.engine.SimpleEngine.popen_uci("stockfish")

board = chess.Board(position)
game = chess.pgn.Game()
game.setup(board)
print(board)
move_history = []
while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(depth=30))
    board.push(result.move)
    move_history.append(result.move)
    print(result.move)
    print(board)

print(board.result())
print(board)
print(board.variation_san(board.move_stack))

engine.quit()
