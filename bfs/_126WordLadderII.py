import collections
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        res = []
        layer = dict()
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                print('w=:', w)
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = str(w[:i])+str(c)+str(w[i+1:])
                            print('neww=', neww)
                            if neww in wordList:
                                newlayer[neww]+=[j+[neww] for j in layer[w]]

            wordList -= set(newlayer.keys())
            layer = newlayer

        return res


sol = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

res = sol.findLadders(beginWord, endWord, wordList)
print('res=:')
print(res)