def count_max_frequency(string) -> int:
    '''
    program that takes a string as input,
    and counts the frequency of each word in the string 
    and returns the highest frequency
    '''
    li = string.split()
    d = {}
    for i in li:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    max_frequency = max(d.values())
    highest_frequency_word = [word for word, frequency in d.items() if frequency == max_frequency]
    highest_frequency_length = len(highest_frequency_word[0])
    
    return highest_frequency_length

print(count_max_frequency('write write write all the number from from from 1 to 100'))
print(count_max_frequency('Hello my name is Hello and I am Hello'))
print(count_max_frequency('give me 4 give me 4 me me me give me'))


'''
Explanation : In first test case we see the word with max frequency is write and its length is 5.

In second test case we see the word with max frequency is Hello and its length is 5. 

In third test case we see the word with max frequency is me and its length is 2
'''