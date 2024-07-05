import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Function to visualize the room with tiles and output the dimensions of all tiles
def visualize_room(room_length, room_width, tile_length, tile_width, points, point_labels, offset_x=0, offset_y=0):
    fig, ax = plt.subplots()
    ax.set_xlim(0, room_length)
    ax.set_ylim(0, room_width)

    # Draw the room
    room = Rectangle((0, 0), room_length, room_width, edgecolor='black', facecolor='none')
    ax.add_patch(room)

    # Draw the tiles
    y = -offset_y
    while y < room_width:
        x = -offset_x
        while x < room_length:
            tile_x = x + offset_x if x == -offset_x else x
            tile_y = y + offset_y if y == -offset_y else y

            # Adjust tile length and width for tiles against the opposite walls
            tile_length_adjusted = tile_length if x + tile_length <= room_length else room_length - tile_x
            tile_width_adjusted = tile_width if y + tile_width <= room_width else room_width - tile_y

            tile = Rectangle((tile_x, tile_y), tile_length_adjusted, tile_width_adjusted, edgecolor='blue', facecolor='lightblue')
            ax.add_patch(tile)

            # Output the dimensions of the tile
            print(f"Tile at ({tile_x}, {tile_y}): Length = {tile_length_adjusted}, Width = {tile_width_adjusted}")

            # Annotate the first tile with its dimensions
            if x == -offset_x and y == -offset_y:
                plt.text(tile_x + tile_length_adjusted / 2, tile_y + tile_width_adjusted / 2, f"{tile_length_adjusted} x {tile_width_adjusted}",
                         color='red', fontsize=6, ha='center', va='center')

            # Annotate and output the dimensions of the tiles against the opposite walls
            if tile_x + tile_length_adjusted >= room_length:
                print(f"Tile against right wall at ({tile_x}, {tile_y}): Length = {tile_length_adjusted}, Width = {tile_width_adjusted}")
                plt.text(tile_x + tile_length_adjusted / 2, tile_y + tile_width_adjusted / 2, f"{tile_length_adjusted} x {tile_width_adjusted}",
                         color='green', fontsize=6, ha='center', va='center')

            if tile_y + tile_width_adjusted >= room_width:
                print(f"Tile against bottom wall at ({tile_x}, {tile_y}): Length = {tile_length_adjusted}, Width = {tile_width_adjusted}")
                plt.text(tile_x + tile_length_adjusted / 2, tile_y + tile_width_adjusted / 2, f"{tile_length_adjusted} x {tile_width_adjusted}",
                         color='blue', fontsize=6, ha='center', va='center')

            x += tile_length
        y += tile_width

    # Plot the points and their labels
    for point, label in zip(points, point_labels):
        plt.plot(point[0], point[1], 'ro')  # Mark the points with red circles
        plt.text(point[0], point[1], label, color='black', fontsize=8, ha='right', va='bottom')

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Function to check if the grout lines intersect with any of the specified points
def grout_lines_intersect(tile_length, tile_width, points, offset_x=0, offset_y=0):
    for point in points:
        if ((point[0] - offset_x) % tile_length == 0 or (point[1] - offset_y) % tile_width == 0):
            return True
    return False

# Function to find optimal offsets to avoid grout lines intersecting with points
def find_optimal_offsets(tile_length, tile_width, points):
    for offset_x in range(tile_length):
        for offset_y in range(tile_width):
            if not grout_lines_intersect(tile_length, tile_width, points, offset_x, offset_y):
                return offset_x, offset_y
    return 0, 0  # Default to no offset if no optimal offset found

# Hardcoded room dimensions (in inches)
room_length = 144  # Example room length in inches
room_width = 150.5 # Example room width in inches

# Hardcoded tile dimensions (in inches)
tile_length = 24  # Example tile length in inches
tile_width = 12  # Example tile width in inches

# Hardcoded points (in inches)
points = [
    (49.5, room_width),#shower
    (49.5, room_width - 38), #shower corner
    (room_length, room_width - 31.5), #entry door wall
    (room_length, room_width - 91),  #door toilet
    (room_length-72, 54), #door toilet
    (114,0), # end of wall toilet
    (0,19) # vanity
]

# Labels for the points
point_labels = [
    "Shower",
    "Shower Corner",
    "Entry Door Wall",
    "Door Toilet",
    "Door Toilet",
    "End of Wall Toilet",
    "Vanity"
]

# Hardcoded offsets for the first row and first column
offset_x = 12
offset_y = 1

# Visualize the room with the tiles and output the dimensions of all tiles
visualize_room(room_length, room_width, tile_length, tile_width, points, point_labels, offset_x, offset_y)
