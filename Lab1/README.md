Limiting combination group size to 6 I got:
  N = 5, best solution: (0, 9, 15), elements: 5, visited nodes: 162 -> optimal because number of elements = N
  N = 10, best solution: (2, 34, 38), elements: 10, visited nodes: 3269 -> as above
  N = 20, best solution: (0, 11, 18, 19, 30), elements: 23, visited nodes: 330616 -> potentially suboptimal because 23 > N 

Using group size = 5 I got:
  N = 5, best solution: (0, 9, 15), elements: 5, visited nodes: 162
  N = 10, best solution: (2, 34, 38), elements: 10, visited nodes: 3269
  N = 20, best solution: (7, 13, 16, 18), elements: 24, visited nodes: 52360 -> requires 1/6 computational time at the cost of a 24 elements set rather than 23
  
Using group size = 7 I got:
  N = 5, best solution: (0, 9, 15), elements: 5, visited nodes: 162
  N = 10, best solution: (2, 34, 38), elements: 10, visited nodes: 3269
  N = 20, best solution: (0, 11, 18, 19, 30), elements: 23, visited nodes: 1675520 -> no improvements in respect to group size = 6 but 5 times slower
  
Using group size = 8 I got:
  N = 5, best solution: (0, 9, 15), elements: 5, visited nodes: 162
  N = 10, best solution: (2, 34, 38), elements: 10, visited nodes: 3269
  N = 20, best solution: (0, 11, 18, 19, 30), elements: 23, visited nodes: 7055136 -> still no improvements but even slower!
  
Using group size = 9 I got:
  N = 5, best solution: (0, 9, 15), elements: 5, visited nodes: 162
  N = 10, best solution: (2, 34, 38), elements: 10, visited nodes: 3269
  N = 20, best solution: (0, 11, 18, 19, 30), elements: 23, visited nodes: 25211340 -> no improvements but even slower!
 
Using group size = 4 I got:
  N = 5, best solution: (0, 9, 15), elements: 5, visited nodes: 162
  N = 10, best solution: (2, 34, 38), elements: 10, visited nodes: 3269
  N = 20, best solution: None, elements: 34, visited nodes: 5984 -> no solution found
  N = 100, best solution: None, elements: 427, visited nodes: 12884725 -> no solution found
 
Conclusions:
  Grouping from 5 to 9 the problem is doable for N << 100. With N = 5, 10 I got optimal results (even for 4-grouping) because the number of elements is equal to the number of integers needed for completing the set without duplicates.
  For N = 20 a 5-grouping produces a slighly less optimal solution because set size is 24 but with 6,7,8,9 grouping it is 23. 
  I'd prefer performing a 6-grouping because it is a good trade-off between results and computational time.
  For N >= 100 computational time to find a solution is just eternal.
