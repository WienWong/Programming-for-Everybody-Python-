'''
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split()
function. The program should build a list of words. For each word on each line check to see if the word is already in the list
and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.pythonlearn.com/code/romeo.txt
'''

fname = raw_input("Enter file name: ")
fh = open(fname)

lst = list()
for line in fh:
    for word in line.split():
        lst.append(word)
    

lst = list(set(lst))
lst.sort()
print lst



'''
Desired Output:
['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
'''

'''
Notes:
'set' doesn't allow duplicates (that is if you try to insert the same element twice, it will simply be ignored).
one example:

Numbers = 1,1,1,3,3,3,4,4,5,5
print list(Numbers)
print list(set(Numbers))

results:
[1, 1, 1, 3, 3, 3, 4, 4, 5, 5]
[1, 3, 4, 5]
'''
