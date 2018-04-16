#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pandas as pd
import glob

def hebing():
    csv_list = []
    csv_list.append('/home/yonah/God_with_me/2018Q2/MLmodel3/data_set/contogio_ben9K.csv')
    #csv_list.append('/home/yonah/Downloads/mimicus-master/data/virustotal-mal.csv')
    #csv_list.append('/home/yonah/Downloads/mimicus-master/data/contagio.csv')
    #csv_list.append('/home/yonah/Downloads/mimicus-master/data/google-ben.csv')
    #csv_list.append('/home/yonah/Downloads/mimicus-master/data/contagio-nopdfrate.csv')
    csv_list.append('/home/yonah/God_with_me/2018Q2/MLmodel3/data_set/normal_sogpi2K.csv')


    print(u'共发现%s个CSV文件'% len(csv_list))
    print(u'正在处理............')
    for i in csv_list:
        fr = open(i,'r').read()
        with open('merge_benE.csv','a') as f:
            f.write(fr)
    print(u'合并完毕！')

def quchong(file):
    df = pd.read_csv(file,header=0,delimiter="\t")
    datalist = df.drop_duplicates()
    datalist.to_csv(file)

if __name__ == '__main__':
    hebing()
    quchong("merge_benE.csv")

