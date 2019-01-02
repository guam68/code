import ast




with open('card_list.txt', 'r', encoding='utf-8') as file:
    text = ast.literal_eval(file.read())


mavericks = []
for i in range(len(text)):
    if text[i]['is_maverick']:
        mavericks.append((text[i]['card_title'], text[i]['house']))


print(sorted(mavericks))
print(len(mavericks))