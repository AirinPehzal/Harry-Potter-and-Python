import re
textnew = open("textnew.txt", "w")  # Заменяем ! из первого во второй файл
with open("text.txt", "r") as text:
    for line in text:
        textnew.write(re.sub(r'!', '.', line))
textnew.close()
text = open("text.txt", "w")  # Заменяем ? из второго в первый файл
with open("textnew.txt", "r") as textnew:
    for line in textnew:
        text.write(re.sub(r'\?', '.', line))
text.close()
textnew = open("textnew.txt", "w")  # Переносим содержимое во второй файл без абзацев
with open("text.txt", "r") as text:
    for line in text:
        textnew.write(re.sub(r'\n', ' ', line))
textnew.close()
text = open("text.txt", "w")  # Переносим содержимое в первый файл построчно
with open("textnew.txt", "r") as textnew:
    for line in textnew:
        text.write(re.sub(r'\.', '.\n', line))
text.close()
textnew = open("textnew.txt", "w")  # Проставляем номера
i = 1
with open("text.txt", "r") as text:
    for line in text:
        textnew.write(str(i)+') '+line)
        i = i+1
textnew.close()
