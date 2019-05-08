import re
from collections import Counter

def create_data_set(input):
    result = []
    for i in range(len(input)):
        text = re.sub('[^a-zA-Z]+', '', input[i:i+2])
        temp = text.replace(" ", "")
        if len(temp) == 2:
            result.append(temp.upper())             
    return Counter(result)


def solution(str1, str2):

    set1 = create_data_set(str1)
    set2 = create_data_set(str2)

    inter = sum((set1& set2).values())
    union = sum((set1|set2).values())

    if inter == 0 and union == 0:
        return 65536
    else:
        return int((inter/union)*65536)
