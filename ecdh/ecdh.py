"""
ecdh.py: Define a Diffie-Helmann asymmetric key exchange protocol based on our previous Elliptic Curve Implementation
Author: Joe Doyle
"""

class ECDH:
    def __init__(self, p, priv, curve):
        """
        Define a class for Diffie-Helmann key exchanges using ECC

        p: random public point that forms a cyclic subgroup
        priv: private key
        curve: public EllipticCurve object
        """

        self.p = p
        self.priv = priv
        self.curve = curve
    
    def get_shared(self, public):
        """
        Return the shared key from public key

        public: Point on elliptic curve self.curve corresponding to (others shared)*P
        """

        return self.curve.scalar_product(self.priv, public)
    
    def get_public(self):
        """
        Return the public key to be shared with the other actor
        """

        return self.curve.scalar_product(self.priv, self.p)
        