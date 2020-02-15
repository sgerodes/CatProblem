BOXES_COUNT = 5
BOXES = frozenset(range(1, BOXES_COUNT+1))
MAX_PATH_LENGTH = 7

class CatError(Exception):
    def __init__(self, message):
        self.message = message


class Node:
    def __init__(self, possible_cat_positions, day=0):
        self.positions = frozenset(possible_cat_positions)
        self.day = day
        self.children = dict()

    def add_child(self, box_opened, child):
        self.children[box_opened] = child


root = Node(BOXES)
nodes_dict = dict()


def solve(node, path=""):
    positions = node.positions
    if len(positions) == 1:
        print(path+str(set(positions)))
        return

    if len(positions) < 1:
        raise CatError("positions less than 1")

    for opening_box in BOXES:
        positions_after_open = positions.difference({opening_box})
        after_night_positions = move_cat(positions_after_open)
        # print(positions, opening_box, positions_after_open, after_night_positions)
        if after_night_positions in nodes_dict.keys():
            child = nodes_dict.get(after_night_positions)
        else:
            child = Node(after_night_positions, node.day + 1)
            nodes_dict[after_night_positions] = child
        node.add_child(opening_box, child)
        #if len(path) > MAX_PATH_LENGTH-2:
        if  child.day < node.day+1:
            continue
        else:
            child.day = node.day+1
            solve(child, path+str(opening_box))


def move_cat(positions):
    pos = set()
    for p in positions:
        if p > 1:
            pos.add(p-1)
        if p < 5:
            pos.add(p+1)
    return frozenset(pos)


nodes_dict[BOXES] = root
solve(root)