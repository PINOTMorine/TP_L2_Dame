class Piece:
    def __init__(self, position, color):
        self.position=position
        self.color=color

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

    def atomic_moves(self,board):
        list=[]

        return list