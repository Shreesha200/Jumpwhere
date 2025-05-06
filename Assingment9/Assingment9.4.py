def shift_coordinates(coords):
    min_x = min(x for x, y in coords)
    min_y = min(y for x, y in coords)
    
    shift_x = -min_x if min_x < 0 else 0
    shift_y = -min_y if min_y < 0 else 0

    new_coords = [(x + shift_x, y + shift_y) for x, y in coords]
    return new_coords

# Example input
input_coords = [(1, -2), (-2, 4), (-1, -1), (-8, -3), (0, 4), (10, -3)]
output_coords = shift_coordinates(input_coords)

print("Output:", output_coords)
