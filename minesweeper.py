import random

class Board:
    def __init__(self, width=10, height=10, mine_count=10, flag_count=10):
        self.width = width
        self.height = height
        self.mine_count = mine_count
        self.flag_count = flag_count
        self.board = [[Tile() for x in range(self.width)] for y in range(self.height)]

    def __str__(self):
        return '\n'.join([''.join([str(tile) for tile in row]) for row in self.board])

class Tile:
    def __init__(self, has_mine=False, has_flag=False, is_revealed=False, adjacent_tiles=[]):
        self.has_mine = has_mine
        self.has_flag = has_flag
        self.is_revealed = is_revealed
        self.adjacent_tiles = adjacent_tiles

    def adjacent_mines(self):
        return sum(1 if tile.has_mine else 0 for tile in self.adjacent_tiles)

    def adjacent_revealed(self):
        return sum(1 if tile.is_revealed else 0 for tile in self.adjacent_tiles) > 0

    def __str__(self):
        state = 'X'
        if self.is_revealed:
            state = 'O'
        if self.has_flag:
            state = 'F'
        
        return state  

def main():
    board = Board()
    print(board)

if __name__ == "__main__":
    main()