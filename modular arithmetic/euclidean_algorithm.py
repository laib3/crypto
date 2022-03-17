# Simple implementation of the Euclidean Algorithm 
# as described in "Understanding Cryptography" by Christof Paar

def gcd(r0, r1):
    # gcd(r0, r1) = gcd(r1, r0 mod r1) = ... = gcd(rl, 0) = rl
    while r1 != 0:
        rtmp = r0 % r1
        r0 = r1
        r1 = rtmp
    return r0
