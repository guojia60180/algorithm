import collections
#Author guo
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordset=set(wordList)
        if endWord not in wordset:
            return 0
        visited=set([beginWord])

        chars=[chr(ord('a')+i) for i in range(26)]
        bfs=collections.deque([beginWord])

        res=1
        while bfs:
            len_bfs=len(bfs)
            for _ in range(bfs):
                origin=bfs.popleft()
                for i in range(len(origin)):
                    originlist=list(origin)
                    for c in chars:
                        originlist[i]=c
                        transword=''.join(originlist)
                        if transword not in visited:
                            if transword==endWord:
                                return res+1
                            elif transword in wordset:
                                bfs.append(transword)
                                visited.add(transword)
            res=res+1
        return 0