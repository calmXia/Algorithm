# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "calm.xia@gmail.com"


# =============================
# 1. 散列表 -- 元素为节点本身以及节点的邻居节点，以此来表示整张图
#      key -- 节点
#      value -- 邻居节点
# 思考：key-value 对的添加顺序重要吗？
# =============================
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

from collections import deque

search_queue = deque()  # 创建一个队列
search_queue += graph["you"]  # 将你的邻居都加入到这个搜索队列中
