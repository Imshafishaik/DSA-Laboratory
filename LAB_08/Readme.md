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
 
-------------------------Exercise 2 done by Anshul-------------------------

Logic & Approach: 

A max-heap stores posts so the most-liked post is always at the root (index 0). The heap is stored as a flat array - for node at index i, its left child is at 2i+1, right child at 2i+2, parent at (i-1)//2. 

Push: append to end, then bubble up (compare with parent, swap if larger) 
Pop max: swap root with last element, remove last, bubble down (compare with children, swap with larger child) 
Update likes: find the post, update its value, then bubble up or down depending on whether likes increased or decreased 


Complexity Analysis Answers:

1.What is the time complexity of get_top_k(k)? Why is it better than sorting all posts? 

Ans: Time complexity of get_top_k(k): 
Copy the heap: O(n) 
Extract k times, each extraction is O(log n): O(k log n) 
Total: O(n + k log n) 
 
2.If you used a sorted array instead of a heap, what would be the cost of update_likes()? 
 
Ans: Update cost with sorted array: 
Finding the post by ID: O(n) linear scan (or O(log n) binary search by likes but after update, position changes) 
Re-inserting in sorted position: O(n) shifting 
Total: O(n) per update, compared to O(log n) for heap 
 

3.How would you modify the heap to automatically remove posts older than 24 hours?  

Ans: Add a timestamp field to each entry. Use a secondary min-heap on timestamp alongside the max-heap on likes. Periodically (or on every push/pop), check if the minimum timestamp entry is older than 24 hours. if so, mark it as deleted (lazy deletion with a valid flag). On pop, skip entries marked deleted.


-------------------------Exercise 3 done by shafi-------------------------

Logic & Approach: 

A Trie stores strings character by character. Each node represents one character. The path from root to a node spells out a prefix. A node marked is_end = True means a complete username ends there. Autocomplete works by navigating to the prefix node, then collecting all complete usernames in the subtree below it.

A segment tree is a binary tree built over an array. Each leaf stores one day's activity. Each internal node stores the aggregate (sum, max, or min) of its range. A node covering range [l, r] has left child covering [l, mid] and right child covering [mid+1, r]. This allows any range query in O(log n) by combining at most O(log n) pre-computed segments.


Complexity Analysis Answers: 

1.Time complexity of query(l, r)? Prove it.

Navigate to prefix node: O(|prefix|)
Collect all matches in subtree: O(total characters in all matching usernames)
For max_results=m results each of average length L: O(|prefix| + m×L)
Overall: O(|prefix| + output size)

2.Space complexity of a segment tree for 365 days?

Each character = one node; shared prefixes share nodes
Worst case (no shared prefixes): 1M × 12 = 12 million nodes
At ~60 bytes per node (Python dict + flags): ~720 MB
With shared prefixes (realistic): significantly less — maybe 3–5 million nodes

3.If you used a prefix sum array instead of a segment tree, what would be the
cost of updates? When is each better?

Hash map: search for exact key is O(L) — it cannot find all strings with a given prefix without scanning all keys O(n×L)
Trie: prefix navigation in O(|prefix|), then collect all results in the subtree — inherently prefix-optimised
Trie wins for any prefix-based operation; hash map wins only for exact-match lookup