# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 21:41:14 2017

@author: zxwan
"""

from wxpy import *
#import re

bot = Bot()
friends = bot.core.get_friends(update=True)[0:]
total=len(friends[1:])
print "Friends num: "+str(total)

def get_var(var):
    variable=[]
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable

Nickname = get_var("NickName")
Sex = get_var("Sex")
Province = get_var("Province")
City = get_var("City")
Signature = get_var("Signature")

from pandas import DataFrame
data = {"NickName":Nickname,"Sex":Sex,"Province":Province,"City":City,"Signature":Signature}
frame = DataFrame(data)
frame.to_csv('data.csv',index=True,encoding = 'utf_8_sig')

import re
siglist = []
for i in friends:
    sign = i["Signature"].strip().replace("span","").replace("class","").replace("emoji","")
    rep = re.compile("1f\d+\w*|[<>/=]|&amp")
    sign =rep.sub("",sign)
    siglist.append(sign)
    
text = "".join(siglist)

import jieba
wordlist = jieba.cut(text,cut_all=True)
word_space_split = " ".join(wordlist)

import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
import numpy as np
import PIL.Image as Image
coloring = np.array(Image.open("wechat.jpg"))
#my_wordcloud = WordCloud(background_color="white",max_words=500,mask=coloring,max_font_size=100,random_state=100,scale=2,font_path="C:/Windows/Fonts/simhei.ttf").generate(word_space_split)
my_wordcloud = WordCloud(background_color="white",max_words=500,max_font_size=50,min_font_size=5,random_state=25,scale=30,font_path="C:/Windows/Fonts/simhei.ttf").generate(word_space_split)
#image_colors = ImageColorGenerator(coloring)
# plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
fig = plt.gcf()
plt.show()
fig.savefig('result.png',dpi=450)