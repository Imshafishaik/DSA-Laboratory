LAB-03                         Advanced Algorithms and Programming                             Team - 23
--------------------------------------------------------------------------------------------------------

Team Members :- Shaik Shafi & Anshul Reddy

-------------------------Exercise 1 done by shafi-------------------------

Logic Explanation: 

The program first prints the current comment and then shows all replies under it with more spaces to make the thread easy to read. It counts the total comments by starting with one for the main comment and then adding the number of comments from all replies using recursion. For total likes, it adds the likes of the main comment and then includes the likes from all replies. To find the deepest reply, it checks how far the replies go and keeps the largest depth level found. The search by user feature checks if the current comment was written by the given user. If not, it continues searching through all replies until it finds the user or finishes checking all comments. 

Complexity Analysis Answers 

Q1. What is the time complexity of traversing an entire comment thread with n total comments? 

Ans: If there are n comments in the thread then the time complexity will be : O(n). Because every comment is visited exactly once. 

Q2. How does recursion depth relate to the comment nesting structure? What happens with very deep threads (1000+ levels)? 

Ans: Recursion depth equals the maximum nesting level of replies 

If threads become extremely deep (1000+ levels), it may cause stack overflow. 

 

Q3. Compare memory usage between recursive and iterative stack-based implementations 

Approach                     Memory Usage 

Recursive                Uses system call stack 

Iterative                 Uses explicit stack 

Recursive version uses stack frames automatically, while iterative version stores states manually.


-------------------------Exercise 4 done by Anshul-------------------------

Logic Explanation:

split the array in half at each step, solve each half independently, then combine results. This is the classic divide-and-conquer pattern. For merge sort, the combining step (merge) does the real work. For ind_peak_hour binary search works because the peak has the property that one neighbor is always smaller - we can determine which side the peak is on by comparing the midpoint with mid+1. 

Complexity Analysis Answers

Q1. What is the time complexity of recursive max_engagement? Prove it. 

Ans: max_engagement time complexity: T(n) = 2T(n/2) + O(1) by Master Theorem = O(n). Every element is visited once 

Q2. Compare recursive merge sort (O(n log n)) with iterative insertion sort (O(n²)) for sorting 10,000 posts 

Ans: Merge sort O(n log n) vs insertion sort O(n²) on 10,000 posts: merge sort ≈ 133,000 ops vs insertion sort ≈ 100,000,000 ops — merge sort is ~750× faster. 

 

Q3. What is the recursion depth for merge sort on n elements? 

Ans: Recursion depth for merge sort O(log n) — the tree of calls is log₂(n) levels deep 


Q4. For find_peak_hour, why can we use binary search-style recursion? What 

property must the array satisfy? 

Ans: find_peak_hour binary search justification works because if likes[mid] < likes[mid+1], the right side is increasing so a peak must exist there (and vice versa).  

The array must be unimodal (rises then falls) — a global max with no plateaus of equal value. 