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