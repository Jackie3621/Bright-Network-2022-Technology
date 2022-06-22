#!/usr/bin/env python
# coding: utf-8

# In[1]:


def createMaze(barriers):
    maze = [[0 for i in range(10)] for i in range(10)]
    maze[0][0] = 'S'
    maze[9][9] = 'E'
    for x in barriers:
        maze[tuple(reversed(x))[0]][tuple(reversed(x))[1]] = 1
    return maze

coords = [(9,7),(8,7),(6,7),(6,8)] # barriers from phase 1 

grid1 = createMaze(coords)
#print(grid1)


# In[2]:


# visual plot of the grid
import numpy as np
maze = np.zeros([10,10])

for x in coords:
    maze[x[1]][x[0]] = 1 # barriers indicated by 1
    
print(maze)


# In[3]:


# shortest path function
import collections

def solveMazeWithPath(maze):
    R, C = len(maze), len(maze[0])

    start = (0, 0)
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'S':
                start = (r, c)

    queue = collections.deque()
    queue.appendleft((start[0], start[1], 0, [start[0] * C + start[1]]))
    directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,-1],[-1,1]]
    visited = [[False] * C for _ in range(R)]

    while len(queue) != 0:
        coord = queue.pop()
        visited[coord[0]][coord[1]] = True

        if maze[coord[0]][coord[1]] == "E":
            return coord[2], [(i%C, i//C) for i in coord[3]] 

        for dir in directions:
            nr, nc = coord[0] + dir[0], coord[1] + dir[1]
            if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == 1 or visited[nr][nc]): continue
            queue.appendleft((nr, nc, coord[2] + 1, coord[3] + [nr * C + nc]))
    return 'unable to reach delivery point'


# In[4]:


# phase 1
print('Path =',solveMazeWithPath(grid1)[1])
print('Number of steps =', solveMazeWithPath(grid1)[0])


# In[5]:


# phase 2
# creating the obstacles
import numpy.random as nrnd

coords = [(9,7),(8,7),(6,7),(6,8)] # barriers from phase 1

for k in range (20):
    (x,y) = (nrnd.randint(0,9),nrnd.randint(0,9))
    
    while (x,y) == (0,0) or (x,y) == (9,9) or (x,y)  in coords:
        (x,y) = (nrnd.randint(0,9),nrnd.randint(0,9))
        
    coords.append((x,y))

#obstacles including the ones from phase 1
print(coords)


# In[6]:


grid2 = createMaze(coords)

maze = np.zeros([10,10])

for x in coords:
    maze[x[1]][x[0]] = 1 # barriers indicated by 1
    
print(maze)

# path and no. of steps
print('Path =',solveMazeWithPath(grid2)[1])
print('Number of steps =', solveMazeWithPath(grid2)[0])


# In[7]:


# test edge case
maze = np.zeros([10,10])

for x in [(8,8),(8,9),(9,8)]:
    maze[x[1]][x[0]] = 1 # barriers indicated by 1
    
print(maze)

print(solveMazeWithPath(createMaze([(8,8),(8,9),(9,8)])))

