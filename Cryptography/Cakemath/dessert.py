import random,math,os
from Crypto.Util.number import *

flag = os.getenv("NCW_FLAG")
c_n1 = random.getrandbits(512)
c_n2 = random.getrandbits(512)

assert c_n1 != c_n2
encrypted = []
bittersweet = [int(r) for r in "{:b}".format(bytes_to_long(flag))]
for sugar in bittersweet:
	while True:
		gc_c = random.randint(65536, c_n1)
		if math.gcd(gc_c, c_n1) == 1:
			encrypted.append((pow(c_n2,sugar)*pow(gc_c,2)) % c_n1)
			break

print("c_n1 =",str(c_n1))
print("c_n2 =",str(c_n2))
print("encrypted = ", end='')
print(encrypted)