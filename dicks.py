from loads.images import *

Dires = {
    "up": (0, (-1, 0)),
    "left": (90, (0, -1)),
    "down": (180, (1, 0)),
    "right": (270, (0, 1))
}

Antonims = {
    "up": "down",
    "down": "up",
    "left": "right",
    "right": "left"
}

digits = {
    "0": Zero,
    "1": One,
    "2": Two,
    "3": Three,
    "4": Four,
    "5": Five,
    "6": Six,
    "7": Seven,
    "8": Eight,
    "9": Nine
}

idk = {
    ((1, 0), "up"): "down",
    ((0, 1), "up"): "right",

    ((0, 1), "left"): "right",
    ((-1, 0), "left"): "up",

    ((-1, 0), "down"): "up",
    ((0, -1), "down"): "left",

    ((0, -1), "right"): "left",
    ((1, 0), "right"): "down"
}