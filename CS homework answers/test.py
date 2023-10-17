left = []2,5,-1,-1,-1,-1]


def traverse (pos)
    if left(pos) != -1:
        traverse (left(pos))
    if right(pos) != -1:
        traverse (right (pos))
    print(name(pos))

traverse(0)

