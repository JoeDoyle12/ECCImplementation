"""
ec_actor.py: Defines an ECActor class to represent a participant in a conversation encrypted with an Elliptic Curve-based cryptographic protocol
Author: Joe Doyle
"""

class ECActor:
    def __init__(self, curve):
        """
        Initialize an actor for our cryptographic protocol (private key will be random)
        """
        
        self.curve = curve
        self.priv = ECActor.rand_private()
    
    def rand_private():
        """
        Generate a random private key
        """

        return 1
    
    def encrypt(self, point, receiver):
        """
        Send a message containing a point on our elliptic curve to the receiver
        """
        
        