from collections import deque

def rotate_clockwise(dx,dy):
    return dy, -dx

def rotate_counterclockwise(dx, dy):
    return -dy, dx

def rotate_180(dx, dy):
    return -dx, -dy

def bfs_minimum_moves(grid, start, destination, move_rule):
    M, N = len(grid), len(grid[0])
    directions = [
        move_rule,
        rotate_clockwise(*move_rule),
        rotate_counterclockwise(*move_rule),
        rotate_180(*move_rule)
    ]
    
    queue = deque([start])
    visited = set()
    visited.add(start)
    moves = 0

    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            
            if current == destination:
                return moves
            
            for direction in directions:
                next_x = current[0] + direction[0]
                next_y = current[1] + direction[1]
                
                if (0 <= next_x < M and 0 <= next_y < N and
                    (next_x, next_y) not in visited and grid[next_x][next_y] == 0):
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y))
        
        moves += 1  
    
    return -1  

M, N = map(int, input("Enter M and N: ").strip().split())
print("Enter the grid (0s and 1s):")
grid = [list(map(int, input().strip().split())) for _ in range(M)]
source = tuple(map(int, input("Enter source coordinates (row col): ").strip().split()))
destination = tuple(map(int, input("Enter destination coordinates (row col): ").strip().split()))
move_rule = tuple(map(int, input("Enter move rule (dx dy): ").strip().split()))

result = bfs_minimum_moves(grid, source, destination, move_rule)
print(result)
