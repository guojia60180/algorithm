#Author guo
#正则
import re
class Solution:
    def atio(self,str):
        str=str.strip()
        str=re.findall('(^[\+\-0]*\d+)\D*',str)

        try:
            result=int(''.join(str))
            MAX_INT=2**32
            MIN_INT=-2**32
            if result>MAX_INT>0:
                return MAX_INT
            elif result<MIN_INT<0:
                return MIN_INT
            else:
                return result

        except:
            return  0