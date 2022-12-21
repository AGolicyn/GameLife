import asyncio
from .schemas import GameOptions


class World:
    def __init__(self, options: GameOptions):
        self.row_num = options.shape.row_num
        self.column_num = options.shape.col_num
        self.cur_epoch_desk = [[0 for _ in range(self.column_num)]
                               for _ in range(self.row_num)]
        self.next_epoch_desk = [[0 for _ in range(self.column_num)]
                                for _ in range(self.row_num)]
        self.molecules = options.molecules
        self.interrupt = options.interrupt
        self.speed = options.speed
        self._set_start_values()

    def _set_start_values(self):
        """Set alive molecules on an empy desk"""
        for mol in self.molecules:
            self.cur_epoch_desk[mol.row][mol.col] = 1

    def refresh(self, options: GameOptions):
        """Reinstall the object with new data"""
        self.__init__(options)

    async def live_an_epoch(self):
        """Live one game cycle, update alive molecules locations"""
        alive_after_epoch = []
        for i, row in enumerate(self.cur_epoch_desk):
            for j, mol in enumerate(row):
                count = self._check_neighbours(i, j)
                if (mol and (count in (2, 3))) or (not mol and (count == 3)):
                    self.next_epoch_desk[i][j] = 1
                    alive_after_epoch.append(f'{i}-{j}')
                else:
                    self.next_epoch_desk[i][j] = 0

        self.cur_epoch_desk = self.next_epoch_desk

        self.next_epoch_desk = [[0 for _ in range(self.column_num)]
                                for _ in range(self.row_num)]
        await asyncio.sleep(self.speed)
        return alive_after_epoch

    def _check_neighbours(self, row, col) -> int:
        """Check the number of molecules around the current"""
        neighbour_counter = 0
        neighbour_counter += self._check_right_side(row, col)
        neighbour_counter += self._check_right_upside(row, col)
        neighbour_counter += self._check_upside(row, col)
        neighbour_counter += self._check_left_upside(row, col)
        neighbour_counter += self._check_left_side(row, col)
        neighbour_counter += self._check_left_downside(row, col)
        neighbour_counter += self._check_downside(row, col)
        neighbour_counter += self._check_right_downside(row, col)

        return neighbour_counter

    def _check_upside(self, row, col):
        if self.cur_epoch_desk[row - 1][col]:
            return 1
        return 0

    def _check_right_side(self, row, col):
        if col == self.column_num - 1:
            if self.cur_epoch_desk[row][0]:
                return 1

        elif self.cur_epoch_desk[row][col + 1]:
            return 1
        return 0

    def _check_right_upside(self, row, col):
        if col == self.column_num - 1:
            if row == 0 and self.cur_epoch_desk[self.row_num - 1][0]:
                return 1
            if self.cur_epoch_desk[row - 1][0]:
                return 1

        elif self.cur_epoch_desk[row - 1][col + 1]:
            return 1
        return 0

    def _check_right_downside(self, row, col):
        if row == self.row_num - 1:
            if col == self.column_num - 1:
                if self.cur_epoch_desk[0][0]:
                    return 1
            elif self.cur_epoch_desk[0][col + 1]:
                return 1
            return 0
        if col == self.column_num - 1:
            if self.cur_epoch_desk[row + 1][0]:
                return 1
            return 0
        if self.cur_epoch_desk[row + 1][col + 1]:
            return 1
        return 0

    def _check_left_side(self, row, col):
        if self.cur_epoch_desk[row][col - 1]:
            return 1
        return 0

    def _check_left_upside(self, row, col):
        if self.cur_epoch_desk[row - 1][col - 1]:
            return 1
        return 0

    def _check_left_downside(self, row, col):
        if col == 0:
            if row == self.row_num - 1:
                if self.cur_epoch_desk[0][col - 1]:
                    return 1
            elif self.cur_epoch_desk[row + 1][col - 1]:
                return 1
            return 0
        if row == self.row_num - 1:
            if self.cur_epoch_desk[0][col - 1]:
                return 1
        elif self.cur_epoch_desk[row + 1][col - 1]:
            return 1
        return 0

    def _check_downside(self, row, col):
        if row == self.row_num - 1:
            if self.cur_epoch_desk[0][col]:
                return 1
        elif self.cur_epoch_desk[row + 1][col]:
            return 1
        return 0

    def __repr__(self):
        return f'Поле размера: {self.column_num}x{self.row_num} ' \
               f'c живыми молекулами: {self.molecules}'
