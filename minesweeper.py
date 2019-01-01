import random

class Board:
    def __init__(self, width=10, height=10, mine_count=10, flag_count=10):
        self.width = width
        self.height = height
        self.mine_count = mine_count
        self.flag_count = flag_count
        self.board = [[Tile() for x in range(self.width)] for y in range(self.height)]

        for i, row in enumerate(self.board):
            for j, tile in enumerate(row):
                tile.adjacent_tiles = [self.board[x][y] 
                                       for x in range(j - 1, j + 2) for y in range(i - 1, i + 2) 
                                       if 0 <= x < self.width and 0 <= y < self.height 
                                       and (x, y) != (j, i)]

        mine_locations = []
        while len(mine_locations) < mine_count:
            mine_x, mine_y = random.randint(0, self.width - 1), random.randint(0, self.height - 1)
            if (mine_x, mine_y) not in mine_locations:
                mine_locations.append((mine_x, mine_y))
                self.board[mine_x][mine_y].has_mine = True

    def show_board(self):
        for row in self.board:
            print('')
            for tile in row:
                if tile.has_mine:
                    print('M', end='')
                else:
                    print('X', end='')

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
    board.show_board()

if __name__ == "__main__":
    main()