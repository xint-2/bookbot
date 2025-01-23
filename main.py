   
def sort_on(dict_list):
    return dict_list["num"]

def count_chars(content):
    character_count = dict() # new dict for counting each char
    for i in content: #loop for each letter in string
        character_count[i] = character_count.get(i, 0) + 1
        # takes a given charracter (i) adds it to dictionary
        # adds 1 to the count every time char (i) is repeated


    dict_list = []
    for char, num in character_count.items():
        if char.isalpha():
            dict_list.append({"char": char, "num": num}) 
    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

       
def report(dict_list, words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(len(words))
    for char_dict in dict_list:
        char = char_dict["char"]
        num = char_dict["num"]
        print(f"The '{char}' character was found {num} times")


def main():
    with open("books/frankenstein.txt") as f: #open frankenstein.txt as f
        file_contents = f.read() #new var file content = read book/book.txt
        content = file_contents.lower() # lowercase all letters in text
        char_list = count_chars(content) # pass lowercase text to count_chars func
        words = content.split()
        # char_list = return value provided by count_chars when run
        report(char_list, words)
        



main()



