#Author guo
class Solution:
    def nextGreatestLetter(self, letters, target):
        l,r=0,len(letters)-1
        if target>letters[r]:
            return letters[0]
        while l<r:
            mid=(l+r)//2
            if letters[mid]<=target:
                l=mid+1
            else:
                r=mid

        if letters[l]>target:
            return letters[l]
        elif letters[r]>target:
            return letters[r]
        else:
            return letters[0]

