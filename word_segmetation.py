import re

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


def word_segmentation(text):
    f = open("160000_ch_dictionary.txt", "r", encoding="utf-8-sig")
    chinese_words = f.read().split("\n")

    split_sentence = re.split(r'[。，!?~:",.@#$%^&*;{}()+=/|\'\s]', text)

    number_with_pos = find_numbers_with_positions(text)
    char_with_pos = find_english_characters_with_positions(text)

    # symbol
    sym = 0
    pos = 0
    ans = ""
    num_dig = 0
    num_char = 0
    for index in range(len(split_sentence)):
        sym += len(split_sentence[index])

        if(split_sentence[index] == ""):
            pass
        else:
            if(split_sentence[index] in chinese_words):
                pos += len(split_sentence[index])
                ans = ans + split_sentence[index] + " "
            else:
                i = len(split_sentence[index])
                while(split_sentence[index] != ""):                    
                    if(number_with_pos != [] or char_with_pos != []):
                        for number, start, end in number_with_pos:
                            if(start == pos):
                                ans += number
                                pos = pos + len(number)
                                split_sentence[index] = split_sentence[index][len(number):]
                                i = len(split_sentence[index])
                                num_dig += 1
                                number_with_pos.pop(0)

                        for char, start, end in char_with_pos:
                            if(start == pos):
                                ans += char
                                pos = pos + len(char)
                                split_sentence[index] = split_sentence[index][len(char):]
                                i = len(split_sentence[index])
                                num_char += 1
                                char_with_pos.pop(0)

                    if(split_sentence[index][:i] in chinese_words):
                        if(num_dig != 0 or num_char != 0):
                            ans += " "
                        ans = ans + split_sentence[index][:i] + " "
                        pos = pos + i
                        split_sentence[index] = split_sentence[index][i:]
                        i = len(split_sentence[index])
                        num_dig = 0
                        num_char = 0    
                    else:
                        i -= 1

        if(sym < len(text)):
            if(text[sym] == " "):
                ans += text[sym]
            else:
                ans = ans + text[sym] + " "
            sym += 1
            pos += 1

    ans_list = ans.split(" ")
    ans_list = [elem for elem in ans_list if elem != '']
    f.close()
    return ans_list

if __name__ == "__main__":
    text = input("請輸入一句話: ")
    words = word_segmentation(text)
    print(words)
