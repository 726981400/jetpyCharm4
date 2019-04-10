
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
def getImg(html):

    reg = r'"objURL":"(.*?)",'
    imgre = re.compile(reg)
    html = html.decode('utf-8')
    imglist = re.findall(imgre,html)

    global x
    global myt1
    global myt2
    for i in imglist:
        pass

    for imgurl in imglist:
        try:
            if str(imgurl).find('.jpg')>=0:
                urllib.request.urlretrieve(imgurl,'D:\pic_down2\jpg\%05d.jpg' %(random.randint(0, 9999)))
            elif str(imgurl).find('.jpeg')>=0:
                urllib.request.urlretrieve(imgurl,'D:\pic_down2\jpeg\%05d.jpeg' %(random.randint(10000, 19999)))
            elif str(imgurl).find('.png')>=0:
                urllib.request.urlretrieve(imgurl,'D:\pic_down2\png\%05d.png' %(random.randint(20000, 29999)))
            elif str(imgurl).find('.gif') >= 0:
                urllib.request.urlretrieve(imgurl, 'D:\pic_down2\gif\%05d.gif' % (random.randint(30000, 39999)))
            else:
                urllib.request.urlretrieve(imgurl,'D:\pic_down2\else\%05d' %(random.randint(40000, 49999)))
            x=x+1
            if x % 250 == 1:
                myt2=datetime.datetime.now()
                xx0=(myt2-myt1).seconds
                print("Time" ,x, "==", xx0)


        except:
            pass

#图片去重：三层for循环，最外层的for遍历所有文件夹，给图片去重
def removePic():

    mypath1 = 'D:\\pic_down2\\jpg\\'
    mypath2 = 'D:\\pic_down2\\jpeg\\'
    mypath3 = 'D:\\pic_down2\\png\\'
    mypath4 = 'D:\\pic_down2\\gif\\'
    mypath5 = 'D:\\pic_down2\\else\\'
    mypath_List = [mypath1, mypath2, mypath3, mypath4,mypath5]
    # for i in mypath_List:
    #     print(i)

    for mypath in mypath_List:
        mylist = os.listdir(mypath)
        for i in range(len(mylist)):
            mypath2 = mypath + mylist[i]
            try:
                fsize1 = os.path.getsize(mypath2)
            except:
                continue
            for j in range(i + 1, len(mylist)):
                mypath3 = mypath + mylist[j]
                try:
                    fsize2 = os.path.getsize(mypath3)
                except:
                    continue
                if fsize1 == fsize2:
                    os.remove(mypath3)

if __name__ == '__main__':

    keyword="灾害"
    key_code = urllib.request.quote(keyword) # 对关键词编码
    s1=r"https://tieba.baidu.com/p/2555125530"
    s2=r'''http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word='''+key_code
    i=0
    # while True:
    while i<2:
        page_number=i
        s3=r'''http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=''' + key_code + "&cg=girl&rn=60&pn=" + str(page_number)
        html = getHtml(s3)

        data_list = get_data_list(html)

        getImg(html)
        removePic()
        i=i+1

        print("第{}页图片下载完毕".format(i))
        print("第{}页图片去重结束".format(i))

        if x>2600:
            break

    get_excel(data_list)

    print("finish!","!!!!"*10)