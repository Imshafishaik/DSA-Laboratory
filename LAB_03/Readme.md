LAB-03                         Advanced Algorithms and Programming                             Team - 23
--------------------------------------------------------------------------------------------------------

Team Members :- Shaik Shafi & Anshul Reddy

-------------------------Exercise 1 done by shafi-------------------------

Logic Explanation:
The story content system utilizes a doubly linked list to create a swipeable
story feed. Each story is a StoryNode containing its information and pointers to
the next and Prev stories. The Story Feed manages the list with head, tail,
current viewing position, and size. New stories are added to the tail to maintain
chronological order. Navigation is simple: moving forward shifts the current
pointer to current.next, and moving backward shifts it to current.prev.

Complexity Analysis Answers

Q1. Compare forward/backward navigation complexity
----------------------------------------------------------
      Structure           Forward              Backward.  |
   Singly Linked List      O(1)                  O(n).    |
   Doubly Linked List      O(1)                  O(1).    |
----------------------------------------------------------

Explanation:
Singly linked lists only store a next pointer, so moving backward requires
traversing from the head.
Doubly linked lists store both next and previous pointers, allowing constant-
time backward traversal.


Q2. Time complexity of removing a node with pointer
O(1)
Explanation:
If we already have the pointer to the node, we only update:
prev.next = next
next.prev = prev
No traversal is required.


Q3. Extra memory required
A doubly linked list stores:
data + next pointer + prev pointer
A singly linked list stores:
data + next pointer
Thus, 1 extra pointer per node is required.


Q4. When bidirectional navigation is useful
Examples include:
• Social media feeds
• Browser history
• Music playlist navigation
• Image galleries
• Undo/redo systems
These systems frequently move both forward and backward, making doubly
linked lists beneficial.


-------------------------Exercise 2 done by Anshul-------------------------

Logic Explanation:
Social media tracks recent activity with a stack (LIFO). New actions (like, comment, share,
follow) are pushed onto the top. Users can pop () off or peek () at the latest activity. An
undo stack holds popped actions.
Notifications use a queue (FIFO) for sequential handling. New notifications enqueue () at
the rear and are processed by dequeue () from the front. Urgent items use priority enqueue
() to jump the line.

Complexity Analysis Answers
Q1. Compare time complexity of all operations
-----------------------------------------------------------------------------
           Operation                  Stack                   Queue.         |
            Insert                     O(1)                    O(1)          |
            Remove                     O(1)                    O(1)          |
          Peek/Front                   O(1)                    O(1).         |
-----------------------------------------------------------------------------
Both stacks and queues support constant-time insertion and deletion.

Q2. For a queue, which implementation (array circular buffer vs. linked list) is more memory efficient for unknown size?
Linked list implementation is more memory efficient because:
It dynamically allocates memory.
It does not require fixed capacity.
Arrays require reallocated memory and may waste space.

Q3. What is the amortized time complexity of a sequence of n enqueue/dequeue Operations?
For n enqueue and dequeue operations:
Total cost = O(n)
Thus amortized complexity per operation: O(1)

Q4. How would you implement a deque (double-ended queue) to support both stack and queue operations?
A Deque (Double Ended Queue) supports:
Insert front
Insert rear
Delete front
Delete rear

Best implementation:

Doubly Linked List

Operations:
-------------------------------------------------
      Operation	                Complexity.      |
     Insert Front	               O(1).         |
     Insert Rear	               O(1)          |
     Delete Front	               O(1)          |
     Delete Rear	               O(1).         |
-------------------------------------------------







