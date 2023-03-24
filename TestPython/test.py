# import re

# with open('bible.txt', 'r', encoding='utf-8') as f:
#     text = f.read()

# pattern = r"\b[창]\d+:\d+\b"
# result = re.findall(pattern, text)

# for r in result:
#     print(r)


# #구문 검색 코드 (챕터장절 -> 본문)
# import re

# with open('bible.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
    
# pattern = r"출1:3\s+(.*)"
# result = re.search(pattern, text)

# if result:
#     print(result.group(0))

# #구문 검색 코드 (본문 -> 챕터장절)
# import re

# with open('bible.txt', 'r', encoding='utf-8') as f:
#     text = f.read()

# pattern = r"(.*)너희(.*)"
# result = re.search(pattern, text)

# if result:
#     print(result.group(0))


import re

with open('bible.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 줄바꿈 공백문자로 치환
text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text) 
# 연속된 공백문자 하나만 출력
text = re.sub(r' +', ' ', text)
# 절 줄바꿈
new_text = re.sub(r'(?<=\d):', '\n', text)
new_text = re.sub(r'(?<=\d)\s', '\n', new_text)

with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(new_text)