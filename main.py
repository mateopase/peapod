from kmk.keys import KC
from peapod import Peapod


keyboard = Peapod()

keyboard.keymap = [
    [
        KC.Q,    KC.W,    KC.E,    KC.R,   KC.T,   KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,
        KC.A,    KC.S,    KC.D,    KC.F,   KC.G,   KC.H,    KC.J,    KC.K,    KC.L,   KC.BSPC,
        KC.Z,    KC.X,    KC.C,    KC.V,   KC.SPC, KC.ENT,  KC.B,    KC.N,    KC.M,   KC.RSFT
    ],
]


if __name__ == '__main__':
    keyboard.go()

