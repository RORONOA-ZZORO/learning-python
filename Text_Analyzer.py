# ******************Problem Statement*********************
# Write a Python program that takes a piece of text from the user
# (for example, a paragraph or multiple sentences) and then performs several analyses on it,
# such as:
#     Count total words and characters. done
#     Find the most common word(s).
#     Count how many sentences there are.
#     Show how many times each vowel appears.
#     Reverse each word in the text and display the transformed text.



def Text_Input():
    str = input("Enter a string ")
    return str


def How_Many_Words(str):
    no_words = 0
    words    = str.split( )
    for word in words:
        no_words += 1        
        print(word)    
    return no_words

def How_Many_Char(str):
    no_char = 0
    new_str = str.replace(" ","")
    chars   = len(new_str)
    for char in range(chars):
        print(char)
        no_char += 1
    return chars

def How_Many_Sentences(str):
    no_sentence = 0
    


if __name__ == "__main__":
    str = Text_Input()
    words = How_Many_Words(str)
    print(f"Number of words in the string are {words}")
    chars = How_Many_Char(str)
    print(f"Number of chars in the string are {chars}")