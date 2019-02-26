#Author guo
class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        unit = ""
        ten = ""
        hundred = ""
        thousand = ""

        # unit's place
        if num % 10 >= 1 and num % 10 <= 3:
            unit += dict[1]
            for i in range(1, num % 10):
                unit += dict[1]
        elif num % 10 == 4:
            unit += dict[1] + dict[5]
        elif num % 10 >= 5 and num % 10 <= 8:
            unit += dict[5]
            for i in range(5, num % 10):
                unit += dict[1]
        elif num % 10 == 9:
            unit += dict[1] + dict[10]
        num = int(num / 10)

        # tens place
        if num % 10 >= 1 and num % 10 <= 3:
            ten += dict[10]
            for i in range(1, num % 10):
                ten += dict[10]
        elif num % 10 == 4:
            ten += dict[10] + dict[50]
        elif num % 10 >= 5 and num % 10 <= 8:
            ten += dict[50]
            for i in range(5, num % 10):
                ten += dict[10]
        elif num % 10 == 9:
            ten += dict[10] + dict[100]

        num = int(num / 10)
        # 100ths place
        if num % 10 >= 1 and num % 10 <= 3:
            hundred += dict[100]
            for i in range(1, num % 10):
                hundred += dict[100]
        elif num % 10 == 4:
            hundred += dict[100] + dict[500]
        elif num % 10 >= 5 and num % 10 <= 8:
            hundred += dict[500]
            for i in range(5, num % 10):
                hundred += dict[100]
        elif num % 10 == 9:
            hundred += dict[100] + dict[1000]
        num = int(num / 10)

        # 100ths place
        for i in range(0, num % 10):
            thousand += dict[1000]

        return (thousand + hundred + ten + unit)
