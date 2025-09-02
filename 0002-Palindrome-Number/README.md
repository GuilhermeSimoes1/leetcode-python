Palindrome Number
-

This solution is not the best, and it is far from the most efficient one. One of the challenges of this problem was not using string conversion. But in my solution I converted the number to a string, because in Python we cannot iterate over an integer directly. That gave me a way to loop through the digits.

About runtime and memory, this is not good either. Python is usually slower than other languages like C++, but I still wanted to do this journey with Python.

Step 1 – Put the Number into a List
-

A palindrome number is a number that reads the same from left to right and from right to left.

The first thing I did was to create a list to put the digits of the number. I didn’t want to use a built-in function that already checks if a string is the same reversed, because I think it’s more fun to do it myself.

Since we cannot loop over an integer in Python, I converted it to a string with str(). Then I used a for loop to go over each digit and insert it into a list with insert(), which lets me put the element in a specific position.

Step 2 – Make the Reversed List
-

Now we have the digits in a list, but we need another list with the digits in reverse order.

To do that, I looped through the first list but started with the index -1, so I could read from the end of the list backwards. Each digit I read, I saved in a temporary variable and then added it into the second list.

At the end, lista2 is just the reverse of lista. If the number is a palindrome, both lists will be the same.

Step 3 – Compare the Lists
-

Finally, I used an if to compare the two lists:

If they are equal → return True (it is a palindrome).

If not → return False.

Important Note:
-
This solution works, but it is not efficient because:

It creates two lists instead of working directly with the number.

I know it converts the integer into a string (which breaks one of the LeetCode constraints), but it’s not illegal xD.

It has extra runtime and memory use because of list operations.

But for me, important part was to understand how palindromes work and to build my own solution step by step, and the LeetCode accept my solution so GG.