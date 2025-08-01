import os
from resource_path import resource_path


class Piece:

    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.texture_rect = texture_rect
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()

    def set_texture(self, size=80):
        try:
            self.texture = resource_path(
                f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')
            # Check if the file exists
            if not os.path.exists(self.texture):
                print(f"Warning: Texture file '{self.texture}' does not exist.")
        except Exception as e:
            print(f"Error setting texture for {self.color} {self.name}: {e}")
            # Set a default texture path even if there's an error
            self.texture = f'assets/images/imgs-{size}px/{self.color}_{self.name}.png'

    def add_move(self, move):
        self.moves.append(move)

    def clear_moves(self):
        self.moves = []


class Pawn(Piece):

    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        self.en_passant = False
        super().__init__('pawn', color, 1.0)


class Knight(Piece):

    def __init__(self, color):
        super().__init__('knight', color, 3.0)


class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop', color, 3.001)


class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook', color, 5.0)


class Queen(Piece):

    def __init__(self, color):
        super().__init__('queen', color, 9.0)


class King(Piece):

    def __init__(self, color):
        self.left_rook = None
        self.right_rook = None
        super().__init__('king', color, 10000.0)
