from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        path: list[Node] = []
        start: Node = self._root
        present: Node = self._root
        other: Node = self._root
        path.append(start)
        k: int = 0
        for i in start.outbound:
            present = i
            if present not in path:
                path.append(present)
            for j in present.outbound:
                if j not in path:
                    path.append(j)
                    while j.outbound:
                        if k < len(j.outbound):
                            other = j.outbound[k]
                            k += 1
                            if other not in path:
                                path.append(other)
                            else:
                                break
                        else:
                            k = 0
                            break
        return path
        raise NotImplementedError


    def bfs(self) -> list[Node]:
        path: list[Node] = []
        start: Node = self._root
        present: Node = self._root
        other: Node = self._root
        path.append(start)
        k: int = 0
        for i in start.outbound:
            present = i
            if present not in path:
                path.append(present)
            for j in present.outbound:
                if j not in path:
                    path.append(j)
                    while j.outbound:
                        if k < len(j.outbound):
                            other = j.outbound[k]
                            k += 1
                            if other not in path:
                                path.append(other)
                            else:
                                break
                        else:
                            k = 0
                            break

        print(path)
        return path
        raise NotImplementedError


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')
k = Node('k')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
a.point_to(e)
e.point_to(f)
e.point_to(g)
f.point_to(i)
f.point_to(h)
g.point_to(k)
g = Graph(a)

g.bfs()

