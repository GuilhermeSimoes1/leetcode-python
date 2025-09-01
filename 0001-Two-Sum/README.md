Two Sum 
-
The logic I used for this problem is not the best one, but I wanted to start with the first idea that came to my mind and document the process.

Step 1
-
The first thing I thought of was using a double for loop, because this way I can iterate through all the indices in the array and sum each element with the others.
Example with array [1,2,3,4,5]:

Logic: [1+2], [1+3], [1+4]...

Step 2
-
The problem asks for the two indices of the numbers that add up to the target.
So, I needed a way to know the index. At first I didn’t know, but then I discovered that Python has a function (enumerate) that returns both the index and the value of an element in the array.

Step 3
-
Now, the only thing left is to return the two indices where the sum of their values is equal to the target,
for that, i used an if statement to check the condition, and I also had to add another check to avoid summing the same index with itself.

 
<img width="919" height="588" alt="image" src="https://github.com/user-attachments/assets/99ce4c33-4397-4b13-8f15-790a88863d6a" />
