LAB-02                         Advanced Algorithms and Programming                             Team - 23
--------------------------------------------------------------------------------------------------------


Team Members :- Shaik Shafi & Anshul Reddy

-------------------------Exercise 1 done by shafi-------------------------

Logic Explanation:
We have to loop through the message. And we find the every character whether it
is a alphabetic, uppercase and punctuation marks. If its alphabetic the increase
the alphabetic with +1 and like wise for every character based on the .

1. How many character comparisons are needed for an n-character string?
We check each character exactly once to:
Check if it is an alphabetic character
Check if it’s uppercase
Check if it’s! or?
Track repeated characters
Each check is a constant-time operation (O (1)), so the total number of comparisons is
roughly n.
Answer: O(n) character comparisons for a string of length n.

2. Can this be done in a single pass? Minimal number of passes needed?
Answer: Yes, it can be done in a single pass.
While iterating through the string once, we can simultaneously:
Count uppercase letters
Count punctuation marks
Track repeated characters
Count total alphabetic characters
Minimal number of passes required: 1. No additional passes are needed.

3. How would the complexity change if we needed to support Unicode characters beyond
ASCII?
With Unicode, operations like isUppercase() and isLetter() may be more expensive than ASCII
checks.
Each character check could involve more complex logic to figure out its category.
Time complexity: Still O(n) for n characters, but the constant factor increases because
Unicode checks are costlier.


-------------------------Exercise 2 done by shafi-------------------------

Logic Explanation:
The main login is in maths we know the intersection, difference and union
same goes here as well. We are checking the seta and setb. For intersection
we will loop the setA and check the element exists in setB. If it’s there then
add it to result. Same goes for difference but a little change and we will
minus and check if it’s not exist the add it. In jaccard_similarity we are
calling the intersection and union functions and checking.

1. What is the time complexity of set intersection for sets of size m and n?
Answer:Time complexity of set intersection hash set O (min (m, n))
worst case O (m × n) .
2. How does the representation (sorted array vs. hash set vs. bit array) affect
complexity?
Representation Complexity
Sorted arrays O(m + n)
Hash sets O(min(m, n))
3. For a network with millions of users, which representation would you choose
and why?
For network eighth million of users, it is better to use Hash sets.
Because 
1) Constant-time average lookup.
2) Scales well with large, sparse networks.
3) Used by most real-world social graphs.











