def check_valid(string) -> str:
    '''
    Function to check whether the given string is valid or not
    '''
    d = {}
    for i in range(len(string)):
        if string[i] in d:
            d[string[i]] += 1
        else:
            d[string[i]] = 1
    d_max = max(d.values())
    d_min = min(d.values())
    
    if d_max == d_min:
        return 'YES'
    else:
        return 'NO'
    
print(check_valid('abc'))
print(check_valid('abcc'))
print(check_valid('anan'))
print(check_valid('aabnbcb'))

'''
Explanation: 
In first test case number of characters are same
In second test case number of test cases are not same
In third case number of characters are same
In fourth test case number of characters are not same
'''