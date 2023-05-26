from Crypto.Util.number import *
import random
import math
m = bytes_to_long(b"REDACTED")

def primevalue(value):
	ind = 0
	while not isPrime(value):
		value += 1
		ind += 1
	print(f"added {ind}")
	return value

def generatePrimes():
	print("generating random numbers...")
	p = random.getrandbits(512)
	q = random.getrandbits(512)
	print("calculating next prime...")
	p = primevalue(p)
	q = primevalue(q)
	print("comparing values...")
	print("=======| > |=======") if p > q else print("=======| < |=======")
	return p, q

while True:
	try:
		print("==================================")
		print("J&M's EncRSAyption MacRSAhine 3000")
		print("==================================")
		print("1. Spill Administrator's message")
		print("2. Encrypt your own message")
		pilihan = input("[?] ")
		if pilihan == "1":
			p, q = generatePrimes()
			e = primevalue(random.randint(3, 100000))
			n = p*q
			c = long_to_bytes(pow(m, e, n))
			print("\nToo bad this part is highly confidential, only the ciphertext are allowed to be displayed.")
			print(f"[>] {c.hex()}\n")
		elif pilihan == "2":
			p, q = generatePrimes()
			n = p * q
			phi  = (p-1)*(q-1)
			print("")
			print("Input plaintext")
			message = bytes_to_long(input("[?] ").encode())
			while True:
				print("Input your exponent")
				e = int(input("[?] "))
				if math.gcd(e, phi) != 1:
					print('Error! exponent and totient have same factor(s)')
				else:
					d = inverse(e, phi)
					print("Imma just show this to you, you already know your own message anyway")
					print(f"d = {d}")
					print("Use this exponent? (Y/N)")
					choice = input("[?] ")
					if choice == "Y" or choice == "y":
						break
					elif choice == "N" or choice == "n":
						pass
			c = pow(message, e, n)
			print("Here's the result:")
			print(f"[>] n = {n}\n[>] e = {e}\n[>] c = {c}\n")
	except:
		print('Error\n')
