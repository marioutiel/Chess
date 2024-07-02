from piece import Piece

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        for col in range(8):
            self.place_piece(Piece('white', 'pawn'), 1, col)
            self.place_piece(Piece('black', 'pawn'), 6, col)

        major_pieces = {'rook': [0,7], 'knight': [1,6], 'bishop': [2,5]}
        for major_piece in major_pieces:
            self.place_piece(Piece('white', major_piece), 0, major_pieces[major_piece][0])
            self.place_piece(Piece('black', major_piece), 7, major_pieces[major_piece][0])
            self.place_piece(Piece('white', major_piece), 0, major_pieces[major_piece][1])
            self.place_piece(Piece('black', major_piece), 7, major_pieces[major_piece][1])

        king_queens = {'king': 3, 'queen': 4}
        for king_queen in king_queens:
            self.place_piece(Piece('white', king_queen), 0, king_queens[king_queen])
            self.place_piece(Piece('black', king_queen), 7, king_queens[king_queen])

    def place_piece(self, piece, row, col):
        self.board[row][col] = piece

    def move_piece(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        piece = self.board[start_row][start_col]
        if piece and piece.is_valid_move(start_pos, end_pos, self.board):
            self.board[end_row][end_col] = piece
            self.board[start_row][start_col] = None

    def print_board(self):
        for row in self.board:
            print(row)