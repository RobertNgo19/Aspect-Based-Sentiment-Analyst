import numpy as np
import pandas as pd


def find_start_end(label):
  start = 0
  end = 0
  lst_start=[]
  lst_end=[]
  for index ,char in enumerate(label):
    if char == "{":
      start = index
      lst_start.append(start)
    elif char == "}":
      end = index
      lst_end.append(end)
  return tuple(zip(lst_start,lst_end))


def Label_str_to_list(label):
  index = tuple(find_start_end(label))
  aspect_temp=[]
  polarity_temp=[]
  for i in index:
    temp = label[i[0]+1:i[1]].replace(" ","").split(",")
    aspect_temp.append(temp[0])
    polarity_temp.append(temp[1])
  return aspect_temp, polarity_temp

def separate_label(labels):
  aspect= []
  polarity = []
  SA = []
  for label in labels:
    temp = Label_str_to_list(label)
    aspect.append(temp[0])
    polarity.append(temp[1])

    sa_temp= []
    for i in range(len(temp[0])):
      sa = "{"+temp[0][i]+", "+temp[1][i]+"}"
      sa_temp.append(sa)
    SA.append(sa_temp)

  return np.array(aspect, dtype=object), np.array(polarity, dtype=object), np.array(SA, dtype=object)

def show_label(list_label, pred_as, pred_pos, pred_neg, pred_neu):
  labels = []
  for index, value in enumerate(pred_as):
    if value == 1:
      label = "{"
      if pred_pos[index] ==1:
        label += str(list_label[index])+", "+"positive"
      elif pred_neg[index] ==1:
        label += str(list_label[index])+", "+"negative"
      elif pred_neu[index] ==1:
        label += str(list_label[index])+", "+"neutral"
      label+="}"
      labels.append(label)
  return labels


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
