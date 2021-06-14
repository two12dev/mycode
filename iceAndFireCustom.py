#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()

        #Set name
        character_name = None
        if got_dj["name"] == "":
            character_name = got_dj["aliases"][0]
        else:
            character_name = got_dj["name"]
        
        #Get houses affiliated with
        affiliations = []
        for house in got_dj["allegiances"]:
            house_resp = requests.get(house)
            house_name = house_resp.json()
            affiliations.append(house_name["name"])
        
        #Get books
        books_char_in = []
        for book in got_dj["books"]:
            book_resp = requests.get(book)
            book_name = book_resp.json()
            books_char_in.append(book_name["name"])

        #Get pov books
        pov_books_char_in = []
        for book in got_dj["povBooks"]:
            book_resp = requests.get(book)
            book_name = book_resp.json()
            pov_books_char_in.append(book_name["name"])
            
        #Print all info found
        print("----------------------------------")
        print(f"Character Name: {character_name}")
        print("House/Houses: ", end="")
        print(*affiliations, sep=", ")
        print("Books appeared in: " ,end="")
        print(*books_char_in, sep=", ")
        print("POV Books appeared in: " ,end="")
        print(*pov_books_char_in, sep=", ")

if __name__ == "__main__":
        main()

