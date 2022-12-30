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
