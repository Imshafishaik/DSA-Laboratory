LAB-07                         Advanced Algorithms and Programming                             Team - 23
--------------------------------------------------------------------------------------------------------

Team Members :- Shaik Shafi & Anshul Reddy


-------------------------Exercise 1 done by shafi-------------------------

Logic & Approach: 

The goal is to efficiently manage 2D space by recursively subdividing it into four equal quadrants (a structure known as a Quadtree). This is used to identify "dense regions" where the number of points exceeds a specific threshold. 

Complexity Analysis Answers: 

 

1.If you have N points and split until size = 1x1, how many recursive calls? 

Ans: For a square of side S, the depth of the tree is log_2(S). Since each call creates 4 more, the total calls are approximately sum_{i=0} ^ {log_2 S} 4^i, which is O(S^2). Note that the number of points N affects the count_points check within each call, but the structure depends on the spatial dimensions. 
 
 
2.What happens if points are all clustered in one corner? 

Ans. The algorithm will still perform a full recursive split in that specific quadrant down to the min_size, while other empty quadrants might stop early if density isn't met, leading to an unbalanced tree. 



-------------------------Exercise 3 done by Shafi-------------------------

Logic & Approach 

This uses Midpoint Displacement. It creates natural-looking terrain by finding the middle of a line, moving it up or down by a random "roughness" factor, and repeating for the new segments 

 

Complexity Analysis Answers: 

1.For a 1024-pixel line with depth 10, how many midpoints are calculated?  

Ans: At each level i, we add 2^{i-1} points. For depth 10, the total midpoints are 2^{10} - 1 = 1,023. 

2.What happens if roughness = 0? If roughness = 2?  

Ans: If roughness = 0, the result is a perfectly straight line because no random offset is added. If roughness is high (e.g., 2), the terrain becomes extremely jagged and chaotic. 
 

