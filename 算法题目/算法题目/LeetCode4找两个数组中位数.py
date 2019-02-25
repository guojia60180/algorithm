#Author guo
class Soultion:

    def findmedian(self,nums1,nums2):
        def median(a):
            if len(a) % 2 != 0:
                return (a[(len(a) + 1) / 2] + a[(len(a) - 1) / 2])
            if len(a) % 2 == 0:
                return (a[len(a) / 2])

        num=nums1+nums2

        num=num.sort()
        return (median(num))
