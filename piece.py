import pygame

class Piece:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type
        self.image = self.load_image()

    def load_image(self):
        path = f'assets/images/pieces/{self.color}_{self.piece_type}.png'
        return pygame.transform.scale(pygame.image.load(path), (50, 50))

    def is_valid_move(self, start_pos, end_pos, board):
        is_valid = None
        if self.piece_type == 'pawn':
            is_valid = self.valid_pawn_move(start_pos, end_pos, board)

        elif self.piece_type == 'rook':
            is_valid = self.valid_rook_move(start_pos, end_pos, board)

        elif self.piece_type == 'knight':
            is_valid = self.valid_knight_move(start_pos, end_pos, board)

        elif self.piece_type == 'bishop':
            is_valid = self.valid_bishop_move(start_pos, end_pos, board)

        elif self.piece_type == 'queen':
            is_valid = self.valid_queen_move(start_pos, end_pos, board)

        elif self.piece_type == 'king':
            is_valid = self.valid_king_move(start_pos, end_pos, board)

        return is_valid

    def valid_pawn_move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        direction = 1 if self.color == 'white' else -1

        valid = False
        if start_col == end_col and start_row + direction == end_row and board[end_row][end_col] is None:
            valid = True

        if start_col == end_col and start_row + 2*direction == end_row and start_row == (1 if self.color == 'white' else 6) and board[end_row][end_col] is None:
            valid = True

        if abs(start_col - end_col) == 1 and start_row + direction == end_row and board[end_row][end_col] is not None and board[end_row][end_col].color != self.color:
            valid = True
        
        return valid

    def valid_rook_move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        valid = False
        if start_col == end_col:
            blocking_piece = False
            if start_row > end_row:
                for row in range(start_row-1, end_row, -1):
                    if board[row][end_col] is not None:
                        blocking_piece = True
            else:
                for row in range(start_row+1, end_row):
                    if board[row][end_col] is not None:
                        blocking_piece = True

            if not blocking_piece:
                if board[end_row][end_col] is None:
                    valid = True
                elif board[end_row][end_col].color != self.color:
                    valid = True

        elif start_row == end_row:
            blocking_piece = False
            if start_col > end_col:
                for col in range(start_col-1, end_col, -1):
                    if board[end_row][col] is not None:
                        blocking_piece = True
            else:
                for col in range(start_col+1, end_col):
                    if board[end_row][col] is not None:
                        blocking_piece = True

            if not blocking_piece:
                if board[end_row][end_col] is None:
                    valid = True
                elif board[end_row][end_col].color != self.color:
                    valid = True

        return valid