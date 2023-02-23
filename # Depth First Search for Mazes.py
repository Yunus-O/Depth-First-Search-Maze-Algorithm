# Depth First Search for Mazes

"""
    Create LIFO stack of frontier and Explored Cells
    Find child cell against all possible cells
    If explored add to explored list
    If not then append child to both eplored and frontier 
    Repeat until target is reached OR frontier is empty
    Rather than picking the next node arbitrarily, move prefferentially in order of WNSE from pyamaze map which is equivalent to Left-Up-Down-Right

"""

# importing pyamaze for randomly generated maze
from pyamaze import maze,agent, COLOR

# Create maze of size x-y
m=maze(20,20)

# Randomy create maze based on previous parameters
m.CreateMaze()

# Start at the last cell
# x = rows 
# y = columns 
start=(m.rows,m.cols)


# Create frontier / explored stacks
explored=[start]
frontier=[start]

# DFS Function:
def DFS(m):
    
    # Dictionary to visualize path of agent
    dfsPath= {}

    # While fontier is not empty
    while len(frontier)>0:

        # add current cell to frontier
        currentCell = frontier.pop()

        # If it is goal (1,1) (top left) stop
        if currentCell == (1,1):
            break
        
        # For all possible directions 
        # Listed in inverse order bc using LIFO stack
        for d in 'ESNW':
            # Check if cell exists in each direction  
            if m.maze_map[currentCell][d]==True:
                # Diffrent condition for moving in each direction 
                if d=='E':
                    # add one to y value: moving to the right *y = columns*
                    childCell = (currentCell[0],currentCell[1]+1)
                elif d=="S":
                    childCell = (currentCell[0]+1,currentCell[1])
                elif d=="N":
                    # Larger the number the further down and to the right we are
                    childCell = (currentCell[0]-1,currentCell[1])
                elif d=="W":
                    # Larger the number the further down and to the right we are
                    childCell = (currentCell[0],currentCell[1]-1)
                # if explored already do nothing
                if childCell in explored:
                    continue
                
                # Add chilcell to fronteir and explored
                explored.append(childCell)
                frontier.append(childCell)

                # Assign child as key with current cell as val, creating path from goal to start rather than start to goal 
                # Reason: cannot have duplicate key (current cell) in dictionary
                dfsPath[childCell]=currentCell

    # Dictionary for reverse of dfs path 
    fwdPath ={}

    # Starting from goal cell (1,1)
    cell = (1,1)

    # Until "start" cell 
    # Swap keys and values of the path
    while cell != start:
        fwdPath[dfsPath[cell]]=cell
        cell = dfsPath[cell]
    return fwdPath



# Set output equal to path
path = DFS(m)

# See agent (which defualts to start of the maze (last row,column))
a = agent(m,footprints= True,)
b = agent(m,footprints=True,color=COLOR.yellow,filled=True)

# See path of agent from a : output of DFS()
m.tracePath({b:explored},showMarked=True)
m.tracePath({a:path}, showMarked= True,delay=90)

m.markCells
m.run()
            

