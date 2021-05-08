# 1 Basic - Print all integers from 0 to 150.

# for x in range(1, 151, 1):
#     print(x)

# 2 Multiples of Five - Print all the multiples of 5 from 5 to 1,000
# for y in range(5, 1005, 5):
#     print(y)


# 3 Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
# for i in range(1, 101):
#     if i%5==0 and i%10 !=0:
#         print("coding")
#     elif i%10==0:
#         print("coding dojo")
#     else:
#         print(i)     

# 4 Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
# sum=0
# for i in range(1,500001,2):
#     sum+=i
# print(sum)


# 5 Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
# for i in range(2018, 1, -4):
#     print(i)

# 6 Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
# lowerNum= 2
# higherNum= 9
# multi= 3
# for i in range(lowerNum, higherNum+1):
#     if i % multi==0:
#         print(i)