"""
ecdh.py: Define a Diffie-Helmann asymmetric key exchange protocol based on our previous Elliptic Curve Implementation
Author: Joe Doyle
"""

import secrets

class ECDH:
    def __init__(self, p, curve, order=0):
        """
        Define a class for Diffie-Helmann key exchanges using ECC

        p: random public point that forms a cyclic subgroup
        order: order of p. Only used if part of an ECActor object
        curve: public EllipticCurve object
        """

        self.p = p
        self.curve = curve
        self.priv = self.rand_private()
    
    def rand_private(self, bytes=124):
        """
        Generate a secure random private key of length bytes
        """

        return (int.from_bytes(secrets.token_bytes(bytes))) % self.curve.p
        
    
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
        