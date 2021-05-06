# 1 basic

# for x in range(1, 151, 1):
#     print(x)

# 2 Multiples of Five
# for y in range(5, 1005, 5):
#     print(y)


# 3 Counting, the Dojo Way
# for i in range(1, 101):
#     if i%5==0 and i%10 !=0:
#         print("coding")
#     elif i%10==0:
#         print("coding dojo")
#     else:
#         print(i)     

# 4 Whoa. That Sucker's Huge
# sum=0
# for i in range(1,500001,2):
#     sum+=i
# print(sum)


# 5 Countdown by Fours 
# for i in range(2018, 1, -4):
#     print(i)

# 6 Flexible Counter
lowerNum= 2
higherNum= 9
multi= 3
for i in range(lowerNum, higherNum+1):
    if i % multi==0:
        print(i)