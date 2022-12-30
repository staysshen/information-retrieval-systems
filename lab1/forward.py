##forward index class

##list of documents, and which words appear in them. 
#crawl the folder, build the list of documents, figure out which words appear in each.



# Steps to build Forward index are:
# Fetch the document and gather all the keywords.
# (read document, merge lines, remove punctuation, remove stopwords)

# Append all the keywords in the index entry for this document.
# Repeat above steps for all documents



#Document  Keywords
#doc1       hello, sky, morning      
#doc2       tea, coffee, hi
#doc3       greetings, sky


#takes a document name and array of words and just appends

import json

class Forward:
  dict = {}
  
  def append_entry(self, document, keywords):
    if document not in self.dict:
      self.dict[document] = keywords
      
    elif document in self.dict:
      #add new and remove duplicates
      self.dict[document] += keywords
      self.dict[document] = list(set(self.dict[document]))
    
  def print(self):
    print(json.dumps(self.dict, sort_keys=False, indent=2))
    
  def search(self, keyword):
    pages = []
    for key in self.dict.keys():
      if keyword in self.dict[key]:
        pages.append(key)
    return pages
