from statistics import pstdev

tl = [5, 10, 10, 10, 15, 11, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

total = sum(tl)

sd = pstdev(tl)


print(total, total/len(tl), sd)