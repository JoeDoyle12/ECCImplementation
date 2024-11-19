"""
ec_time_test.py: Test the speed of our ElGamal systems
Author: Joe Doyle
"""

import time
import matplotlib.pyplot as plt 

from ecc.ec import EllipticCurve
from ecc.ec_elgamal import ECActor

# Define Secp256k1, the elliptic curve that Bitcoin uses. It is defined over a finite field Z/pZ, so every point is a generator

p = 0xFFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFE_FFFFFC2F

ecurve = EllipticCurve(0, 7, p)

# Define Secp256k1's generator point

g = ecurve.decompress_public_key('0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798')

# Define the order of said generator point

ord_g = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

#Initiate our actors alice and bob

alice_gamal = ECActor(g, ord_g, ecurve)
bob_gamal = ECActor(g, ord_g, ecurve)

a_pub = alice_gamal.get_public()
b_pub = bob_gamal.get_public()

tests = 100

gen_time = []
encrypt_time = []
decrypt_time = []

for i in range(tests):
    t = time.time()
    to_encrypt = ecurve.random_point()
    gen_time.append(time.time() - t)

    t = time.time()
    encrypted = alice_gamal.encrypt(to_encrypt, b_pub)
    encrypt_time.append(time.time() - t)

    t = time.time()
    decrypted = bob_gamal.decrypt(encrypted)
    decrypt_time.append(time.time() - t)

    assert to_encrypt == decrypted

def avg(array):
    """
    Simple helper function to calculate average of an array
    """
    return sum(array) / len(array)

plt.bar(['Gen', 'Enc', 'Dec'], [avg(gen_time), avg(encrypt_time), avg(decrypt_time)])

plt.show()