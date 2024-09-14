import os 

os.chdir("github.com/asphrix/bookbot")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    def get_num_words(text):
        words = text.split()
        return len(words)
    
    def char_count(w):
        characters = {}
        for word in w:
            for s in word:
                lowercase = s.lower()
                try:
                    characters[lowercase] += 1
                except:
                    characters[lowercase] = 1
        
        return characters
    
    word_count = get_num_words(file_contents)
    words = file_contents.split()
    
    character_counts = char_count(words)

    char_list = []

    # Converting dictionary to list of dictionaries
    for character in character_counts:
        if character.isalpha():
            dictionary = {"Char name":character, "Count":character_counts[character]}
            char_list.append(dictionary)

    def sort_on(dict):
        return dict["Count"]
    
    char_list.sort(reverse=True, key=sort_on)

    def book_report():
        print(f"{word_count} words found in the document")
        for c in char_list:
            char = c['Char name']
            count = c['Count']
            print(f"The '{char}' character was found {count} times")

    book_report()
    

            




if __name__ == "__main__":
    main()