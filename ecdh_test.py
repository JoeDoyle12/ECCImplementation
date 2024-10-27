"""
ecdh_test.py: Test our ECDH class
Author: Joe Doyle
"""

from ec.elliptic_curve import EllipticCurve
from ecdh.ecdh import ECDH


ecurve = EllipticCurve(2, 2, 17)

alice = ECDH(ecurve.get_point_from_x(5, pos=False), 6, ecurve)
bob = ECDH(ecurve.get_point_from_x(5, pos=False), 4, ecurve)

a_pub = alice.get_public()
b_pub = bob.get_public()

print("Alice", alice.get_shared(b_pub))
print("Bob", bob.get_shared(a_pub))