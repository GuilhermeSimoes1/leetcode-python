Longest Common Prefix
-
Spent half the morning and the whole afternoon on this problem. Later I saw other solutions were just a few lines and much more optimized, but I’m glad I figured it out and got it accepted.

The exercise ask us to write a function to find the longest common prefix string amongst an array of strings.

<img width="700" height="246" alt="image" src="https://github.com/user-attachments/assets/ade36ae3-cab9-4370-b7db-ab9372491be3" />


Step 1 
-
This step was actually one of the last I figured out, after getting an error on my submission.

<img width="900" height="532" alt="Captura de ecrã 2025-09-04 173054" src="https://github.com/user-attachments/assets/99e9b959-b5dc-4de7-98d6-a1d6206e011e" />

The first thing I did was use a for loop to iterate over the list provided by the user, since we need to compare the elements of this list with each other.

Here I also added a condition for the case where the list has only one element. If that happens, we just return this element directly since there’s nothing to compare.

(For now, let’s ignore the commonLista and the delimiter.)

<img width="494" height="249" alt="image" src="https://github.com/user-attachments/assets/defb9325-f294-4f6b-907f-d9719ce7a541" />


Step 2 
-

The main idea of this part of the code is to get the first common prefix between the first element and the second element of the list. After that, we only need to use this prefix and compare it with the next elements. If the third element (or others) doesn’t share the same prefix, then either no prefix exists or the prefix becomes shorter after those comparisons.

So I created a condition for the first iteration of the loop, where I compare the first two elements if at least two exist. That way we avoid errors when the list has only one element.

Then I used a for loop with zip to iterate through both strings at the same time, comparing character by character. If the characters match, I add them to commonLista. If they don’t, I stop with a break.

<img width="420" height="145" alt="image" src="https://github.com/user-attachments/assets/fd547216-0080-45fc-9c8c-c2d1e96f5d36" />

Step 3 
-

After comparing the first two elements, we get the “genesis” prefix. This is the prefix we’ll use to compare with the rest of the strings in the list.

For this part of the code, I created a condition where i needs to be greater than 0 and smaller than the length of the list.

Since we only want to return the final prefix, we just keep updating it as we go. To convert the commonLista list into a string, I used join. That’s why I created a delimiter earlier. In this case, the delimiter is just an empty string, since we want the letters to be concatenated directly. The result is stored in the variable word.

After that, I clear commonLista so we can use it again with the updated prefix. This time we compare the current prefix (word) with the next element of the list. Then we update both commonLista and word based on the new prefix.

<img width="352" height="197" alt="image" src="https://github.com/user-attachments/assets/5b8d367b-ccca-4744-b166-abdffca82507" />


Step 4 
-

The last step is simple: we just need return the final prefix.

Here I again use delimiter.join(commonLista). When we reach the last element of the list, the condition 0 < i < len(strs) becomes false. But since the last operation we did was appending to commonLista, we just need one last join to return the final prefix string.

<img width="328" height="99" alt="image" src="https://github.com/user-attachments/assets/a6a54350-c4e8-4bc7-9030-468591a42857" />


Submission LettCode:
-
Let's goo! I got the exercise accepted, but with a bad runtime xD. I made it more complicated than it needed to be.

<img width="914" height="753" alt="Captura de ecrã 2025-09-04 173214" src="https://github.com/user-attachments/assets/4417e257-7328-4244-824d-df6aeb202b18" />


