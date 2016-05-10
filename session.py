from bs4 import BeautifulSoup as bs
import requests
from datetime import date, datetime
import csv
import re

from .local_settings import loginfields

class Session(requests.Session):
	def __init__(self):
		super().__init__()
		r = self.get('https://secure2.convio.net/comcau/admin/AdminLogin')
		soup = bs(r.text,'lxml')
		inputs = soup.find_all('input')
		
		logindict = {}
		for input in inputs:
			for field in loginfields.keys():
				if field.lower() in input['name'].lower():
					logindict[field] = input['name']

		payload = {}
				
		for field in loginfields.keys():
			payload[logindict[field]] = loginfields[field]
			
		r = self.post('https://secure2.convio.net/comcau/admin/AdminLogin',data=payload)

class ConvioError(Exception):
	def __init__(self,msg):
		self.msg = msg

		