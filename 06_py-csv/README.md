Cashew
SoftDev
K<06> -- Divine Your Destiny Pt.2 Summative Assessment (Explain the code)
<2021>-<09>-<29>
How the code works
1. We opened the file in read mode which lets us go through the file's content without being able to edit (wrtie mode). Orinally, we had copied the data wrong. so we treated it as a text file instead of a csv (comma separated value).
2. Then we used the split function to divide the content of file whereever there was a newline and added each piece to a list.
3. This list had all the job and percents as one string. Then we looped through the list and looked at each item. 
4. We then split the string by the character inbetween the job and the percentage.
5. Then we put the job and percentage in a dictionary. In the dictionary, each entry has a key (like a word) and a corresponding value (like definition). In our case, the job was the key and percentage was the value.
6. Dictionaries are useful because you store two sets of related data together. The order is also not preserved so it is easy to sort, unlike lists. You can also easily find values using keys rather than their index. They also don't allows duplicates, which can be useful in some cases.
7. We then split the dictionary into two lists: one for the keys and one for the values. We do this for the random.choices method. Random.choices lets us pick a value in a list with weighted values.
