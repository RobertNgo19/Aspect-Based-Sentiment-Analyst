from . import process_Labels as pre_label
from . import process_Review as pre_review


class preProcessing_Label(object):
    def __init__(self, label = " ",
                      list_label_aspect=[],
                      transform_label_aspect=None,
                      aspect = False,
                      positive = False,
                      negative = False,
                      neutral = False):
      self.label = label
      self.list_label_aspect = list_label_aspect
      self.transform_label_aspect = transform_label_aspect
      self.aspect = aspect
      self.positive = positive
      self.negative = negative
      self.neutral = neutral
    
    def make_label_dataframe(self):
      if self.aspect:
        df = pre_label.get_aspect_data_frame(self.label,self.list_label_aspect,self.transform_label_aspect)
      elif self.positive:
        df = pre_label.get_positive_data_frame(self.label,self.list_label_aspect,self.transform_label_aspect)
      elif self.negative:
        df = pre_label.get_negative_data_frame(self.label,self.list_label_aspect,self.transform_label_aspect)
      else:
        df = pre_label.get_neutral_data_frame(self.label,self.list_label_aspect,self.transform_label_aspect)
      return df
    
class preProcessing_Review(object):
  def __init__(self,texts =" ",
                    text_Lower=True, 
                    del_Emoji =True,
                    rep_PricewDisance=True,
                    del_Special_character = True,
                    normalize_Teencode=True,
                    rep_Acronyms=True):
      self.texts = texts
      self.text_Lower = text_Lower
      self.del_Emoji = del_Emoji
      self.rep_PricewDisance = rep_PricewDisance
      self.del_Special_character = del_Special_character
      self.normalize_Teencode = normalize_Teencode
      self.rep_Acronyms = rep_Acronyms

  def process(self):
      result = self.texts
      if self.text_Lower:
        result = pre_review.text_Lower(result)
      if self.del_Emoji:
        result = pre_review.del_Emoji(result)
      if self.rep_PricewDisance:
        result = pre_review.rep_PricewDisance(result)
      if self.del_Special_character:
        result = pre_review.del_Special_character(result)
      if self.normalize_Teencode:
        result = pre_review.normalize_Teencode(result)
      if self.rep_Acronyms:
        result = pre_review.rep_Acronyms(result)
      return result