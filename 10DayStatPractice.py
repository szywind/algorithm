from scipy.stats import norm
import math
import numpy as np
from sklearn import linear_model


# Gaussian Distribution
# {\displaystyle F(x)=\Phi \left({\frac {x-\mu }{\sigma }}\right)={\frac {1}{2}}\left[1+\operatorname {erf} \left({\frac {x-\mu }{\sigma {\sqrt {2}}}}\right)\right]}
def day5_1():
    mu, sigma = list(map(int, input().split()))
    x = float(input())
    y1, y2 = list(map(float, input().split()))
    p1 = norm.cdf(x, mu, sigma)
    p2 = norm.cdf(y2, mu, sigma) - norm.cdf(y1, mu, sigma)
    print("{0:.3f}\n{1:.3f}".format(p1, p2))


def day5_2():
    def cdf(x, mu, sigma):
        return .5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))));

    mean, stddev = list(map(int, input().split()))
    x = int(input())
    y = int(input())

    p1 = (1 - cdf(x, mean, stddev)) * 100
    p2 = (1 - cdf(y, mean, stddev)) * 100
    p3 = 100 - p2

    print("{0:.2f}\n{1:.2f}\n{2:.2f}".format(p1, p2, p3))

# Central Limit Theorem
def day6_1():
    def cdf(x, mu, sigma):
        return .5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))));
    W = int(input())
    n = int(input())
    mu = int(input())
    sigma = int(input())

    print("%.4f" % cdf(W, n*mu, math.sqrt(n)*sigma))

def day6_2():
    def cdf(x, mu, sigma):
        return .5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))));
    nTicket = int(input())
    n = int(input())
    mu = float(input())
    sigma = float(input())
    print("%.4f" % (cdf(nTicket, n * mu, math.sqrt(n) * sigma)))

def day6_3():
    import math
    n = int(input())
    mu = int(input())
    sigma = int(input())
    prob = float(input())
    z = float(input())

    a = mu - z * sigma / math.sqrt(n)
    b = mu + z * sigma / math.sqrt(n)

    print("{0:.2f}\n{1:.2f}".format(a, b))


# Pearson Correlation Coefficient
def day7_1():
    n = int(input())
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))

    def mean(x, n):
        mux = 0
        for xi in x:
            mux += xi
        return mux/n
    mux = mean(x, n)
    muy = mean(y, n)
    x = [i-mux for i in x]
    y = list(map(lambda i: i-muy, y))

    covxy = 0
    stdx = 0
    stdy = 0
    for i in range(n):
        covxy += x[i]*y[i]
        stdx += x[i]*x[i]
        stdy += y[i]*y[i]

    print("%.3f" %(covxy/(math.sqrt(stdx*stdy))))

def day7_2():
    def get_rank(X):
        x_rank = dict((x, i + 1) for i, x in enumerate(sorted(set(X))))
        return [x_rank[x] for x in X]

    n = int(input())
    X = list(map(float, input().split()))
    Y = list(map(float, input().split()))

    rx = get_rank(X)
    ry = get_rank(Y)

    d = [(rx[i] - ry[i]) ** 2 for i in range(n)]
    rxy = 1 - (6 * sum(d)) / (n * (n * n - 1))

    print('%.3f' % rxy)

# Least Square Regression Line
def day8_1():
    x = np.array([95, 85, 80, 70, 60]).reshape(-1, 1)
    y = np.array([85, 95, 70, 65, 70])
    lm = linear_model.LinearRegression()
    lm.fit(x, y)
    print(lm.intercept_)
    print(lm.coef_[0])


def day9():
    x = [[0.18, 0.89], [1.0, 0.26], [0.92, 0.11], [0.07, 0.37], [0.85, 0.16], [0.99, 0.41], [0.87, 0.47]]
    y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]
    lm = linear_model.LinearRegression()
    lm.fit(x, y)
    b = lm.intercept_
    a1, a2 = lm.coef_
    test = np.array([0.49, 0.18, 0.57, 0.83, 0.56, 0.64, 0.76, 0.18]).reshape(4, 2)
    test = np.hstack((np.ones([4, 1]), test))
    ans = test.dot(np.array([b, a1, a2]).transpose())