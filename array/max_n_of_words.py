class Solution:
    """
    A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
    You are given an array of strings sentences, where each sentences[i] represents a single sentence.
    Return the maximum number of words that appear in a single sentence. 

    Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    Output: 6   
    """
    def mostWordsFound(self,sentences:list[str]) -> int:
        count =0
        lst = []
        for i in range(len(sentences)):
            s= sentences[i].split(" ")
            for j in s:
                count+=1
            lst.append(count)
            count=0
        return max(lst)
           
obj = Solution()
print(obj.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))