import sys
from collections import Counter
#to check if the input is valid or not
def validate_input(para):
    if not para.strip():
        print("Error: Paragraph is empty. Please enter valid text.")
        return False
    return True
#to count the number of words in the paragraph
def word_count(para):
    
    word=para.split()
    if(word):
       count=len(word)        
       print(f"Total Words: {count}")
    else:
        print("error*** no word found in the paragraph")  
#to count number of characters with spaces in the paragraph         

def char_count_with_spaces(para):
    if(para):
      a=len(para)
      print(f"Total Characters(with spaces): {a}")
    else:
        print("error no character found in the paragraph ")  

#to count number of spaces in the para without spaces

def char_count_without_spaces(para): 
    if(para):
       a=len(para.replace(" ",""))
       print(f"Total Characters(without spaces): {a}")
    else:
        print("error** no character found in the paragraph")   

#to count number of sentences in the paragraph
def sentence_count(para): 
    if(para):
        a=para.count(".")
        b=para.count("!")
        c=para.count(";")
        count=int(a)+int(b)+int(c)
        print(f"Total Sentences  :{count}")
    else:
        print("error*** no sentence found in the paragraph")    

#to count frequent wordss in the paragraph        

def frequent_words(para):
    l = para.split()
    if(l):
         word_count = Counter(l)
         sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
         print("Frequent Words: ")
         for i,count in sorted_words:
           print(f" -{i} : {count}")
    else:
        print("error*** no frequent word found in the paragraph")       
     
#to check and to display the longest word in the paragraph     

def longest_word(para):
    l = para.split()
    if(l):
       longest=max(l,key=len)
       print(f" Longest Word \n {longest} :{len(longest)}")
    else:
        print("error*** no longest word found in the paragraph")   

#to check and to display common words in the paragraph
def common_word(para):
    l = para.split()
    if(l):
       word_count = Counter(l)
       sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
       print("Common Word:")
       print(sorted_words[0]) 
    else:
        print("error*** no common word found in the paragraph")   

#main to call all the functions

if __name__=='__main__':
    #to enter the paragraph
    print("Enter a paragraph")
    para=sys.stdin.read()
    if not validate_input(para):
        sys.exit(1)
    print("to end paragraph,\n In Windows(press ctrl+Z followed by enter) \n In MacOS\Linux(press ctrl+D) ")
    print(f"your paragraph is : {para}")
    print("TEXT ANALYSIS RESULT")
    print()
    #function calling
    word_count(para)
    char_count_with_spaces(para)
    char_count_without_spaces(para)
    sentence_count(para)
    frequent_words(para) 
    longest_word(para)
    common_word(para)
   