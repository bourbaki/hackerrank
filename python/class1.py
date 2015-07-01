#!/usr/bin/env python

from math import sqrt

class ComplexNumber(object):
    """ComplexNumber Class"""
    def __init__(self, real, im):
        super(ComplexNumber, self).__init__()
        self.real = real
        self.im = im
    
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.im + other.im)
        
    def __abs__(self):
        return self.absolute()
        
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.im - other.im)
        
    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.im * other.im, self.real * other.im + self.im * other.real)
    
    def __str__(self):
        if self.im == 0:
            return "{:.2f}".format(self.real)
        elif self.real == 0:
            return "{:.2f}i".format(self.im)
        else:
            op = "+" if self.im > 0 else "-"
            return "{:.2f} {} {:.2f}i".format(self.real, op, abs(self.im))  
    
    def __repr__(self):
        return "<ComplexNumber re:{} im:{}>".format(self.real, self.im)
        
    def absolute(self):
        return sqrt(self.real ** 2 + self.im ** 2)
        
    def __len__(self):
        return self.absolute()
        
    def __truediv__(self, other):
        # Как делать в зависимости от класса
        K = other.real ** 2 + other.im ** 2
        return ComplexNumber((self.real * other.real + self.im * other.im) / K, (self.im * other.real - self.real * other.im) / K )
        
if __name__ == '__main__':
    z1 = ComplexNumber(*map(float, input().strip().split()))
    z2 = ComplexNumber(*map(float, input().strip().split()))
    print(z1 + z2)
    print(z1 - z2)
    print(z1 * z2)
    print(z1 / z2)
    print("{:.2f}".format(abs(z1)))
    print("{:.2f}".format(abs(z2)))