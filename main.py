#!/usr/bin/env python3
"""Reading a Comic Book CSV file with Python
   Created by: Clinton Robertson
   Date: 06/09/2021"""

import csv

def comic_file_reader():
  """This function will take user input to search for comics located in brett_comics.txt and print results..if there are any to a txt file"""

  search_for_comic = "y"
  while search_for_comic == "y":
    print("-----Welcome to Learning Python Comics-----")
    search_term = input("Enter a word or name to find a random comic from our inventory\n> ").lower()
    row_num = 1
    with open("brett_comics.txt", "r") as csvfile:
      # for unique file names
      i = 1
      comicfile = csv.reader(csvfile, delimiter=';')
      for row in comicfile:
        heading_one = row[0].lower()
        heading_two = row[2].lower()
        authors = row[5].lower()
        if search_term in heading_one or search_term in heading_two or search_term in authors:
          filename = f"results{i}.txt"
          with open(filename, "a") as finalresults:
            print(f"{row_num}) {heading_one.title()} {heading_two.title()}\nWritten By: {authors.title()}\n", file=finalresults)
            row_num += 1
      i += 1

    if row_num == 1:
      print("I'm sorry no comic in our inventory matched your search term")
    else:
      print("---------------------------------------------------------")
      print("\nDont forget to grab the print out of your random comics from results.txt\n")
    try_again = ""
    while try_again != "y" and try_again != "n" and try_again != "yes" and try_again != "no":
      try_again = input("Would you like to search again?\nYes or No\n> ").lower()
      if try_again == "y" or try_again == "yes":
        search_for_comic = "y"
      elif try_again == "n" or try_again == "no":
          search_for_comic = "n"
          print("-------------------------------------")
          print("Thanks for trying out our comic store")
      else:
        try_again = ""
        print("Please enter yes or no to search again!\n> ")


def main():
  """This function will run all other functions"""
  comic_file_reader()

if __name__ == "__main__":
    main()



