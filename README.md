Team Members
Shaik Shafi
Anshul Reddy

-------------------------Exercise 1 done by shafi-------------------------


first question is integer mirror means nothing but reverse a number.
1) while loop n!=0 runs until n != 0.
2) The main logic is first we will mod a value. like 123%10 we will get remainder=3.
3) then we will 0*10+3 so will get 3 and assigned to reverse=3.
4) then we will do 123/10 we will get 12 and so n=12.
5) like this it repeats until n!=0;

1. How many arithmetic operations are performed for a d-digit number?

d = number of digits in n
The while loop runs once per digit, so it runs d times.

Arithmetic operations per loop:

remainder = n % 10 → 1 modulo

reverse * 10 → 1 multiplication

+ remainder → 1 addition

n /= 10 → 1 division 

so total 4 arthimetic

2. What is the time complexity in terms of n?
O(n)

-------------------------Exercise 2 done by shafi-------------------------

second question is balanced symbols means checking every open bracket has closed bracket.
1) first we will initialize a empty stack.
2) then we will run a loop on string and if there is open bracket we will push to stack.
3) and when closed bracket comes we will check the stack is it empty then return false.
4) if it's exist then pop it.

1. How many comparisions needed for an n-character string?
For a string of length n:
Each character is runs once.
For every close bracket, one comparison is done with the top of the stack.

so, n comparisions.

2. What happens if we extend to include additional symbol pairs or other different characters?
if we add more symbol pairs, the idea will be the same and time complexity will be O(n).


-------------------------Exercise 3 done by shafi-------------------------

third question merge overlap nothing but merging the overlap of arrays.
1) first we checked intervals length is less than 1 then return intervals because there is no use of checking it.
2) then we are sorting intervals.
3) we created empty stack merged. and took current and assigned first positioned array.
4) then we run a loop and checked with current in if else. using Math.max() we found the bigger and assigned to current.
5) in else condition we pushed the current. and assigned current to next.
6) in merged stack we pushed the current and return merged.

1. How many comparision operations are needed for n intervals?
During merging approximately n comparisons.
Sorting requires additional comparisons.

2. What is the time complexity of your solution?
Sorting intervals: O(n log n)
Merging intervals: O(n)
Time Complexity: O(n log n).

-------------------------Exercise 4 done by Anshul-------------------------

fourth question is polynomial evaluation 
1) we have created a function polynomial_evaluate and passing two parameters coeffs, x.
2) then created a result variable and assigned 0 to it. 
3) then ran a loop on coeffs, then operation result * x + coefficient. 
4) then returned result.

1. How many multiplications are needed for a degree-n polynomial?
N-degree polynomial needs n multiplications.

2. Compare the native approach: what is the improvment?
it reduces the number of operations.





