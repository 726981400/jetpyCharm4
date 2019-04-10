
#改进内容
#1.第二次需要改进的所有功能均已完善
#2.依然采用了D:\pic_down\单文件夹保存图片
#3.图片去重，将D:\pic_down\图片根据大小3个区段导入3个列表，分别进行去重。
#4.保留以及提供下载失败图片的序号信息，
#5.新不足：在xls表格中，已经被去重的图片信息仍然存在，改进ing

#6.下载多页图片，在main函数while循环那里设定

import urllib.request
import re
from bs4 import BeautifulSoup as BS
import datetime
import os
import random
import xlwt

myt1=datetime.datetime.now()
myt2=datetime.datetime.now()

def getHtml(url):
    global my_count
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

my_count=0
data_list = []
def get_data_list(html):
    global my_count
    soup=BS(html,"lxml")
    x = soup.p.text
    y1=str(x).replace(" ","")
    y1 =y1.replace("[转载]", "转载-")

    s1=r'\[(.+?)\]'
    s2=re.compile(s1)
    y2=re.findall(s2,y1)

    y3=y2[1]
    s3=r'\{(.+?)\}'
    s3=re.compile(s3)
    y4=re.findall(s3,y3)
    for i in range(0,len(y4)):
        my_count=my_count+1
        s1=re.compile(r'"objURL":"(.+?)"')
        k1=re.findall(s1,y4[i])
        s2=re.compile(r'"fromPageTitle":"(.+?)"')
        k2=re.findall(s2,y4[i])
        s3 = re.compile(r'"fromURL":"(.+?)"')
        k3 = re.findall(s3, y4[i])
        print(k3)
        s4 = re.compile(r'"bdImgnewsDate":"(.+?)"')
        k4 = re.findall(s4, y4[i])

        s5 = re.compile(r'"type":"(.+?)"')
        k5 = re.findall(s5, y4[i])

        rowdata = [k1, k2, k3, k4, k5]
        data_list.append(rowdata)
    return data_list

def get_excel(datalist):
    print(5 * '=========')
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
    rowdata = ['图片url', 'title', '图片来源网址', '图片上传日期', '图片格式']
    col = 0
    for G in range(len(rowdata)):
        col = col + 1
        booksheet.write(0, col, rowdata[G])
    workbook.save('图片信息.xls')

    # print(len(data_list))
    row = 0
    for i in range(len(data_list)):
        col = 0
        row = row + 1
        rowdata = data_list[i]
        for G in range(len(rowdata)):
            col = col + 1
            booksheet.write(row, col, rowdata[G])
        workbook.save('图片信息.xls',)
    print("所有图片信息保存完毕")

x = 0
y = 0
Error_pic =[]
def getImg(html):

    reg = r'"objURL":"(.*?)",'
    imgre = re.compile(reg)
    html = html.decode('utf-8')
    imglist = re.findall(imgre,html)

    global x
    global y
    global myt1
    global myt2
    for i in imglist:
        pass

    for imgurl in imglist:
        try:
            if str(imgurl).find('.jpg')>=0:
                urllib.request.urlretrieve(imgurl,'D:\pic_down\%05d.jpg' %(random.randint(0, 9999)))
            elif str(imgurl).find('.jpeg')>=0:
                urllib.request.urlretrieve(imgurl,'D:\pic_down\%05d.jpeg' %(random.randint(10000, 19999)))
            elif str(imgurl).find('.png')>=0:
                urllib.request.urlretrieve(imgurl,'D:\pic_down\%05d.png' %(random.randint(20000, 29999)))
            elif str(imgurl).find('.gif') >= 0:
                urllib.request.urlretrieve(imgurl, 'D:\pic_down\%05d.gif' % (random.randint(30000, 39999)))
            else:
                urllib.request.urlretrieve(imgurl,'D:\pic_down\%05d' %(random.randint(40000, 49999)))
            x=x+1
            if x % 250 == 1:
                myt2=datetime.datetime.now()
                xx0=(myt2-myt1).seconds
                print("Time" ,x, "==", xx0)


        except:
            pass
            x+=1
            y+=1
            Error_pic.append(x)
            # print("列表库中第{}张图片=下载失败!!!".format(x))
            print("共{}张图片下载失败".format(y))

#图片去重：三层for循环，最外层的for遍历所有文件夹，给图片去重
def removePic():
    x = "d:\\pic_down\\"
    mylist = os.listdir(x)
    pic1 = []
    pic2 = []
    pic3 = []
    pic_Lists = [pic1, pic2, pic3]
    for i in range(len(mylist)):
        x1 = x + mylist[i]
        try:
            fsize1 = os.path.getsize(x1)
            # print(fsize1)
        except:
            continue
        if fsize1 <= 100 * 1024:
            pic1.append(x1)
        elif fsize1 <= 600 * 1024:
            pic2.append(x1)
        else:
            pic3.append(x1)

    # pics为临时列表
    for pic_list in pic_Lists:
        # mylist = os.listdir(mypath)
        for i in range(len(pic_list)):
            # mypath2 = mypath + mylist[i]
            try:
                fsize1 = os.path.getsize(pic_list[i])
            except:
                continue
            for j in range(i + 1, len(pic_list)):
                # mypath3 = mypath + mylist[j]
                try:
                    fsize2 = os.path.getsize(pic_list[j])
                except:
                    continue
                if fsize1 == fsize2:
                    os.remove(pic_list[i])

if __name__ == '__main__':

    keyword="火灾"
    key_code = urllib.request.quote(keyword) # 对关键词编码
    s1=r"https://tieba.baidu.com/p/2555125530"
    s2=r'''http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word='''+key_code
    i=0
    # while True:
    while i<1:
        page_number=i
        s3=r'''http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=''' + key_code + "&cg=girl&rn=60&pn=" + str(page_number)
        #1.整合网页信息
        html = getHtml(s3)

        #2.加载图片5项信息
        data_list = get_data_list(html)
        #3.下载图片至本地
        getImg(html)
        #4.图片去重
        removePic()

        # 翻页
        i=i+1

        print("**"*10)
        print("第{}页图片下载完毕".format(i))
        print("第{}页图片去重结束".format(i))
        print("**" * 10)


        if x>2600:
            break
    #保存图片信息至xls表格
    get_excel(data_list)

    print("下载失败图片序号如下：{}".format(Error_pic))

    print("finish!","!!!!"*10)
