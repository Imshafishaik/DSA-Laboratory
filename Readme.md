LAB-05                         Advanced Algorithms and Programming                             Team - 23
--------------------------------------------------------------------------------------------------------

Team Members :- Shaik Shafi & Anshul Reddy

 -------------------------Exercise 1 done by Anshul-------------------------

Logic Explanation:

calculate_height:
The function calculates the height of a tree by checking how deep the tree goes. It starts from the current node and recursively finds the height of the left and right subtrees. Then it takes the larger of the two and adds one for the current node. If the node is empty, it returns -1, meaning no height.

calculate_node_height:
The function searches for a specific category and calculates how far it is from the root. It checks if the current node matches the target ID. If not, it searches in both left and right subtrees. When the target is found, it returns the distance by adding one at each step while going back up.

count_nodes:
The function counts all categories in the tree. It starts from the current node and counts it as one. Then it recursively counts nodes in the left and right subtrees and adds them together. If the node is empty, it returns zero.

count_leaves:
The function counts how many categories have no subcategories. It checks if a node has no left or right child, and if so, counts it as a leaf. Otherwise, it continues checking both subtrees and adds their leaf counts.

is_balanced:
The function checks whether the tree is balanced by comparing the heights of left and right subtrees for each node. If the difference is more than one, the tree is not balanced. It applies this check recursively to all nodes.

find_category:
The function searches for a category using its ID. It checks the current node first. If it doesn’t match, it searches in the left subtree, and if still not found, it searches in the right subtree. It stops when the category is found or the tree ends.

find_path_to_root:
The function finds the path from a category to the root. When it finds the target node, it starts building a list. As recursion returns back up, each parent node is added to the list, forming the path from the target to the root.

lowest_common_ancestor:
The function finds the common parent of two categories. It searches for both nodes in the tree. If one node is found in the left subtree and the other in the right subtree, then the current node is their lowest common ancestor. Otherwise, it returns whichever side contains both nodes.


Complexity Analysis Answers:

Q1. What is the time complexity of calculating tree height? Prove it.
Ans: Visits every node = O(n)

Q2. For a perfectly balanced binary tree with n nodes, what is the maximum height?
Ans: O(log n)

Q3. In a social network with millions of categories, why would balance matter?
Ans. Balanced = fast search O(log n)
Unbalanced = worst case O(n)

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