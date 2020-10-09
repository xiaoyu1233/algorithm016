import os
import cv2 as cv
import xml.etree.ElementTree as ET

def xml_to_jpg(imgs_path, xmls_path, out_path):
    imgs_list = os.listdir(imgs_path)  #读取图片列表
    xmls_list = os.listdir(xmls_path)  # 读取xml列表
    print(xmls_list)
    if len(imgs_list) <= len(xmls_list):  #若图片个数小于或等于xml个数，从图片里面找与xml匹配的
        for imgName in imgs_list:
            print('xml_path')
            temp1 = imgName.split('.')[0]   #图片名 例如123.jpg 分割之后 temp1 = 123
            temp1_ = imgName.split('.')[1]  #图片后缀
            if temp1_!='jpg' and temp1_ !='bmp':
                continue
            for xmlName in xmls_list:       #遍历xml列表，

                temp2 = xmlName.split('.')[0]  #xml名
                temp2_ = xmlName.split('.')[1]
                if temp2_ != 'xml':

                    continue
                if temp2!=temp1:   #判断图片名与xml名是否相同，不同的话跳过下面的步骤 继续找

                    continue
                else:              #相同的话 开始读取xml坐标信息，并在对应的图片上画框
                    img_path = os.path.join(imgs_path, imgName)
                    xml_path = os.path.join(xmls_path, xmlName)
                    print(xml_path)
                    img = cv.imread(img_path)
                    labelled = img
                    root = ET.parse(xml_path).getroot()
                    for obj in root.iter('object'):
                        bbox = obj.find('bndbox')
                        xmin = int(bbox.find('xmin').text.strip())
                        ymin = int(bbox.find('ymin').text.strip())
                        xmax = int(bbox.find('xmax').text.strip())
                        ymax = int(bbox.find('ymax').text.strip())
                        labelled = cv.rectangle(labelled, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
                    cv.imwrite(out_path + '\\' +imgName, labelled)
                    break
    else:  # 若xml个数小于图片个数，从xml里面找与图片匹配的。下面操作与上面差不多
        for xmlName in xmls_list:
            temp1 = xmlName.split('.')[0]
            temp1_ = xmlName.split('.')[1]
            if temp1_ != 'xml':
                continue
            for imgName in imgs_list:
                temp2 = imgName.split('.')[0]
                temp2_ = imgName.split('.')[1]  # 图片后缀
                if temp2_ != 'jpg' and temp2_ != 'bmp':
                    continue
                if temp2 != temp1:
                    continue
                else:
                    img_path = os.path.join(imgs_path, imgName)
                    xml_path = os.path.join(xmls_path, xmlName)
                    img = cv.imread(img_path)
                    labelled = img
                    root = ET.parse(xml_path).getroot()

                    for obj in root.iter('object'):
                        bbox = obj.find('bndbox')
                        xmin = int(bbox.find('xmin').text.strip())
                        ymin = int(bbox.find('ymin').text.strip())
                        xmax = int(bbox.find('xmax').text.strip())
                        ymax = int(bbox.find('ymax').text.strip())
                        labelled = cv.rectangle(labelled, (xmin, ymin), (xmax, ymax), (0, 0, 255), 1)
                    cv.imwrite(out_path + '\\' +imgName, labelled)
                    break
if __name__ == '__main__':
	# 使用英文路径，中文路径读不进来
    imgs_path = r'D:\AleetcodeOn\algorithm016\Week_03\test\img'  #图片路径
    xmls_path = r'D:\AleetcodeOn\algorithm016\Week_03\test\xml' #xml路径
    retangele_img_path = r'D:\AleetcodeOn\algorithm016\Week_03\test\after_xml' #保存画框后图片的路径
    xml_to_jpg(imgs_path, xmls_path, retangele_img_path)
