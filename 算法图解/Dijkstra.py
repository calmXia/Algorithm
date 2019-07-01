#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'calm.xia@gmail.com'

'''
狄克斯特拉算法（Dijkstra’s algorithm）-- 最快路径
包含4个步骤 
(1) （从起点开始）找出开销最低的节点
(2) 对于该节点的邻居，检查是否有前往它们的更短路径，如果有，就更新其开销。 -- 开销指的是从起点开始的花费。 
(3) 重复这个过程，直到对图中的每个节点都这样做了。-- 终点除外。 
(4) 计算最终路径。
'''

# ==================================================
# 1. 散列表 graph -- 表示整张图 
#   一级散列表 "key-value" 
#         --> "节点-邻居节点"
#   二级散列表 "key-value" -- 一级散列表中元素的 value 使用散列表构造 
#         --> "节点-（从父节点过来的）开销"
# ==================================================

graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
# graph["start"].keys()  # 获取 start 节点的所有邻居节点

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}  # 终点没有任何邻居

# ==================================================
# 2. 散列表 costs -- 存储每个节点的开销
#   节点的开销指的是从起点出发前往该节点的总开销。
#   对于还不知道的开销，将其设置为无穷大
#   注意：刚开始设置散列表的时候，只知道起点的邻居节点的开销，其他的节点都是未知的，设置为无穷大
# ==================================================

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# ==================================================
# 3. 散列表 parents -- 存储父节点
# ==================================================

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# ==================================================
# 4. 数组 processed -- 记录处理过的节点
#   对于同一个节点，不用处理多次
# ==================================================

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # 遍历所有的节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # 如果当前节点的开销更低且未处理过
            lowest_cost = cost  # 就将其视为开销最低的节点
            lowest_cost_node = node
    return lowest_cost_node
        
def main():
    node = find_lowest_cost_node(costs) # 在未处理的节点中找出开销最小的节点
    print("First lowest code node: ", node)

    while node is not None:             # while 循环在所有节点都被处理过后结束
        print("--------------")
        cost = costs[node]
        neighbors = graph[node]
        print("node ", node, ": cost ", cost, " neighbors ", neighbors)

        for n in neighbors.keys():      # 遍历当前节点的所有邻居
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:     # 如果经当前节点前往该邻居更近,
                costs[n] = new_cost     # 就更新该邻居的开销,
                parents[n] = node       # 同时将该邻居的父节点设置为当前节点
        processed.append(node)          # 将当前节点标记为处理过
        print("processed: ", processed)
        node = find_lowest_cost_node(costs) # 找出接下来要处理的节点, 并循环
    print()
    print("Done! Cost of 'fin' is : ", costs['fin'])
    print("'fin' <-- ", parents["fin"], " <-- ", parents[parents["fin"]] )


if __name__ == "__main__":
    main()
