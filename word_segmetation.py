import re
import os

def find_numbers_with_positions(sentence):
    numbers_with_positions = []
    for match in re.finditer(r'\d+', sentence):
        number = match.group()
        start_pos = match.start()
        end_pos = match.end()
        numbers_with_positions.append((number, start_pos, end_pos))
    return numbers_with_positions

def find_english_characters_with_positions(sentence):
    characters_with_positions = []
    for match in re.finditer(r'[a-zA-Z]', sentence):
        character = match.group()
        start_pos = match.start()
        end_pos = match.end()
        characters_with_positions.append((character, start_pos, end_pos))
    return characters_with_positions


text = input("請輸入一句話: ")
f = open("160000_ch_dictionary.txt", "r", encoding="utf-8-sig")
chinese_words = f.read().split("\n")

split_sentence = re.split(r'[。，!?\s]', text)
print(split_sentence)

number_with_pos = find_numbers_with_positions(text)
char_with_pos = find_english_characters_with_positions(text)

# symbol
sym = 0
pos = 0
for index in range(len(split_sentence)):
    
    sym += len(split_sentence[index])

    if(split_sentence[index] == ""):
        sym += 1
        pos += 1
        continue
    elif(re.match(r'[a-zA-Z]', split_sentence[index][0])):
        print(split_sentence[index], end=" ")
        pos += len(split_sentence[index])
    else:
        if(split_sentence[index] in chinese_words):
            pos += len(split_sentence[index])
            print(split_sentence[index], end=" ")
        else:
            i = len(split_sentence[index])
            while(split_sentence[index] != ""):
                
                if(number_with_pos != []):
                    for number, start, end in number_with_pos:
                        if(start == pos):
                            print(number, end=" ")
                            pos = pos + len(number)
                            split_sentence[index] = text[end:]
                            i = len(split_sentence[index])
                            number_with_pos.pop(0)
                        break

                if(split_sentence[index][:i] in chinese_words):
                    print(split_sentence[index][:i], end=" ")
                    pos = pos + i
                    split_sentence[index] = split_sentence[index][i:]
                    i = len(split_sentence[index])     
                else:
                    i -= 1

    
    if(sym < len(text)):
        if(text[sym] == " "):
            print(text[sym], end="")
        else:
            print(text[sym], end=" ")
        sym += 1
        pos += 1

f.close()
