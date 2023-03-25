import numpy as np
import pandas as pd
"""
  
  
"""

def start_end_Label(str):
  start = 0
  end = 0
  lst_start=[]
  lst_end=[]
  for i ,v in enumerate(str):
    if v == "{":
      start = i
      lst_start.append(start)
    elif v == "}":
      end = i
      lst_end.append(end)
  return tuple(zip(lst_start,lst_end))


def Label_str_to_list(str):
  index = tuple(start_end_Label(str))
  aspect_temp=[]
  polarity_temp=[]
  for i in index:
    temp = str[i[0]+1:i[1]].replace(" ","").split(",")
    aspect_temp.append(temp[0])
    polarity_temp.append(temp[1])
  return aspect_temp, polarity_temp

def separate_label(list):
  aspect= []
  polarity = []
  SA = []
  for i in list:
    temp = Label_str_to_list(i)
    aspect.append(temp[0])
    polarity.append(temp[1])

    sa_temp= []
    for j in range(len(temp[0])):
      sa = "{"+temp[0][j]+", "+temp[1][j]+"}"
      sa_temp.append(sa)
    SA.append(sa_temp)

  return np.array(aspect, dtype=object), np.array(polarity, dtype=object), np.array(SA, dtype=object)


def create_label_dataframe(labels,list_label_aspect,transform_label_aspect):
    aspect, polarity,_ = separate_label(labels)
    aspect_tf = transform_label_aspect.transform(aspect)
    for index1,label in enumerate(aspect_tf):
        count = 0
        for index2,a in enumerate(label):
            if a == 1:
                if polarity[index1][count] == "positive":
                    aspect_tf[index1][index2] = 1
                elif polarity[index1][count] == "negative":
                    aspect_tf[index1][index2] = 2
                else:
                    aspect_tf[index1][index2] = 3
                count+=1
    aspect_tf = pd.DataFrame(aspect_tf)
    aspect_tf.columns = list_label_aspect
    return aspect_tf

def get_aspect_data_frame(labels,list_label_aspect,transform_label_aspect):
    df_ = create_label_dataframe(labels,list_label_aspect,transform_label_aspect)
    for aspect in list_label_aspect:
        df_[aspect]=df_[aspect].replace(1,1)
        df_[aspect]=df_[aspect].replace(2,1)
        df_[aspect]=df_[aspect].replace(3,1)
    df_ = df_.fillna(0)
    return df_

def get_positive_data_frame(labels,list_label_aspect,transform_label_aspect):
    df_ = create_label_dataframe(labels,list_label_aspect,transform_label_aspect)
    for aspect in list_label_aspect:
        df_[aspect]=df_[aspect].replace(1,1)
        df_[aspect]=df_[aspect].replace(2,0)
        df_[aspect]=df_[aspect].replace(3,0)
    df_ = df_.fillna(0)
    return df_

def get_negative_data_frame(labels,list_label_aspect,transform_label_aspect):
    df_ = create_label_dataframe(labels,list_label_aspect,transform_label_aspect)
    for aspect in list_label_aspect:
        df_[aspect]=df_[aspect].replace(1,0)
        df_[aspect]=df_[aspect].replace(2,1)
        df_[aspect]=df_[aspect].replace(3,0)
    df_ = df_.fillna(0)
    return df_

def get_neutral_data_frame(labels,list_label_aspect,transform_label_aspect):
    df_ = create_label_dataframe(labels,list_label_aspect,transform_label_aspect)
    for aspect in list_label_aspect:
        df_[aspect]=df_[aspect].replace(1,0)
        df_[aspect]=df_[aspect].replace(2,0)
        df_[aspect]=df_[aspect].replace(3,1)
    df_ = df_.fillna(0)
    return df_
  
a = ['Ga giường không sạch, nhân viên quên dọn phòng một ngày.{ROOM_AMENITIES#CLEANLINESS, negative}, {SERVICE#GENERAL, negative},{HOTEL#DESIGN&FEATURES, positive}','Địa điểm thuận tiện, trong vòng bán kính 1,5km nhiều quán ăn ngon{LOCATION#GENERAL, positive}']
print(separate_label(a))
