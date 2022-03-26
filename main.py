
##### A

def read_line(n, file):

    # בודק האם הקלט חוקי
    if type(n) != int:
        return "invalid input detected"

    #בודק האם הקובץ עם השם שקיבלנו בקלט קיים
    try:
        f = open(file)   #מנסה להשתמש (לפתוח) את הקובץ
    except:
        return "file not found"

    # בודק האם מספר השורה נמצא בקובץ
    list_lines = f.readlines()
    if n not in range(1, len(list_lines)+1):
        return "line " + str(n) + " doesn't exist"


    #בודק האם התו האחרון הוא ירידת שורה
    if '\n' == list_lines[n-1][-1:]:
        list_lines[n-1] = list_lines[n-1][:-1]

    f.close()

    return list_lines[n-1]


'''
file1 = "ex3_text.txt"
print(read_line(3, file1))
assert read_line(1, file1) == "B L A C K    H O L E S    I N    S P A C E"
assert read_line(3, file1) == " "
# assert read_line(4, file1) == " There is much more to black holes than meets the eye. In fact,"
assert read_line(9, file1) == " "
assert read_line(29, file1) == "line 29 doesn't exist"
assert read_line(-1, file1) == "line -1 doesn't exist"
assert read_line(0, file1) == "line 0 doesn't exist" 
assert read_line("c", file1) == "invalid input detected"
assert read_line(1.5, file1) == "invalid input detected"
assert read_line(9, "ex4_text.txt") == "file not found"
assert read_line(29, "ex4_text.txt") == "file not found"
'''

import re

#### B

def longest_words(file):

    # בודק האם הקובץ עם השם שקיבלנו בקלט קיים
    try:
        f = open(file)  # מנסה להשתמש (לפתוח) את הקובץ
    except:
        return "file not found"

    #מפריד את קובץ הטקסט רק לפי מילים
    words = re.split(r"\W+", f.read())
    f.close()

    #מסדר את המילים מהגדול לקטן לפי אורכן
    #לוקח את ה5 הכי גדולות
    sort_words = sorted(words, key=len, reverse=True)[:5]


    return sort_words




'''
print(longest_words("ex3_text.txt"))
assert longest_words("ex4_text.txt") == "file not found"
assert longest_words("ex4_text.txt") == "file not found"
assert longest_words("ex3_text.txt") == \
             ['electromagnetic', 'gravitational', 'Consequently', 'calculations', 'ultraviolet']
'''