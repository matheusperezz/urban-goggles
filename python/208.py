from dataclasses import dataclass

@dataclass
class Tree:
    name: str
    qnt: int

trees = []
N, C = map(int, input().strip().split())
for _ in range(N):
    name, qnt = map(str, input().split(" "))
    qnt = int(qnt)
    trees.append(Tree(name=name, qnt=qnt))

sorted_trees = sorted(trees, key=lambda tree: tree.qnt, reverse=True)

sorted_trees = sorted_trees[:C]
for i in range(C):
    print(sorted_trees[i].name)
