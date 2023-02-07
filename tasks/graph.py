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
        rows: list[list[Node]] = [[]]
        row: list[list[Node]] = []
        rowA: list[Node] = []

        start: Node = self._root
        present: Node = self._root

        k: int = 1

        rowA.append(start)
        rows.append(rowA)

        for node in start.outbound:
            if node not in rows[1]:
                row.append(node)
        rows.append(row)
        row = []

        for node_row in rows[2]:
            for node in node_row.outbound:
                if node not in rows[1] and node not in rows[2]:
                    row.append(node)
        rows.append(row)
        row = []

        for node_row in rows[3]:
            for node in node_row.outbound:
                if node not in rows[1] and node not in rows[2] and node not in rows[3]:
                    row.append(node)
        rows.append(row)
        row = []

        print(rows)
        for node_row in rows:
            for node in node_row:
                path.append(node)


        print(path)
        return path
        raise NotImplementedError
