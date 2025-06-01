# A student is taking a cryptography class and has found anagrams to be very useful. Two strings are anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.
#
# The student decides on an encryption scheme that involves two large strings. The encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Determine this number.
#
# Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.
from collections import Counter


def makeAnagram(a, b):
    count_a = Counter(a)
    count_b = Counter(b)
    count = 0
    set_a=set(a)
    set_b=set(b)
    union_set=set_a.union(set_b)


    for item in union_set:
        if (item in count_b) and (item in count_a):
            count += abs(count_a[item] - count_b[item])
        else:
            count += count_a[item]
            count += count_b[item]
    return count

# a='cde'
# b='abc'
# print(makeAnagram(a, b))


def isValid(s):
    # Write your code here
    count_s= Counter(s)

    if  len(set(count_s.values()))>1:
        return 'NO'
    else:
        return 'YES'

s='aabbc'



def repeatedString(s, n):
    # Write your code here
    if s=='a':
        return n
    if len(s)<n:
        times= n//len(s)+1
        new_str= s*times
    count_s= Counter(new_str[:10])
    for key in count_s:
        if key=='a':
            return count_s[key]

s='a'
n=1000000000000
print(repeatedString(s, n))