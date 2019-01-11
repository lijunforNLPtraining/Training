
#DFS,deep first serach
def dfs(graph,concat_func):
    seen = set()
    need_visited = ['A']
    while need_visited:
        node = need_visited.pop(0)
        if node in seen:continue
        seen.add(node)
        new_discoveried = graph[node]
        need_visited = concat_func(new_discoveried,need_visited)



def treat_new_discover_more_important(new_discoveried,need_visited):
    return  new_discoveried + need_visited

def treat_already_more_important(new_discoveried,need_visited):
    return  need_visited + new_discoveried

#BFS ，breadth first search
def bfs(graph):
    seen = set()
    need_visted = ['A']
    while need_visted:
        node = need_visted.pop(0)
        if node in seen:continue
        need_visted += graph[node]
        seen.add(node)


def search_destination(graph,start,destination):
    pathes = [[start]]
    seen = set()
    choosen_path = []
    while pathes:
        path = pathes.pop(0)
        frontier = path[-1]
        if frontier in seen:continue
        for city in graph[frontier]:
            new_path = path + [city]
            pathes.append(new_path)
            if city == destination:
                return  new_path
        seen.add(frontier)
    return choosen_path










