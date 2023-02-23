![IMG](https://miro.medium.com/v2/resize:fit:640/format:webp/1*KS6LQjfnwaG_vlN0BtBlDw.png)
# Depth-First-Search-Maze-Algorithm

1. Create LIFO stack of frontier and Explored Cells
2. Find child cell against all possible cells
3. If explored add to explored list
4. If not then append child to both eplored and frontier 
5. Repeat until target is reached OR frontier is empty
6. Rather than picking the next node arbitrarily, move prefferentially in order of WNSE from pyamaze map which is equivalent to Left-Up-Down-Right
