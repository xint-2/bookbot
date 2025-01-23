   
def sort_on(dict_list): #sort function, input of dict_list
    return dict_list["num"] # returns value of the "num" key in dict_list

def count_chars(content):
    character_count = dict() # new dict for counting each char
    for i in content: #loop for each letter in string
        character_count[i] = character_count.get(i, 0) + 1
        # takes a given charracter (i) adds it to dictionary
        # adds 1 to the count every time char (i) is repeated


    dict_list = []
    for char, num in character_count.items(): #looking for variable char and num in character_count
        if char.isalpha(): #if the character is alpabetical (no $,#,.) -> then
            dict_list.append({"char": char, "num": num}) 
            # takes "char" and "num" keys appends them with char, num vals in dict_list
    dict_list.sort(reverse=True, key=sort_on)
    # sorts dict list by (revese=True) big numbers first
    # (key=sort_on) finds the value pair for the key "num" with sort_on function
    return dict_list
    # takes dictionary and overwrites it with new sorted dictionary
       
def report(dict_list, words): #func takes dictionary and split content file
    print("--- Begin report of books/frankenstein.txt ---")
    print(len(words)) #prints length of split content (words)
    for char_dict in dict_list: #looking for value in dict_list
        char = char_dict["char"] # assigning variable char to "char" value
        num = char_dict["num"] # assigning variable num to "num" value
        print(f"The '{char}' character was found {num} times")


def main():
    with open("books/frankenstein.txt") as f: #open frankenstein.txt as f
        file_contents = f.read() #new var file content = read book/book.txt
        content = file_contents.lower() # lowercase all letters in text
        char_list = count_chars(content) # pass lowercase text to count_chars func
        # char_list = return value provided by count_chars when run
        words = content.split() #splits content into list of individual words
        report(char_list, words)
        # passes (char_list) and (words) variables to report function
        



main()



