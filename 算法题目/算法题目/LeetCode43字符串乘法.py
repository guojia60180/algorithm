#Author guo

def multiply( num1, num2):
    res = []
    for i in range(len(num1)):
        for j in range(n=len(num2)):
            #Multiply num1's digit number by digit * num2's digit number by digit
		    #and stroe the result in a list
			res.append(int((num1[-i-1]))*(10**i)*int((num2[-j-1]))*(10**j))
    # sum up the list of numbers and convert it to a string
	return str(sum(res))
