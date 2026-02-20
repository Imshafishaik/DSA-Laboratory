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

---------------------------------------------------------------------|
     Representation                        Complexity                |
---------------------------------------------------------------------|
       Sorted arrays                         O(m + n)                |
                                                                     |
       Hash sets                             O(min(m, n))            |
                                                                     |
---------------------------------------------------------------------|                                                                     

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

-------------------------Exercise 3 done by Anshul-------------------------

Logic Explanation:
in this exercise, friend recommendation is based on the similarity of user interests. User interests are represented using a user–interest matrix, where each row corresponds to a user and each column corresponds to a specific interest. The value stored in each cell represents the level of interest of a user in a particular category on a scale from 0 to 10.
Each user’s interests are treated as a multi-dimensional vector. To measure how similar two users are, cosine similarity is used. Cosine similarity calculates the cosine of the angle between two vectors, focusing on the similarity in interest patterns rather than absolute values. A higher cosine similarity value indicates that users have similar preferences, while a lower value indicates dissimilar interests.
For friend recommendation, the similarity between a given user and all other users is computed. Existing friends and the user themself are excluded from consideration. The remaining users are sorted based on similarity scores, and the top K most similar users are recommended as potential friends.

1. What is the time complexity of computing all pairwise similarities for U users and I interest?
Time complexity of computing all pairwise similarities for U users and I interest is O (U^2.I)
2. How would you optimize this for sparse matrices (most users have few
interests)?
Use sparse representations (list of (interest, strength) pairs)
Only compute dot products over nonzero overlaps
Reduces time complexity for sparse data to: O (U.avg_nonzero^2)
3. What is the space complexity of storing the full matrix vs. sparse
Representations?
---------------------------------------------------------------------------------------
               Representation                         Space                            |
               Full matrix                          O(U × I)                           |
          Sparserepresentation                 O(total_nonzero_entries).               |
----------------------------------------------------------------------------------------











