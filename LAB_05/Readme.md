LAB-05                         Advanced Algorithms and Programming                             Team - 23
--------------------------------------------------------------------------------------------------------

Team Members :- Shaik Shafi & Anshul Reddy

-------------------------Exercise 2 done by shafi-------------------------

Logic Explanation:

in_order_collect:
The function visits nodes in the order: left subtree, current node, then right subtree. It collects category names in this order, which helps display them in a sorted or structured way.

in_order_find_kth:
The function finds the k-th node in in-order traversal. It keeps a counter while traversing and returns the node when the counter matches k.

pre_order_export:
The function prints the current category first, then recursively prints the left and right subcategories. It adds indentation based on the level to visually show the hierarchy structure.

pre_order_copy:
The function creates a duplicate of the tree. It copies the current node and recursively copies the left and right subtrees to build a new identical tree.

pre_order_serialize:
The function converts the tree into a string representation. It processes the current node first and then appends serialized results of left and right subtrees.

post_order_total_posts:
The function calculates total posts by first collecting values from all subcategories. It recursively sums posts from left and right subtrees, then adds the current node’s posts at the end.

post_order_collect_leaves:
The function collects all leaf nodes. It first checks children recursively, and when it finds a node without children, it adds it to the result.

find_most_popular_category:
The function finds the category with the highest number of posts. It compares the current node with the best results from left and right subtrees and keeps the one with the highest value.

category_with_most_subcategories:
The function finds the node with the most direct children. It counts children for each node and compares results across the tree to find the maximum.


Complexity Analysis Answers: 

Q1. What is the time and space complexity of each traversal? 
Ans: Time: O(n) 
Space: O(h) (recursion stack) 

Q2. When would you use pre-order vs. post-order for aggregating metrics? 
Ans: Pre-order → structure/export. 
Post-order → aggregation (bottom-up) 

Q3. How would you implement an iterative version of these traversals using a stack? 
Ans: Use stack 
Simulate recursion manually 

Q4. For a social network's category export feature, which traversal is most appropriate and why? 
Ans: Pre-order (preserves structure) 