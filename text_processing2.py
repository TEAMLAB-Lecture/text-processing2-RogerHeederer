#######################
# Test Processing II  #
#######################
import re

def digits_to_words(input_string):
    
    digit_set = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four',
                5:'five', 6:'six', 7:'seven', 8:'eight',9:'nine'}

    digit_string = re.sub('[^0-9]','',input_string) # 숫자를 제외한 캐릭터는 ''로 치환
    convert = ''
    for digit in digit_string:
        convert += digit_set.get(int(digit)) + ' '

    return convert


def to_camel_case(underscore_str):
    parts_num = underscore_str.split("_")
    
    if len(parts_num) == 1: # 언더스코어로 안짤리는 이미 카멜을 만족하는 경우, 특수문자만 구성, 공백 등이 들어오면 리스트 1개로 묶인다.
        return underscore_str
    
    elif not ''.join(underscore_str.split("_")): # 언더스코어로만 구성된 경우, 빈 어레이. # whitespace도 없는 경우
        return ''

    else:
        underscore_str = underscore_str.lower()
        for i in range(0, len(underscore_str) -1):
            if underscore_str[i] == '_' and underscore_str[i+1].isalpha():
                #underscore_str[0] 과 일치하는 캐릭터 전부를 대치시켜버리기 때문에, 1 옵션을 줬다.(한번만 수행~) 해당 인덱스에 해당하는 것만 바꾸기
                underscore_str = underscore_str.replace(underscore_str[i+1], underscore_str[i+1].upper(), 1)
        underscore_str = re.sub('[^a-zA-Z0-9]','',underscore_str)
        underscore_str = underscore_str.replace(underscore_str[0], underscore_str[0].lower(), 1)

        return underscore_str