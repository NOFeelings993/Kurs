import numpy as np

class Checker(object):
    def __init__(self, color):
        self.color = color


class Board(object):
    def __init__(self):
        self.board = np.array([[ int((i+j)%2==0) for j in range(8)] for i in range(8)])
