def reduce_alpha_on_color(color: tuple, reduce: int):
    value_reduced = color[3] - reduce
    if value_reduced < 0:
        value_reduced = 0
    return color[:3] + (value_reduced,) + color[4:]

def increase_alpha_on_color(color: tuple, increase: int):
    value_increased = color[3] + increase
    if value_increased > 255:
        value_increased = 255
    return color[:3] + (value_increased,) + color[4:]