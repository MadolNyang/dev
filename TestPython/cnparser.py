# import re

# with open('bible.txt', 'r', encoding='utf-8') as f:
#     text = f.read()

# hanja_word_list = list(set(re.findall("[\u4e00-\u9fff]+", text)))
# hanja_char_list = list(set("".join(hanja_word_list)))

# print("한자 단어 리스트:", hanja_word_list)
# print("한자 글자 단위 리스트:", hanja_char_list)

# hanja_word_list_org = re.findall("[\u4e00-\u9fff]+", text)

# word_count = {}
# for word in hanja_word_list_org:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# for word, count in sorted_word_count:
#     if count >= 20:
#         print(f"{word}: {count}")

# hanja_char_list_org = "".join(hanja_word_list_org)

# char_count = {}
# for word in hanja_char_list_org:
#     if word in char_count:
#         char_count[word] += 1
#     else:
#         char_count[word] = 1

# sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

# for char, count in sorted_char_count:
#     if count >= 20:
#         print(f"{char}: {count}")


import re

with open('bible.txt', 'r', encoding='utf-8') as f:
    text = f.read()

hanja_word_list = re.findall("[\u4e00-\u9fff]+", text)
hanja_char_list = list(set("".join(hanja_word_list)))

word_count = {}
for word in hanja_word_list:
    if len(word) >= 4:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_word_count:
    print(f"{word}: {count}")