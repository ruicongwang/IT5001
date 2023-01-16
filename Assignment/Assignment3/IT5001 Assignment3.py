'''
Full Name:
Matric No.:
Email:
'''
import random

#Complete Q1a below
def nChooseK(n,k):
    if k == 0:
        return 1
    else:
        result = 1
        for i in range(1, k+1):
            result = result * (n - i + 1) // i
        return result

#Complete Q1b below
def nChooseK_recursive(n,k):
    if k == 0 or k == n:
        return 1
    else:
        return nChooseK_recursive(n-1,k-1) + nChooseK_recursive(n-1,k)

'''
Space for your thought in Question 1c



'''

    
#Complete Q2 below
def monte_carlo_pi(n):
    r = 1
    k = 0
    for i in range(n):
        x = random.uniform(-r,r)
        y = random.uniform(-r,r)
        d_square = x**2 + y**2
        if d_square <= r**2:
            k = k + 1
    p = k / n
    return 4*p




print(monte_carlo_pi(10))
print(monte_carlo_pi(100))
print(monte_carlo_pi(1000))
print(monte_carlo_pi(10000))
print(monte_carlo_pi(100000))
print(monte_carlo_pi(1000000))

