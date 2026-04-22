LAB-08                         Advanced Algorithms and Programming                             Team - 23
--------------------------------------------------------------------------------------------------------

Team Members :- Shaik Shafi & Anshul Reddy


-------------------------Exercise 1 done by shafi-------------------------

Logic & Approach: 

A BST organises users by user_id as the key. Every node's left subtree contains users with smaller IDs, right subtree contains larger IDs. This gives O(log n) average search and insert. 

For friend-of-friend suggestions: find the user, iterate their friends list, for each friend fetch their friends from the BST, collect all users who are not already direct friends and not the user themselves, count how many mutual friends each candidate has, return the top k by count.


Complexity Analysis Answers: 

1.If you have N points and split until size = 1x1, how many recursive calls? 
Ans: For a square of side S, the depth of the tree is log_2(S). Since each call creates 4 more, the total calls are approximately sum_{i=0} ^ {log_2 S} 4^i, which is O(S^2). Note that the number of points N affects the count_points check within each call, but the structure depends on the spatial dimensions. 
 
 
2.What happens if points are all clustered in one corner? 
Ans. The algorithm will still perform a full recursive split in that specific quadrant down to the min_size, while other empty quadrants might stop early if density isn't met, leading to an unbalanced tree. 
 