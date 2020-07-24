Get the Average of each level of a BST. 

 - traverse tree via BFS
 - get average at each level based on depth
 - root = depth 1
 - same in array type float
 
 return array of floats

 walls 

 - create a visited Matrix
 - iterate through the Matrix
 - run DFS if equal to -2 
 - turn visited[r][c] on
 - test all 4 options
 - turn visited[r][c] off

 - DFS
   - check if safe
   - check if current depth is smallest
   - run all dfs

 - is_safe
 	- row > 0 
 	- col > 0
 	- row <= len(M)
 	- col <= len(M[0])