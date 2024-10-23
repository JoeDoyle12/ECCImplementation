"""
elliptic_curve.py: Define a class representing a finite Elliptic Curve
Author: Joe Doyle

Lots drawn from this paper: https://math.uchicago.edu/~may/REU2020/REUPapers/Shevchuk.pdf
"""

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
        
        if p1 == self.PTATINF:
            return p2
        elif p2 == self.PTATINF:
            return p1
        elif p1 == p2:
            pass
        elif p1[0] == p2[0]:
            return self.PTATINF
        else:
            pass

    def scalar_product(self, t, p):
        """
        Calculate the product t*p, where p is a point on the elliptic curve and t is an integer

        Uses Double and Add algorithm found here: https://math.uchicago.edu/~may/REU2020/REUPapers/Shevchuk.pdf
        """

        bits = bin(t)[2:] # Chops off the first 2 characters (0b) in binary string

        result = self.PTATINF

        for b in bits:
            if b == '1':
                result = self.add_points(result, p)
            p = self.add_points(p, p)
        
        return result
