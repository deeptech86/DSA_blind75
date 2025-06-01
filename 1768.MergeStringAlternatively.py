import self


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        iteratelen = min(len(word1), len(word2))
        maxlen = max(len(word1), len(word2))
        result = ''
        for i in range(0, iteratelen):
            result += word1[i] + word2[i]

        if len(word1) > len(word2):
            result += word1[len(word2):len(word1)]
        else:
            result += word2[len(word1):len(word2)]
        return result


    word1= 'abc'
    word2 = 'pqrs'
    print(mergeAlternately( self, word1, word2))