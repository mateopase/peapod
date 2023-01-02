import board 

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation


class Peapod(KMKKeyboard):
    col_pins = (
        board.D2, 
        board.D1,
        board.D0,
        board.D3,
        board.D4
    )

    row_pins = (
        board.D9,
        board.D10,
        board.D8,
        board.D7,
        board.D5,
        board.D6
    )

    diode_orientation = DiodeOrientation.COL2ROW
