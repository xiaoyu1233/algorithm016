import os;

imgs_path = r'F:\AdatabaseForGraduation\img\fiber'  # 图片路径
xmls_path = r'F:\AdatabaseForGraduation\voc\fiber_voc'  # xml路径
retangele_img_path = r'F:\AdatabaseForGraduation\img_after\fiber_after'  # 保存画框后图片的路径
imgs_list = os.listdir(imgs_path)  # 读取图片列表
xmls_list = os.listdir(xmls_path)  # 读取xml列表

count = 0
for imgName in imgs_list:
    #print('xml_path')
    temp1 = imgName.split('.')[0]  # 图片名 例如123.jpg 分割之后 temp1 = 123
    temp1_ = imgName.split('.')[1]  # 图片后缀

    print("AAA",temp1)
    if temp1_ != 'jpg' and temp1_ != 'bmp':
        print("CC",temp1_)
        continue
    for xmlName in xmls_list:  # 遍历xml列表，

        temp2 = xmlName.split('.')[0]  # xml名
        temp2_ = xmlName.split('.')[1]
        print("BBB", temp2)
        if temp1 == temp2:
            break



        if temp1 == temp2:
            count += 1
            print(count)