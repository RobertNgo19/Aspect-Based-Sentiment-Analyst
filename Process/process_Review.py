import emoji
import re
import numpy as np

"""
  - Normalize Text ;) - 

+ lower str : ABC -> abc
+ delete emoji in str: ABC :) - > ABC
+ replace price and distance: 200k and 15km -> gia_tien and khoang_cach
+ delete special characters in str: abc@#$%%@- > abc
+ normalize teencode: ngon quaaaaaa - > ngon qua

"""
def text_Lower(list):
    list_result = list.copy()
    for i in range(len(list_result)):
        list_result[i]=list_result[i].lower()
    return list_result

def del_Emoji(list):
    list_result = list.copy()
    list_result =  np.array([emoji.get_emoji_regexp().sub('', text) for text in list_result])
    return list_result

def rep_PricewDisance(list):
  list_result = []
  for i in list:
    distance_pattern = "([0-9.,]{1,9}?.km)|([0-9.,]{1,9}?.cây số)|([0-9.,]{1,9}?.cây)|([0-9.,]{1,9}?.mét)|([0-9.,]{1,3}?.m)"
    new_text = re.sub(distance_pattern, ' khoang_cach ',i)
    money_pattern = "(\d{1,3}k.{0})|([0-9.]{1,9}?.vnd)|([0-9.]{1,9}?.việt nam đồng)|([0-9.]{1,9}?.đồng)"
    new_text = re.sub(money_pattern, 'gia_tien' ,new_text)
    list_result.append(new_text)
  return list_result

def del_Special_character(list):
  list_result = []
  for i in list:
    special_character_pattern = '[!”"#$%&()•/:;<=>-?@[\]^`{|}~+*_-]'
    new_text = re.sub(special_character_pattern,'', i)
    words = new_text.split()
    new_text = ' '.join(words)
    list_result.append(new_text)
  return list_result

def normalize_Teencode(list):
  list_result = []
  for text in list:
    Teencode_pattern = r"(\w)\1*"
    new_text = re.sub(Teencode_pattern, r'\1', text)
    list_result.append(new_text)
  return list_result


def rep_Acronyms(list):
  list_result = []
  for i in list:
    hotel_pattern = r"\bksạn\b|\bk sạn\b|\bks\b|\bKS\b|\bKs\b"
    new = re.sub(hotel_pattern, 'khách sạn', i)
    new = re.sub(r"\bnc\b", 'nước', new)
    new = re.sub(r"\bnvs\b|\bnhà vs\b", 'nhà vệ sinh', new)
    new = re.sub(r"\bnv\b", 'nhân viên', new)
    new = re.sub(r"\bvs\b", 'vệ sinh', new)
    No_pattern = r"\bkh\b|\bko\b|\bkhg\b|\bkhong\b|\bk\b|\bhông\b|\bhem\b|\bk0\b"
    new = re.sub(No_pattern, 'không', new)
    new = re.sub(r"\bdc\b|\bdk\b", 'được', new)
    new = re.sub(r" 1 ", " một ", new)
    list_result.append(new)
  return list_result
