import os;
import pypinyin
from pypinyin import pinyin, lazy_pinyin
import re
from zhon.hanzi import punctuation

def lm_find_unchinese(file):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    unchinese = re.sub(pattern,"",file) #排除汉字
    unchinese = re.sub('[{}]'.format(punctuation),"",unchinese) #排除中文符号
    unchinese = unchinese .replace('-','')
    #print("unchinese:",unchinese)
    return unchinese

def rename():
    #path = r"F:\AdatabaseForGraduation\voc\scratch_voc"
    # path = r"F:\AdatabaseForGraduation\voc\fiber_voc"
    #path = r"F:\AdatabaseForGraduation\voc\circle_voc"
    #path = r"F:\AdatabaseForGraduation\img\scratch"
    path = r"F:\AdatabaseForGraduation\img\fiber"
    #path = r"F:\AdatabaseForGraduation\img\circle"

    filelist = os.listdir(path)  # 该文件夹下所有的文件（包括文件夹）

    for files in filelist:  # 遍历所有文件

        Olddir = os.path.join(path, files);  # 原来的文件路径

        if os.path.isdir(Olddir):  # 如果是文件夹则跳过

            continue;

        filename = os.path.splitext(files)[0];  # 获取文件名
        name20=lm_find_unchinese(filename)
        print(name20)
        # print(filename[:3])
        # 把文件名里的汉字转换成其首字母
        filename1 = pinyin(name20, style=pypinyin.FIRST_LETTER)
        # 创建一个空列表
        filename2 = []
        for ch in filename1:
            filename2.extend(ch)
        # 把列表转换成没有间隔的字符串，因为文件名要以字符串形式存在
        filenameToStr = ''.join(filename2)

        filetype = os.path.splitext(files)[1];  # 文件扩展名

        Newdir = os.path.join(path, filenameToStr + filetype);  # 新的文件名

        os.rename(Olddir, Newdir);  # 重命名


rename();