# Instructions
# Run simply with:
# python a2.py
# It will execute all the questions and print the wanted results

# Uses Python 3.8.10

# ==============================================================================
# ElGamal Digital Signature Standard
# ==============================================================================
# ------------------------------------------------------------------------------
# Domain (System) Parameter Generation
# ------------------------------------------------------------------------------
# p: a prime number
# q: a prime factor of (p - 1)
# g: Z_p with order q (smallest positive integer q such that g^q = 1 mod p)
# h: a cryptographic hash function h
# PRNG: A pseudo random number generator
# ------------------------------------------------------------------------------
# Key Pair
# ------------------------------------------------------------------------------
# x: private key, 0 < x < q
# y: public key, g^x mod p
# ------------------------------------------------------------------------------
# Signature Generation
# ------------------------------------------------------------------------------
# Generate k, 0 < k < q, k is obtained from PRNG (changes every time)
# Find r = g^k mod p
# Solve for s in the equation: h(m) = (xr + ks) mod q (signing equation)
# If s = 0, start again with a different random k
# Return Sig(m) = (r, s) (digital signature of the message m)
# ------------------------------------------------------------------------------
# Verification Process
# ------------------------------------------------------------------------------
# Reject the signature if either 0 < r < p or 0 < s < p is not satisfied
# Set u = h(m)s^-1 mod q and v = -rs^-1 mod q
# Compute w = g^uy^v mod p
# Accept the signature if w = r, otherwise reject it
# ------------------------------------------------------------------------------
# ==============================================================================

# ==============================================================================
# Assignment Parameters
# ==============================================================================
print("====================================================================")
print("Assignment Parameters")
print("====================================================================")
print()

p = int("16819938870120985392012908511330240702317396271716022919731854" \
        "54848231010183867243519643163012786421435674358104484724658871" \
        "43222934545154943005714265124445244247988777471773193847131514" \
        "08303074040754323361669655019764351945813446570069156968090556" \
        "8000063025830089599260400096259430726498683087138415465107499")
print("p = " + str(p))
print()

q = 959452661475451209325433595634941112150003865821
print("q = " + str(q))
print()

g = int("94389192776327398589845326980349814526433869093412782345430946" \
        "05920656880400518160085582590614296727187254837587773894987581" \
        "25404332234449684613507894613850437750299639006381231834351335" \
        "37262152973355498432995364505138912569755859623649866375135353" \
        "179362670798771770711847430626954864269888988371113567502852")
print("g = " + str(g))
print()

pk1 = int("493360183248080935347335488404117524857260585278296306689674805" \
          "688547564165674962162949190519101486861866227068697023216644650" \
          "947032473686465068210152903024809904501302806169292269172462551" \
          "470632923017242976806834012586361821855991241311700775484507542" \
          "94083728885075516985144944984920010138492897272069257160")
print("pk1 = " + str(pk1))
print()

sk1 = 432398415306986194693973996870836079581453988813
print("sk1 = " + str(sk1))
print()

sk2 = 165849943586922055423650237226339279137759546603
print("sk2 = " + str(sk2))
print()

sk3 = 627658512551971075308886219669315148725310346887
print("sk3 = " + str(sk3))
print()

amnt = [ 1, 2, 3, 4 ]
for i, amnt_i in enumerate(amnt):
    print("amnt_" + str(i) + " = " + str(amnt_i))
print()

# nonce[1] (nonce_1) and nonce[2] (nonce_2) have yet to be found
nonce = [ None, None, None ]
print("nonce_1 and nonce_2 have yet to be found")
print()

# ==============================================================================
# Square and Multiply Algorithm
# ==============================================================================

# Returns g^x mod n
def square_and_multiply(g, x, n):
    return pow(g, x, n)

# Uses the Key Pair scheme of the ElGamal Digital Signature Standard above
# Returns True if the public key y was indeed formed from the private key x
# Returns False otherwise
def verify_key(x, y):
    # generate public key y from private key x
    generated_y = square_and_multiply(g, x, p)
    return generated_y == y

# Perform the operations asked by question
print("====================================================================")
print("Square and Multiply Algorithm")
print("====================================================================")
print()
if verify_key(sk1, pk1):
    print("pk1 is indeed the public key that was generated from sk1")
else:
    print("pk1 is not the public key that can be generated from sk1")
print()
pk2 = square_and_multiply(g, sk2, p)
print ("pk2 = " + str(pk2))
print()
pk3 = square_and_multiply(g, sk3, p)
print ("pk3 = " + str(pk3))
print()

# ==============================================================================
# SHA3-224 Representation of Integer of Any Length
# ==============================================================================

from hashlib import sha3_224

# Returns the SHA3-224 hash in binary form of the given integer
# Converts int to str starting with 0x representing its
# hexadecimal form with hex()
# Strips 0x with [2:]
# Converts the str representing the number in hexadecimal to
# utf-8 bytes with bytes(, 'utf-8')
# Obtains a str representing the SHA3-224 hash in hexadecimal
# without 0x at the beginning using sha3_224()
# Converts the str representing the hash in hexadecimal to
# an int using int(, 16)
# Converts that int representing the hash to a str representing
# the hash in binary leading with 0b using bin()
# Strips 0b with [2:]
def SHA3_224(given_integer):
    return bin(SHA3_224_int(given_integer))[2:]

# For better performance on Finding and Verifying Nonce 1 and Nonce 2
def SHA3_224_int(given_integer):
    return int(sha3_224(bytes(hex(given_integer)[2:],
        'utf-8')).hexdigest(), 16)

print("====================================================================")
print("SHA3-224 Representation of Integer of Any Length")
print("====================================================================")
print()
ten_hash = SHA3_224(10)
print ("Binary form of the SHA3-224 hash of 10: " + str(ten_hash))
print()
twenty_hash = SHA3_224(20)
print ("Binary form of the SHA3-224 hash of 20: " + str(twenty_hash))
print()
thirty_hash = SHA3_224(30)
print ("Binary form of the SHA3-224 hash of 30: " + str(thirty_hash))
print()

# ==============================================================================
# Standard SHA3-224 (1152-bit input)
# ==============================================================================

# Takes 2 public keys and a given amnt in the form of integers
# Converts them to binary and concatenates them in the same
# order the parameters are passed
# Converts the obtained binary to its representing integer
def generate_message(public_key_1, public_key_2, given_amnt):
    return int(bin(public_key_1)[2:][:399] + bin(public_key_2)[2:][:399] \
        + bin(given_amnt)[2:], 2)

print("====================================================================")
print("Standard SHA3-224 (1152-bit input)")
print("====================================================================")
print()
m1 = generate_message(pk1, pk2, amnt[1])
print ("m1 = " + str(m1))
print()
m2 = generate_message(pk2, pk3, amnt[2])
print ("m2 = " + str(m2))
print()

# ==============================================================================
# DSS Module to Sign Transactions
# ==============================================================================

from random import randint

# Signs a message using a private key using the Signature Generation scheme
# of the ElGamal Digital Signature Standard above
# Returns a tuple (r, s)
def sign_message(message, private_key):
    s = 0
    while s == 0:
        k = randint(1, q - 1)
        r = square_and_multiply(g, k, p)
        hash_of_message = int(SHA3_224(message), 2)
        # h(m) = (xr + ks) mod q (solve for s), where x is the private key
        # ks = (h(m) - xr) mod q
        # s = ((h(m) - xr) * k^-1) mod q
        # We use the property (A * B) mod C = ((A mod C) * (B mod C)) mod C
        # So ((h(m) - xr) * k^-1) mod q
        # = (((h(m) - xr) mod q) * (k^-1 mod q)) mod q
        s = (square_and_multiply(hash_of_message - private_key * r, 1, q) \
            * square_and_multiply(k, -1, q)) % q
    return r, s

# Uses the Verification Process scheme of the ElGamal Digital Signature
# Standard above
# Returns True if the signature (r, s) is accepted
# Returns False if the signature (r, s) is rejected
def verify_signature(r, s, message, public_key):
    if not (r > 0 and r < p) or not (s > 0 and s < p):
        return False
    hash_of_message = int(SHA3_224(message), 2)
    # We use the property (A * B) mod C = ((A mod C) * (B mod C)) mod C
    # So u = (h(m) * s^-1) mod q = ((h(m) mod q) * (s^-1 mod q)) mod q
    u = (square_and_multiply(hash_of_message, 1, q) \
        * square_and_multiply(s, -1, q)) % q
    # We use the property (A * B) mod C = ((A mod C) * (B mod C)) mod C
    # So v = (-r * s^-1) mod q = ((-r mod q) * (s^-1 mod q)) mod q
    v = (square_and_multiply(-r, 1, q) \
        * square_and_multiply(s, -1, q)) % q
    # We use the property (A * B) mod C = ((A mod C) * (B mod C)) mod C
    # So  (g^uy^v) mod p = ((g^u mod p) * (y^v mod p)) mod p
    w = (square_and_multiply(g, u, p) \
        * square_and_multiply(public_key, v, p)) % p
    return w == r


print("====================================================================")
print("DSS Module to Sign Transactions")
print("====================================================================")
print()
r1, s1 = sign_message(m1, sk1)
print ("Sig1 = (" + str(r1) + ", " + str(s1) + ")")
print()
r2, s2 = sign_message(m2, sk2)
print ("Sig2 = (" + str(r2) + ", " + str(s2) + ")")
print()
if verify_signature(r1, s1, m1, pk1):
    print("Sig1 is an accepted signature of m1")
else:
    print("Sig1 is not an accepted signature of m1")
print()

# ==============================================================================
# Find and Verify Nonce 1 and Nonce 2
# ==============================================================================

# Finds the nonce using brute force
def proof_of_work(previous_message, message):
    hash_of_previous_message = SHA3_224_int(previous_message)
    nonce_num_bits = 128
    num_0_leading_bits = 24
    candidate_nonce = 0
    exclusive_maximum_nonce = 2 ** nonce_num_bits
    two_to_128 = 2 ** 128
    two_to_928 = 2 ** 928
    two_to_200 = 2 ** 200
    while candidate_nonce < exclusive_maximum_nonce:
        #print("candidate nonce: " + str(candidate_nonce))
        T = SHA3_224_int(candidate_nonce + message * two_to_128 \
            + hash_of_previous_message * two_to_928)
        if T < two_to_200:
            return candidate_nonce
        candidate_nonce += 1
    # Shouldn't happen but would signify it wasn't able to find the nonce
    return -1

# Returns True if the nonce is accurate and False otherwise
def verify_nonce(previous_message, message, given_nonce):
    hash_of_previous_message = SHA3_224_int(previous_message)
    two_to_128 = 2 ** 128
    two_to_928 = 2 ** 928
    two_to_200 = 2 ** 200
    T = SHA3_224_int(given_nonce + message * two_to_128 \
            + hash_of_previous_message * two_to_928)
    return T < two_to_200

print("====================================================================")
print("Find and Verify Nonce 1 and Nonce 2")
print("====================================================================")
print()  
print("Please wait for at least 5 minutes")
print()
nonce[1] = proof_of_work(amnt[0], m1)
print("nonce_1 = " + str(nonce[1]))
print()
if (verify_nonce(amnt[0], m1, nonce[1])):
    print("nonce_1 is accurate")
else:
    print("nonce_1 is not accurate")
print()
nonce[2] = proof_of_work(m1, m2)
print("nonce_2 = " + str(nonce[2]))
print()
if (verify_nonce(m1, m2, nonce[2])):
    print("nonce_2 is accurate")
else:
    print("nonce_2 is not accurate")
print()