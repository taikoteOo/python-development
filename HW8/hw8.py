poem = open('poem.txt','r',encoding='utf-8')
my_text = poem.read()

# 1. Кол-во символов в тексте
def sym_count(text: str) -> str:
    symb_count = len(text)
    return f'1. Всего символов в тексте - {symb_count}'

# 2. Кол-во букв в тексте
def let_count(text: str) -> str:
    symbols = '.,: \n'
    for sym in symbols:
        text = text.replace(sym,'')
    lets_count = len(text)
    return f'2. Букв в тексте - {lets_count}'

# 3. Кол-во строк в тексте
def str_count(text: str) -> str:
    text_list = text.split('\n')
    strs_count = len(text_list)
    return f'3. Всего строк в тексте - {strs_count}'

# Промежуточная функция, убирающая лишние пустые элементы списка
def space_del(list1: list) -> list:
    out_index = []
    for i in range(len(list1)):
        if list1[i] == '':
            out_index.append(i)
    out_index.reverse()
    for index in out_index:
        list1.pop(index)
    return list1

# 4. Кол-во не пустых строк в тексте
def not_empty_str_count(text: str) -> str:
    text_list = text.split('\n')
    space_del(text_list)
    strs_count = len(text_list)
    return f'4. Непустых строк в тексте - {strs_count}'

# 5. Кол-во слов в тексте
def word_count(text: str) -> str:
    text = text.replace('\n', ' ')
    text_list = text.split(' ')
    space_del(text_list)
    words_count = len(text_list)
    return f'5. Всего слов в тексте - {words_count}'

# 6. Кол-во слов в каждой строке
def str_word_count(text: str) -> str:
    text_list = text.split('\n')
    space_del(text_list)
    str_word = []
    for i in range(len(text_list)):
        str_list = text_list[i].split()
        str_word.append(f'{i+1} строка - {len(str_list)} слов')
    result = '\n'.join(str_word)
    return f'6. Анализ слов по строкам:\n{result}'

# 7. Кол-во символов в каждой строке
def str_sym_count(text: str) -> str:
    text_list = text.split('\n')
    space_del(text_list)
    str_sym = []
    for i in range(len(text_list)):
        str_sym.append(f'{i + 1} строка - {len(text_list[i])} символов')
    result = '\n'.join(str_sym)
    return f'7. Анализ символов по строкам:\n{result}'

# 8. Повторяющиеся слова
def repeat_word(text: str) -> str:
    text = text.replace('\n', ' ')
    symbols = '.,:'
    for sym in symbols:
        text = text.replace(sym, '')
    text = text.lower()
    text_list = text.split(' ')
    space_del(text_list)
    count_word = {}
    count_word_list = []
    for word in text_list:
        words_count = text_list.count(word)
        if words_count > 1:
            count_word[word] = words_count
    for key in count_word:
        count_word_list.append(f'{key} - {count_word[key]}')
    result = '\n'.join(count_word_list)
    return f'8. Повторяющиеся слова:\n{result}'

# 9. Частотный анализ текста
def repeat_let(text: str) -> str:
    symbols = '.,: \n'
    for sym in symbols:
        text = text.replace(sym, '')
    text = text.lower()
    text_list = list(text)
    count_let = {}
    count_let_list = []
    for let in text_list:
        lets_count = text_list.count(let)
        count_let[let] = lets_count
    for key in count_let:
        count_let_list.append(f'{key} - {count_let[key]}')
    result = '\n'.join(count_let_list)
    return f'9. Частотный анализ текста:\n{result}'

# 10. Прочие символы
def extra_sym(text: str) -> str:
    text_list = list(text)
    symbols = '.,: \n'
    extra_sym_count = {}
    symbol_count = []
    for sym in symbols:
        count = text_list.count(sym)
        if sym == ' ':
            sym = 'пробелов'
        if sym == '\n':
            sym = 'переносов строки'
        extra_sym_count[sym] = count
    for key in extra_sym_count:
        symbol_count.append(f'{key} - {extra_sym_count[key]}')
    result = '\n'.join(symbol_count)
    return f'10. Прочие символы:\n{result}'

with open('result.txt','w',encoding='utf-8') as result_file:
    result_file.write(sym_count(my_text)+'\n')
    result_file.write(let_count(my_text) + '\n')
    result_file.write(str_count(my_text) + '\n')
    result_file.write(not_empty_str_count(my_text) + '\n')
    result_file.write(word_count(my_text) + '\n')
    result_file.write(str_word_count(my_text) + '\n')
    result_file.write(str_sym_count(my_text) + '\n')
    result_file.write(repeat_word(my_text) + '\n')
    result_file.write(repeat_let(my_text) + '\n')
    result_file.write(extra_sym(my_text))

poem.close()