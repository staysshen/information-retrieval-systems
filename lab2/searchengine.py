import sys
import os
import docworks

import inverted

foldername = False
if len(sys.argv) > 1 and sys.argv[1]:
  foldername = sys.argv[1]

searchmode = False
if len(sys.argv) > 2 and sys.argv[2]:
  if sys.argv[2] == "-s":
    searchmode = True

path = ''
filenames = []    # list of strings / files
index = {}        # dict mutable result, inverted append, empty
file_titles = {}  # dict mutable titles of docs key pair, empty
if foldername:
  path = "./" + foldername
  for file in os.listdir(path):
    if file.endswith(".txt"):
      file_path = f"{path}/{file}"
      filenames.append(file_path)

  docworks.create_index(filenames, index, file_titles)
  inverted.print_dict(index)
  print(file_titles)

query = ''
query_res = []
if searchmode:
  query = input("Query (empty query to stop): ")
  if query != "\n":
    query_res = inverted.search(index, query)
    if len(query_res) > 0:
      for doc in query_res:
        print(f'Title: "{file_titles[doc]}", File: {doc}')
    else:
      print("None found")