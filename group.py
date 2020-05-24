# group
import math


class Group(object):
    def __init__(self, N, val=1):
        self.N = N
        self.val = val % N;

    def __add__(self, other):
        if (self.N != other.N):
            raise Exception("Elements not in the same group")
        temp = self.val + other.val;
        temp = temp % self.N
        return Group(self.N, temp)
    
    def __sub__(self, other):
        if (self.N != other.N):
            raise Exception("Elements not in the same group")
        temp = self.val - other.val;
        temp = temp % self.N
        return Group(self.N, temp)

    def __mul__(self, other):
        if (self.N != other.N):
            raise Exception("Elements not in the same group")
        temp = self.val * other.val;
        temp = temp % self.N
        return Group(self.N, temp)

    def __pow__(self, pow):
        if (pow < 1):
            raise Exception("power less than one")
        if (pow == 1):
            return Group(self.N, self.val)
        else:
            if (pow % 2 == 1):
                return ((Group(self.N, self.val) * Group(self.N, self.val)) ** (pow // 2)) * Group(self.N, self.val)
            else:
                return ((Group(self.N, self.val) * Group(self.N, self.val)) ** (pow // 2))
        