# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = "calm.xia@gmail.com"

"""
Greedy Algorithm 贪婪算法：
    每步都选择局部最优解，最终得到的就是全局最优解

求解场景：
    假设办了个广播节目，要让特定几个州的听众都能收听到。为此，需要决定在哪些广播台播出。
    已知每个广播台都覆盖特定的区域，即覆盖可能不止一个州，不同广播台的覆盖区域可能重叠。
    问：如何找出覆盖所有州的最小广播台集合？
"""

# ==================================
# 1. 集合 -- 包含要覆盖的州
#    注：集合的特性是不能包含重复的元素
# ==================================
# 放在这里定义的话，下面main方法执行的时候回报 states_needed 引用未定义，暂不知为什么.
# states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])  # 传入的数组被转换为集合

# ==================================
# 2. 散列表 -- 可供选择的广播台清单
#    key   -- 广播台名称
#    value -- 广播台覆盖的州，用集合表示（你将看到这将简化工作!）
# ==================================
stations = {}
stations["kone"]   = set(["id", "nv", "ut"])
stations["ktwo"]   = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"]  = set(["nv", "ut"])
stations["kfive"]  = set(["ca", "az"])

# ==================================
# 3. 集合 -- 最终选择的广播台
# ==================================
final_stations = set()

def main():
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])  # 传入的数组被转换为集合
    
    while states_needed:  #  Greedy 1 : 待覆盖目标非空
        best_station = None     # 每轮选择的最佳广播台 -- 每步的局部最优解
        states_covered = set()  # 每轮选择的最佳广播台所覆盖的目标州集合（注意不是该广播台本身覆盖的所有州）
        #  Greedy 2 : 每轮剩余待处理覆盖材料的规模
        for station, states_for_station in stations.items():  # key 和 value 被分别赋值给了 station 和 states_for_station
            covered = states_needed & states_for_station  # 计算交集 -- 所选的广播台覆盖的目标州集合
            if len(covered) > len(states_covered):  #  Greedy 2.1 : 找出该轮覆盖材料的局部最优解
                best_station = station
                states_covered = covered
        print("round done: best_station: ", best_station, "--states_covered: ", states_covered)

        states_needed -= states_covered  #  Greedy 3 : 待覆盖目标收缩
        final_stations.add(best_station) #  Greedy 4 : 局部最优解收集
    
    print("final stations selected: ", final_stations)


if  __name__ =="__main__":
    main()
    
