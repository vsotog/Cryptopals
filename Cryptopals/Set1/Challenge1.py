import base64
import binascii


#Initial value and expected output
h = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
solution = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'


#Convert from HEX to BINARY and then BINARY to BASE64
def hexToBase64(string):
	decoded = binascii.unhexlify(string)
	return base64.b64encode(decoded)

proposal = hexToBase64(h)

#Check if the method used works
if (proposal == solution):
	print ("Success!")
else:
	print("Nope")


