#Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
#You may assume all four edges of the grid are all surrounded by water.



def numIslands(grid):
    if not grid  or len(grid)==0:
        return 0
    
    nr = len(grid)
    nc = len(grid[0])
    islands = 0
    
    def dfs(grid, i,j):
        print(grid)
        print("\n")
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) :
            print("1 False") 
            print(grid)
            print("\n")
            return
        if grid[i][j]!='1':
            print(" 2 False") 
            print(grid)
            print("\n")
            return
        
        grid[i][j] = 'vis'
        dfs(grid, i-1, j)
        dfs(grid, i, j-1)
        dfs(grid, i+1, j)
        dfs(grid, i, j+1)

        print("True") 
        print(grid)
        print("**********************************", i, j)
    
    for i in range(nr):
        for j in range(nc):
            if grid[i][j] == '1':
                islands +=1
                dfs(grid, i, j)
                
                
                
    print("islands") 

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

numIslands(grid)
