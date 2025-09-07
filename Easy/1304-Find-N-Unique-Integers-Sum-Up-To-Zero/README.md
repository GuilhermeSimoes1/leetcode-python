Find N Unique Integers Sum Up To Zero
-
Hello again! In this problem, I came up with two solutions. I will explain the one that was accepted by LeetCode. The other one was not accepted because it violated a constraint.
According to the problem statement, the goal of this exercise is to receive an integer as a parameter of the function. We then need to build an array with the same length as this integer value. The key point is that the sum of all the numbers in the array need to be equal 0 and all the numbers in the array need to be diferent so you cant just put an array with length 5 like this [0,0,0,0,0] xD:

<img width="682" height="447" alt="image" src="https://github.com/user-attachments/assets/36aded5d-8feb-4612-a9ad-bff4631fa626" />

Step 1
-
First "if", if the n = 1, so we can add instantly the number 0:

<img width="192" height="83" alt="image" src="https://github.com/user-attachments/assets/533646ec-7328-47f1-b9c8-c951030674a7" />

Step 2
-
In the second step, we handle the case where n is even. The idea is very simple: since the array must contain unique numbers, we use a for loop that iterates from 1 up to n/2. For each iteration, we insert the current number into the array and then insert its negative counterpart. For example, if we add 1, we also add -1, because 1 + (-1) = 0. This process continues until we reach the required length.

<img width="233" height="93" alt="image" src="https://github.com/user-attachments/assets/abbcc35d-51d0-4039-8e75-346cf8c805b9" />

Step 3
-
In the final step, we apply the same logic as in step 2, but now for the case where n is odd. We divide n // 2 to get the integer part and generate pairs in the same way as before. The only difference is that, at the end, we add the number 0. This works because the problem statement does not forbid using zero—it only forbids repeating numbers. Therefore, for all odd values of n, we build pairs as before and then append 0 to reach the correct length.

<img width="217" height="108" alt="image" src="https://github.com/user-attachments/assets/b34e3d2c-eb03-42c0-bfdc-756e1a316e8b" />

Submission
-
A bad runtime ;( 

<img width="740" height="691" alt="image" src="https://github.com/user-attachments/assets/ae5e8937-fde3-465d-90b3-eac3937e3e29" />

