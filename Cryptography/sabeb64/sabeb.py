import binascii
import random

charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
charset2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generateSecret():
	secret = "".join(random.choices(charset2, k=30))
	return secret.encode()

def sabebencode(text):
    ####################################
    ####################################
    ####################################
    ##ceritanya ini rusak kesiram kopi##
    ####################################
    ####################################
    ####################################

if __name__ == '__main__':
	print('Hi! I am Decoda, your personal base64 encoder 0_0')
	print('People said my calculations a little bit something... dunno. But, i\'ll do my best 0_0')
	print("My boss said bruteforce isn't needed, so you're only given 10 chances to use the encoder")
	print('====================================================')
	print('Please make a choice from the options below:')
	count = 0
	secret = generateSecret()
	while True:
		if count == 10:
			print("You've reached your limit")
			print("Thank you and have a good time! ^_^")
			break
		print(f"Encode remaining: {10 - count}")
		print('1. Print encoded secret')
		print('2. Encode plaintext')
		print('3. Submit secret and get flag')
		inputan = input('>> ')
		if inputan == '1':
			print('Here\'s your encoded secret sir:')
			res = sabebencode(secret)
			print(res)
			print('')
			print('Anything else? 0_0')
		elif inputan =='2':
			print('Please input your plaintext in hex 0_0.')
			text = input('>>')
			try:
				text = binascii.unhexlify(text)
				res = sabebencode(text)
				print('Beep boop... here\'s the result sir:')
				print(res)
				print('')
				print('Anything else? 0_0')
				count+=1
			except:
				print('Sorry sir... weird input detected 0_0\n')
		elif inputan == '3':
			print("Please submit the administrator's secret")
			secretsubmit = input('>>').encode()
			try:
				if secretsubmit == secret:
					flag = 'REDACTED'
					print(f"Welcome back, admin. Here's your flag: {flag}\n")
				else:
					print("Wrong secret! You are not admin >:[\n");
			except:
				print('Sorry sir... weird input detected 0_0\n')
		else:
			print('Sorry sir... weird input detected 0_0\n')
