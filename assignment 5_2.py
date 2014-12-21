'''
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered,
print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try
/except and put out an appropriate message and ignore the number. Enter the numbers from the book for problem 5.1 and Match the
desired output as shown.
'''


'''
Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
'''

largest = None
smallest = None

while 1:

    n = raw_input("Enter a number: ")
    
    # Handle the edge cases
      
    if len(n) < 1:
        break               # Check for empty line
            
    if n == "done": 
        break 
    
    # Do the work
    
    try:            
        num = int(n)
        
        if largest is None:
            largest = num
        elif num > largest:
            largest = num
        
        if smallest is None:
            smallest = num
        elif num < smallest:
            smallest = num

    except:
        print "Invalid input"
        continue
     
print "Maximum is", largest
print "Minimum is", smallest



'''
Desired Output:
Invalid input
Maximum is 7
Minimum is 4
'''
