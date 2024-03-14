"""First function prints out each word in uppercase"""
def print_upper_words(words):
    for word in words:
        print(word.upper())
        
       
       
     """second function prints out each word in uppercase if it starts with e or E"""  
 def print_upper_words(words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
        print(word.upper())
        
"""third function prints out each word in uppercase if it starts with a letter in the list must_start_with"""
 for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
