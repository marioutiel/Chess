import pygame
from board import Board

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption('Chess')
        self.board = Board()
        self.selected_piece = None
        self.selected_pos = None
        self.turn = 'white'

    def draw_board(self):
        colors = [pygame.Color(238, 238, 210), pygame.Color(118, 150, 86)]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                pygame.draw.rect(self.screen, color, pygame.Rect(col*50, row*50, 50, 50))

                piece = self.board.board[row][col]
                if piece:
                    self.screen.blit(piece.image, (col*50, row*50))

    def handle_click(self, pos):
        row, col = pos[1] // 50, pos[0] // 50
        if self.selected_piece:
            if self.selected_piece.color == self.turn and self.board.move_piece(self.selected_pos, (row, col)):
                self.turn = 'black' if self.turn == 'white' else 'white'
            self.selected_piece = None
            self.selected_pos = None
        else:
            self.selected_piece = self.board.board[row][col]
            self.selected_pos = (row, col)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(pygame.mouse.get_pos())

            self.draw_board()
            pygame.display.flip()
        pygame.quit()