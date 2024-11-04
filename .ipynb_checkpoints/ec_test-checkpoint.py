"""
ecdh_test.py: Test our ECDH class
Author: Joe Doyle
"""

from ec.elliptic_curve import EllipticCurve
from ecdh.ecdh import ECDH
from ec_elgamal.ec_actor import ECActor

# Define Secp256k1, the elliptic curve that Bitcoin uses. It is defined over a finite field Z/pZ, so every point is a generator

p = 0xFFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFF_FFFFFFFE_FFFFFC2F

ecurve = EllipticCurve(0, 7, p) # y^2 = x^2 + 7 (mod p)

# Define Generator point

g = ecurve.decompress_public_key('0279BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798')


ord_g = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

alice = ECDH(g, ecurve)
bob = ECDH(g, ecurve)

a_pub = alice.get_public()
b_pub = bob.get_public()

print("Alice shared:", alice.get_shared(b_pub))
print("Bob shared:", bob.get_shared(a_pub))

alice_gamal = ECActor(g, ord_g, ecurve)
bob_gamal = ECActor(g, ord_g, ecurve)

a_pub = alice_gamal.get_public()
b_pub = bob_gamal.get_public()

print("Publics", a_pub, b_pub)

to_encrypt = ecurve.random_point()

print("Encrypting: ", to_encrypt)

encrypted = alice_gamal.encrypt(to_encrypt, b_pub)

print("Encrypted: ", encrypted)

decrypted = bob_gamal.decrypt(encrypted)

print("Decrypted: ", decrypted)