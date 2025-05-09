from pyamaze import maze,agent,COLOR


def bfs(m):
    start = (m.rows,m.cols)
    frontier = [start]
    explored = [start]
    bfs_path ={}

    while frontier:
        current_cell= frontier.pop(0)
        if current_cell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[current_cell][d]==True:
                if d=='E':
                    child_cell=(current_cell[0],current_cell[1]+1)
                elif d=='W':
                    child_cell=(current_cell[0],current_cell[1]-1)
                elif d=='N':
                    child_cell=(current_cell[0]-1,current_cell[1])
                elif d=='S':
                    child_cell=(current_cell[0]+1,current_cell[1])
                if child_cell in explored:
                    continue
                frontier.append(child_cell)
                explored.append(child_cell)
                bfs_path[child_cell]=current_cell
    
    
    
    fwd_path = {}
    goal = (1, 1)


    if goal in bfs_path:
        while goal != start:
            fwd_path[bfs_path[goal]] = goal 
            goal = bfs_path[goal]

    return fwd_path
    

   
                    

m= maze(20,20)
m.CreateMaze()
path=bfs(m)

a=agent(m,footprints=True)
m.tracePath({a:path})
m.run()