from random import randint, choice


class Ship:

    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [1] * self._length

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    @staticmethod
    def get_cells_coords(ship):
        if ship._tp == 1:
            coord_x = range(ship._x, ship._x + ship._length)
            coord_y = [ship._y] * ship._length
        else:
            coord_x = [ship._x] * ship._length
            coord_y = range(ship._y, ship._y + ship._length)
        return zip(coord_x, coord_y)

    @staticmethod
    def is_collide_one_cell(coord1, coord2):
        if abs(coord1[0] - coord2[0]) < 2 and abs(coord1[1] - coord2[1]) < 2:
            return True
        else:
            return False

    def is_collide(self, ship):
        for i in self.get_cells_coords(self):
            for j in ship.get_cells_coords(ship):
                if self.is_collide_one_cell(i, j):
                    return True
        return False

    def move(self, go=1):
        if self._tp == 1:
            self._x += go
        else:
            self._y += go

    def is_out_pole(self, size):
        if self._x > size or self._x + self._length > size or self._y > size or self._y + self._length > size or \
                self._x < 1 or self._y < 1:
            return True
        return False

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value


class GamePole:

    def __init__(self, size):
        self._size = size
        self._ships = []

    def init(self):
        self._ships.clear()
        self._ships = [Ship(4, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)), Ship(3, tp=randint(1, 2)),
                       Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)), Ship(2, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)), Ship(1, tp=randint(1, 2)),
                       Ship(1, tp=randint(1, 2))
                       ]
        for ship in self._ships:
            ship.set_start_coords(randint(1, 10), randint(1, 10))
            while any([ship.is_collide(i) for i in self._ships if i != ship]):
                ship.set_start_coords(randint(1, 10), randint(1, 10))

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            coords = ship.get_start_coords()
            go = choice([-1, 1])
            if ship._is_move:
                ship.move(go)
                if any([ship.is_collide(i) for i in self._ships if i != ship]) or ship.is_out_pole(self._size):
                    ship.move(-2 * go)
                    if any([ship.is_collide(i) for i in self._ships if i != ship]) or ship.is_out_pole(self._size):
                        ship.set_start_coords(*coords)

    def
