from collections import deque


def search(graph_data, start_key, end_key):
    """
    BFS 广度优先遍历 O(V + E)
    :param graph_data: 图数据
    :param start_key: 开始节点
    :param end_key: 目标节点
    :return: 是否可以从开始节点遍历到目的节点
    """
    search_queue = deque()
    search_queue += graph_data[start_key]
    searched = []
    while search_queue:
        name = search_queue.popleft()
        if name not in searched:
            if end_key == name:
                return True
            else:
                search_queue += graph_data[name]
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

