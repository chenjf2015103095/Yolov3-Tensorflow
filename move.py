# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author :       陈剑锋
   Date：         2019-07-16 下午6:22
   Description :  Dream it possible!
   
-------------------------------------------------
   Change Activity:

-------------------------------------------------
"""
# import os
# import shutil
# name_list=[]
# dst_path='/media/ubutnu/fc1a3be7-9b03-427e-9cc9-c4b242cefbff/YOLOv3/data/VOCdevkit/VOC2012/Annotations'
# for roots,dirs,files in os.walk('/media/ubutnu/fc1a3be7-9b03-427e-9cc9-c4b242cefbff/YOLOv3/data/VOCdevkit/VOC2012/JPEGImages'):
#     for file in files:
#         if file.endswith('.xml'):
#             xml_path=os.path.join(roots,file)
#             print(xml_path)
#             shutil.move(xml_path,dst_path)

            # name=file.split(' ')
            # # print(type(name))
            # for names in name:
            #     if not names.endswith('.xml'):
            #         print(names)








import os
import random
trainval_percent = 0.7
train_percent = 0.8
xmlfilepath = './data/VOCdevkit/VOC2012/Annotations/'
txtsavepath = './data/VOCdevkit/VOC2012/ImageSets/Main'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num*trainval_percent)
tr = int(tv*train_percent)
trainval = random.sample(list,tv)
train = random.sample(trainval,tr)

ftrainval = open(txtsavepath+'/trainval.txt', 'w')
ftest = open(txtsavepath+'/test.txt', 'w')
ftrain = open(txtsavepath+'/train.txt', 'w')
fval = open(txtsavepath+'/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4]+'\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest .close()
print('Well Done！！！')
