'''
给定一张包含N个点、N-1条边的无向连通图，节点从1到N编号，每条边的长度均为1。
假设你从1号节点出发并打算遍历所有节点，那么总路程至少是多少？

输入描述：
第一行包含一个整数N，1≤N≤10^5。
接下来N-1行，每行包含两个整数X和Y，表示X号节点和Y号节点之间有一条边，1≤X，Y≤N。

输出描述：
输出总路程的最小值。

示例：
输入
4
1 2
1 3
3 4
输出
4
'''
from collections import defaultdict,deque

def function(N,lists):
    graph=lists
    visited=set([1])
    queue=deque()
    queue.append((1,0))
    max_depth=0
    while queue: #求图最大深度
        cur_node,depth=queue.popleft()
        max_depth=max(max_depth,depth)
        for child in graph[cur_node]:
            if child not in visited:
                visited.add(child)
                queue.append((child,depth+1))
    return 2*(N-1)-max_depth
        


if __name__ == "__main__":
    N=int(input())
    #N=int(N)
    graph=defaultdict(list)
    for _ in range(N-1):
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    print(function(N,graph))
