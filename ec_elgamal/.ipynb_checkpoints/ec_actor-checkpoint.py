"""
ec_actor.py: Defines an ECActor class to represent a participant in a conversation encrypted with an Elliptic Curve-based El-Gamal Cryptographic Protocol
Author: Joe Doyle

Outline of the ElGamal Cryptosystem found here: https://math.uchicago.edu/~may/REU2020/REUPapers/Shevchuk.pdf
"""

from ecdh.ecdh import ECDH

class ECActor:
    def __init__(self, p, ord_p, curve):
        """
        Initialize an actor for our El Gamal system (private key will be random)

        p: random point on the curve
        ord_p: order of p
        curve: elliptic curve to perform operations on
        """
        
        self.curve = curve
        self.p = p
        self.ord_p = ord_p
        self.ecdh = ECDH(self.p, self.curve)

    def get_public(self):
        """
        Get the public key of an actor in our ElGamal cryptosystem
        """
        
        return self.ecdh.get_public()
    
    
    def encrypt(self, point, receiver_pub):
        """
        Send a message containing a point on our elliptic curve to the receiver

        point: point to encrypt
        receiver_pub: receiver's public key
        """
        
        # c = self.curve.scalar_product(self.priv, self.p) # compute C = k * P
        d = self.curve.add_points(point, self.ecdh.get_shared(receiver_pub)) # compute D = M + shared key (shared key is just k * Q)

        return (self.get_public(), d) # Return public key and ciphertext

    def decrypt(self, encrypted_output):
        """
        Decrypt a message stored in "encrypted_output" of the form (public key, ciphertext)
        """
        
        c, d = encrypted_output

        m = self.curve.add_points(d, self.curve.neg(self.ecdh.get_shared(c))) # compute M = D - shared key (shared key is just priv * C )

        return m