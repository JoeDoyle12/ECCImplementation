"""
elliptic_curve.py: Define a class representing a finite Elliptic Curve
Author: Joe Doyle

Lots drawn from this paper: https://math.uchicago.edu/~may/REU2020/REUPapers/Shevchuk.pdf
"""

import math

class EllipticCurve:
    def __init__(self, a, b, p):
        """
        Initialize an Elliptic Curve of the form y^2 = x^3 + ax + b (mod p)
        """

        self.a = a
        self.b = b
        self.p = p

        self.PTATINF = (0, 0) # Point at Infinity
    
    def add_points(self, p1, p2):
        """
        Add two points p1 and p2 along this elliptic curve

        p1: (p1x, p1y)
        p2: (p2x, p2y) 
        """
        
        self.assert_point(p1)
        self.assert_point(p2)

        slope = 0

        if p1 == self.PTATINF:
            return p2
        elif p2 == self.PTATINF:
            return p1
        elif p1 == p2:
            slope = (((3 * p1[0]**2 + self.a) % self.p) * pow(2 * p1[1], -1, self.p)) % self.p
        elif p1[0] == p2[0] and p1[1] == -1 * p2[1]:
            return self.PTATINF
        else:
            slope = ((p2[1] - p1[1]) * pow(p2[0] - p1[0], -1, self.p)) % self.p

        xr = (slope ** 2 - p1[0] - p2[0]) % self.p
        yr = (slope * (p1[0] - xr) - p1[1]) % self.p

        return xr, yr

    def scalar_product(self, t, p):
        """
        Calculate the product t*p, where p is a point on the elliptic curve and t is an integer

        Uses Double and Add algorithm found here: https://math.uchicago.edu/~may/REU2020/REUPapers/Shevchuk.pdf
        """

        bits = bin(t)[2:] # Chops off the first 2 characters (0b) in binary string

        result = self.PTATINF

        for b in reversed(bits):
            if b == '1':
                result = self.add_points(result, p)
            p = self.add_points(p, p)
        
        return result

    def neg(self, point):
        """
        Return (a, -b) when given a point (a, b) on an elliptic curve 
        """
        
        return (point[0], (-1 * point[1]) % self.p)


    def get_point_from_x(self, x, pos = True):
        """
        Get a point on the curve from an x coordinate (pos controls if it is the positive or negative point corresponding to the point)
        """

        for y in range(self.p):
            if (y ** 2) % self.p == (x ** 3 + self.a * x + self.b) % self.p:
                point = (x, y % self.p)
                self.assert_point((x, y % self.p))
                if pos:
                    return point
                else:
                    return self.neg(point)

    def assert_point(self, p):
        """
        Assert that a point is on the elliptic curve
        """

        if p == self.PTATINF:
            return

        assert (p[1] ** 2) % self.p == (p[0] ** 3 + self.a * p[0] + self.b) % self.p