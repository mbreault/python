import chess
import chess.polyglot
board = chess.Board()

with chess.polyglot.open_reader("data/polyglot/bookfish.bin") as reader:
    for entry in reader.find_all(board):
        print(entry.move, entry.weight, entry.learn)

mov = chess.polyglot.MemoryMappedReader("data/polyglot/bookfish.bin").weighted_choice(board)
print(mov)