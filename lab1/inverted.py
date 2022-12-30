##inverted index class

#result is list of words, and the documents in which they appear. 
# provide the list of words (your search query), and Google produces the documents (search result links).


# takes a list of words
# then searches through every document
# and builds something idk


#Steps to build Inverted index are:
# Fetch the document and gather all the words
# (read document, merge lines, remove punctuation, remove stopwords)

# Check for each word
# - if present - add reference of document to index 
# - else       - create new entry in index for that word.
# Repeat above steps for all documents 
# - and sort the words.



#Word       Documents
#hello        doc1      
#sky          doc1, doc3
#coffee       doc2
#hi           doc2
#greetings    doc3  


import json  
  
class Inverted:
  dict = {}
  
  def append_entry_singular(self, keyword, document):
    if keyword not in self.dict:
      self.dict[keyword] = [document]
    
    elif keyword in self.dict:
      if document not in self.dict[keyword]:
        self.dict[keyword].append(document)
        
  def append_entry(self, document, keywords):
    for key in keywords:
      self.append_entry_singular(key, document)
  
  def print(self):
    print(json.dumps(self.dict, sort_keys=False, indent=2))
  
  def search(self, keyword):
    return self.dict[keyword]
