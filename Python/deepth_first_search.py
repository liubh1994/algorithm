from collections import deque


def search(graph_date, start_key, end_key):
    """
    深度优先遍历 O(v + e)
    :param graph_date: 待遍历图
    :param start_key: 开始节点
    :param end_key: 目标节点
    :return: 是否可以从开始节点到达目标节点
    """
    search_queue = deque()
    search_queue += graph_date[start_key]
    searched = []
    while search_queue:
        name = search_queue.pop()
        if name not in searched:
            if name == end_key:
                return True
            else:
                search_queue += graph_date[name]
                searched.append(name)
    return False


graph = {}
graph['Ann'] = ['Tom', 'Bob', 'Lee']
graph['Tom'] = ['Bob', "Jone"]
graph['Bob'] = ['Less', 'Gay']
graph['Lee'] = ['Gay', 'Hello']
graph['Hello'] = ['World']
graph['Jone'] = []
graph['Less'] = []
graph['Gay'] = []
graph['World'] = []

print(search(graph, 'Ann', 'Hello'))
print(search(graph, 'Ann', 'World'))
print(search(graph, 'Ann', 'HDU'))