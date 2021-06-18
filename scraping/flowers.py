#!/usr/bin/env python3
"""Gathering Flower names using Beautiful Soup
   Created By: Clint Robertson"""

import requests
from bs4 import BeautifulSoup


def main():
	#Finds all Flower names and adds them to flower dictionary
	
	flower_dictionary = {}
	URL = "https://florgeous.com/types-of-flowers/"
	response = requests.get(URL)
	if response.encoding == "UTF-8":
		data = response.text
		soup = BeautifulSoup(data, 'html.parser')
		for h3 in soup.find_all('h3'):
			flower_name = h3.text
			if "About" not in flower_name:
				flower_dictionary[f"{flower_name}"] = {}

	print(flower_dictionary)			




if __name__ == "__main__":
	main()

