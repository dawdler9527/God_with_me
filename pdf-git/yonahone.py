#!/usr/bin/python
# -*- coding: utf-8 -*-


import re

#from peepdf.PDFCore import PDFParser
from peepdf.PDFCore import *

file = r"F:/PDFdata/data2000/pdf/关于证券公司托管证券投资基金所涉及的场内结算业务有关事项的通知.pdf"
#file = r"/home/yonah/PDFdata/malPDF/VirusShare_ffc1941e3eb5c85cabf6eea94d742b0e"
#file = r"/home/yonah/PDFdata/pdfnormal/SQL_tutorial_pt1.pdf"



# bool change to string
def bool_change(vlue):
    if vlue == True:
        return 0
    else:
        return 1


def None_int(vlue):
    if vlue == None:
        return 0
    else:
        return int(vlue[0])

def None_len(vlue):
    if vlue == None:
        return 0
    else:
        return len(vlue)

def None_vlue(vlue):
    if vlue == None:
        return 0
    else:
        return vlue

#判断是否为PDF文件
def feature_extract(froot): #对输入文件进行特征提取
    '''***********************'''
    feature = dict()
    f_id = []
    pdfParser = PDFParser()
    _, pdf = pdfParser.parse(froot)
    statsDict = pdf.getStats()

    XrefSection = pdf.getXrefSection()
    ti = pdf.getTrailer()
    Header = pdf.getHeaderOffset()
    getVarContent()
    PDFBody.containsXrefStreams(pdf)


    Metadata = pdf.getBasicMetadata(0)
    print len(Metadata)
    feature['Metadata_len'] =len(Metadata)
    meta_K =[]
    for k in Metadata:
        meta_K.append(k)
    #feature['creator_len'] = len(Metadata['creator'])
    #feature['creation_len'] = len(Metadata['creation'])
    #feature['producer_len'] = len(Metadata['producer'])
    #feature['author_len'] = len(Metadata['author'])



    gtree = pdf.getTree()
    font_count = 0
    Javascript_count = 0
    JS_count = 0
    acd = gtree[len(gtree)-1][1]
    for k in acd:
        if '/Font'== acd[k][0]:
            font_count += 1
        if '/JavaScript'== acd[k][0]:
            Javascript_count += 1
        if '/JS' == acd[k][0]:
            JS_count += 1
    feature['font_count'] = font_count
    feature['Javascript_count'] = Javascript_count
    feature['JS_count'] = JS_count



    JavascriptCode= pdf.getJavascriptCode()
    Offsets = pdf.getOffsets()
    Catalog = pdf.getCatalogObjectId()



    feature['JS_MODULE'] = bool_change(JS_MODULE)
    #feature['MAL_ALL']= MAL_ALL
    #feature['MAL_BAD_HEAD'] = MAL_BAD_HEAD
    #feature['MAL_EOBJ'] = MAL_EOBJ
    #feature['MAL_ESTREAM'] = MAL_ESTREAM
    #feature['MAL_HEAD'] = MAL_HEAD
    #feature['MAL_XREF'] = MAL_XREF




    for version in range(len(statsDict['Versions'])):
        statsVersion = statsDict['Versions'][version]
        obj = []
        obj_size = []

        for ob in statsVersion['Objects'][1]:
            obj_one = pdf.getObject(ob).getValue()
            obj.append(obj_one)
            obj_size.append(len(obj_one))

        obj_size.sort(cmp=None, key=None, reverse=True);  # 对这个存有10个最大值数组（TopK数组）进行降序排序
        if len(obj_size) >= 10:
            for h in range(10):
                feature['obj_10_' + str(h)] = obj_size[h]
        else:
            while 10-len(obj_size)> 0:
                obj_size.append(0)
            for h in range(10):
                feature['obj_10_' + str(h)] = obj_size[h]

        feature['Catalog'] = None_vlue(statsVersion['Catalog'])
        feature['Xref Streams'] = None_int(statsVersion['Xref Streams'])
        feature['elements'] = None_len(statsVersion['Elements'])
        feature['Events_num'] = None_len(statsVersion['Events'])

        feature['Actions_num'] = None_len(statsVersion['Actions'])

        feature['Vulns'] = None_len(statsVersion['Vulns'])
        feature['Encoded_num'] = None_int(statsVersion['Encoded'])
        feature['Objects_JS_num'] = None_int(statsVersion['Objects with JS code'])
        feature['Compressd_obj'] = None_int(statsVersion['Compressed Objects'])
        feature['Xref Streams'] = None_int(statsVersion['Xref Streams'])
        feature['Info'] = None_int(statsVersion['Info'])
        feature['Object Streams'] = None_int(statsVersion['Object Streams'])
        #feature['Decoding Errors'] = None_int(statsVersion['Decoding Errors'])


    feature['Binary'] = bool_change(statsDict['Binary'])
    feature['Linearized'] = bool_change(statsDict['Linearized'])
    feature['Encrypted'] = bool_change(statsDict['Encrypted'])
    feature['Metadata'] = None_len(pdf.getMetadata())
    feature['version'] = pdf.version
    feature['stream_num'] = pdf.numStreams
    feature['file_size'] = pdf.getSize()
    feature['object_num'] = pdf.numObjects
    feature['update'] = pdf.getNumUpdates()
    feature['comments'] = len(pdf.comments)
    feature['error'] = len(pdf.errors)
    feature['len_URLs'] = len(pdf.getURLs())
    #feature['Catalog'] = pdf.getCatalogObjectId()

    '''sha1 = pdf.getSHA1()
    for h in range(len(sha1)):
        feature['sha1_' + str(h)] = int(sha1[h], 16)'''
    for i in feature:
        f_id.append(i)

    #test
    for k in feature:
        print(k,feature[k])
    #print('fileneme: %s'%name)
    print len(feature)

    return [feature[k] for k in feature],f_id



if __name__ == '__main__':
    feature_extract(file)

