
import networkx
from sys import platform as sys_pf
if sys_pf == 'darwin':
 import matplotlib
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.pyplot import show



# graph = {
#     'A' :'B B B C',
#     'B' : 'A C',
#     'C' : 'A B D E',
#     'D' : 'C',
#     'E' : 'C F',
#     'F' : 'E'
# }
# for k in graph:
#     graph[k] = set(graph[k].split())
#
# print(graph)
# Graph = networkx.Graph(graph)
# networkx.draw(Graph, with_labels=True)
# # show()
# seen = set()
# need_visited = ['A']
# while need_visited:
#     node = need_visited.pop(0)
#     if node in seen:
#         print('{} has been seen'.format(node))
#         continue
#     print('I am looking at :{}'.format(node))
#     need_visited +=graph[node]
#     seen.add(node)

# graph_long = {
#     '1': '2 7',
#     '2': '3',
#     '3': '4',
#     '4': '5',
#     '5': '6 10',
#     '7': '8',
#     '6': '5',
#     '8': '9',
#     '9': '10',
#     '10': '5 11',
#     '11': '12',
#     '12': '11',
# }
# for n in graph_long:
#     graph_long[n] = graph_long[n].split()
# Graph = networkx.Graph(graph_long)
# networkx.draw(Graph, with_labels=True)
# show()
#
# def treat_new_discover_more_important(new_discoveried,need_visited):
#     return new_discoveried + need_visited
# def treat_already_discoveried_more_important(new_discoveried,need_visited):
#     return need_visited + new_discoveried
#
#
# def search(gragh,concat_func):
#     seen = set()
#     need_visted = ['1']
#
#     while need_visted:
#         node = need_visted.pop(0)
#         if node in seen:
#             print('{} has been seen'.format(node))
#             continue
#         print('i am looking at :{}'.format(node))
#         seen.add(node)
#         new_discoverd = gragh[node]
#         need_visted = concat_func(new_discoverd,need_visted)



BJ = 'Beijing'
SZ = 'Shenzhen'
GZ = 'Guangzhou'
WH = 'Wuhan'
HLG = 'Heilongjiang'
NY = 'New York City'
CM = 'Chiangmai'
SG = 'Singapore'
air_route = {
    BJ : {SZ, GZ, WH, HLG, NY},
    GZ : {WH, BJ, CM, SG},
    SZ : {BJ, SG},
    WH : {BJ, GZ},
    HLG : {BJ},
    CM : {GZ},
    NY : {BJ}
}

Graph = networkx.Graph(air_route)
networkx.draw(Graph, with_labels=True)
show()

def search_destination(graph,start,destination):
    pathes = [[start]]
    seen = set()
    chosen_pathes = []
    while pathes:
        path = pathes.pop(0)
        print('++++++++++++')
        print('path  ',path)
        frontier = path[-1]
        print('frontier',frontier)
        print('%%%%%%%%%')
        if frontier in seen:continue

        for city in graph[frontier]:
            if city in path:continue
            new_path = path + [city]
            pathes.append(new_path)
            if city == destination:return new_path

        seen.add(frontier)
    return chosen_pathes

def draw_route(cities):
    return ' ----> '.join(cities)


if __name__ == '__main__':
    draw_route(search_destination(air_route, SZ, CM))










