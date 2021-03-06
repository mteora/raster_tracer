import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def get_neighbors(size_i, size_j, ij):
    """ returns possible neighbors of a numpy cell """
    i,j = ij
    neighbors = set()
    if i>0:
        neighbors.add((i-1, j))
    if j>0:
        neighbors.add((i, j-1))
    if i<size_i-1:
        neighbors.add((i+1, j))
    if j<size_j-1:
        neighbors.add((i, j+1))
    return neighbors

def get_cost(array, current, next):
    return array[next]



def find_path(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    size_i, size_j = graph.shape
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in get_neighbors(size_i, size_j, current):
            new_cost = cost_so_far[current] + get_cost(graph, current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    
    path = reconstruct_path(came_from, start, goal)
    return path

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse() # optional
    return path
