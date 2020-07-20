x = 0
for i in range(1, 10000001):
    xnew = (2*x**2 + 3)/ 5
    if abs(xnew - x) < 0.0001:
        break
    x = xnew

print("The root : %0.5f" % xnew)
print("The number of iterations : %d" % i)
