class Node:
    def __init__(self, connection, key) -> None:
        self.key = key
        self.connected = []
        if connection:
            self.connected.append(connection)

    def addConnection(self, connection):
        self.connected.append(connection)
        if self not in connection.getConnected():
            connection.connected.append(self)

    def getConnected(self):
        return self.connected

    def findNode(self, key, seen=None):
        if not seen:
            seen = []
        if self.key == key:
            return self
        seen.append(self.key)
        for connection in self.connected:
            if connection.key not in seen:
                node = connection.findNode(key, seen)
                if node:
                    return node

    def getKey(self):
        return self.key

    __repr__ = getKey


def main():
    with open('input.txt') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    root = Node(None, 'start')
    unConnected = []

    for line in lines:
        s, e = line.split('-')
        start = root.findNode(s)
        end = root.findNode(e)
        if not start:
            for t in unConnected:
                start = t.findNode(s)
                if start:
                    break
            if not start:
                start = Node(None, s)
                unConnected.append(start)
        if not end:
            for t in unConnected:
                end = t.findNode(e)
                if end:
                    break
            if not end:
                end = Node(start, e)
        start.addConnection(end)

    paths = findPathsSingleSmall(root)
    paths = len(paths)
    print('Single small cave {}'.format(paths))

    double = findPathsDoubleSmall(root)
    double = len(double)
    print('Double small cave {}'.format(double))

def findPathsDoubleSmall(node, path=None, seen=False):
    if not path:
        path = []
    branchPaths = []
    if node.getKey().islower() and node in path and (seen or node.getKey() == 'start' or node.getKey() == 'end'):
        return []
    elif node.getKey().islower() and node in path and node.getKey() != 'start' and node.getKey() != 'end':
        seen = True
    path.append(node)
    if node.getKey() == 'end':
        branchPaths.append(path)
    else:
        for node in node.getConnected():
            branchPaths.extend(findPathsDoubleSmall(node, path[:], seen))
    return branchPaths

def findPathsSingleSmall(node, path=None):
    if not path:
        path = []
    branchPaths = []
    if node.getKey().islower() and node in path:
        return []
    path.append(node)
    if node.getKey() == 'end':
        branchPaths.append(path)
    for node in node.getConnected():
        branchPaths.extend(findPathsSingleSmall(node, path[:]))
    return branchPaths

if __name__ == '__main__':
    main()