#coding=utf-8
#urllib模块提供了读取Web页面数据的接口
import urllib.request
#re模块主要包含了正则表达式
import re
from bs4 import BeautifulSoup as BS
import datetime

myt1=datetime.datetime.now()
myt2=datetime.datetime.now()
#定义一个getHtml()函数
my_count=0
def getHtml(url):
    global my_count
    page = urllib.request.urlopen(url)  #urllib.request.urlopen()方法用于打开一个URL地址
    html = page.read() #read()方法用于读取URL上的数据
    #print(html)
    soup=BS(html,"lxml")
    #print(soup.prettify())
    #print(10*"==")
    #print(soup.strong.name,soup.strong.attrs,soup.strong.text)
    x = soup.p.text
    y1=str(x).replace(" ","")
    y1 =y1.replace("[转载]", "转载-")
    #print(y1)

    s1=r'\[(.+?)\]'
    s2=re.compile(s1)
    y2=re.findall(s2,y1)

    y3=y2[1]
    s3=r'\{(.+?)\}'
    s3=re.compile(s3)
    y4=re.findall(s3,y3)
    #print(y4[1])
    #print(10 * '=========')
    for i in range(0,len(y4)):
        my_count=my_count+1
        #print(my_count)
        s1=re.compile(r'"objURL":"(.+?)"')
        k1=re.findall(s1,y4[i])
        #print(k1)
        s2=re.compile(r'"fromPageTitle":"(.+?)"')
        k2=re.findall(s2,y4[i])
        #print(k2)
        s3 = re.compile(r'"fromURL":"(.+?)"')
        k3 = re.findall(s3, y4[i])
        #print(k3)
        s4 = re.compile(r'"bdImgnewsDate":"(.+?)"')
        k4 = re.findall(s4, y4[i])
        #print(k4)

        s5 = re.compile(r'"type":"(.+?)"')
        k5 = re.findall(s5, y4[i])
        #print(k5)
        #print(10 * '=========')
    return html
x = 0
def getImg(html):
    #reg = r'src="(.+?\.jpg)" pic_ext'    #正则表达式，得到图片地址
    #data-imgurl="http://img3.imgtn.bdimg.com/it/u=2801575109,271440238&fm=26&gp=0.jpg"
    #"pageNum":7,            "objURL":"http://imgsrc.baidu.com/imgad/pic/item/a6efce1b9d16fdfaf204db73be8f8c5495ee7bc6.jpg"


    reg = r'"objURL":"(.*?)",'
    imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
    html = html.decode('utf-8') #python3
    imglist = re.findall(imgre,html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的数据

    #return
    #把筛选的图片地址通过for循环遍历并保存到本地
    #核心是urllib.request.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    global x
    global myt1
    global myt2
    for i in imglist:
        pass
        #print(i)
    for imgurl in imglist:
     #print(imgurl)
        try:
            if str(imgurl).find('.jpg')>=0:
                #print("x1-{}={}".format(x,imgurl))
                urllib.request.urlretrieve(imgurl,'D:\pic_down\%s.jpg' %x)
            elif str(imgurl).find('.jpeg')>=0:
                #print("x2-{}={}".format(x,imgurl))
                urllib.request.urlretrieve(imgurl,'D:\pic_down\%s.jpeg' %x)
            elif str(imgurl).find('.png')>=0:
                #print("x3-{}={}".format(x,imgurl))
                urllib.request.urlretrieve(imgurl,'D:\pic_down\%s.png' %x)
            else:
                #print("x4-{}={}".format(x,imgurl))
                urllib.request.urlretrieve(imgurl, 'D:\pic_down\%s.jpg' % x)
            x=x+1
            if x % 250 == 1:
                myt2=datetime.datetime.now()
                xx0=(myt2-myt1).seconds
                print(x, "==", xx0)


        except:
            pass
            #print("{}=error!!!".format(x))



keyword="灾害"
key_code = urllib.request.quote(keyword) # 对关键词编码
s1=r"https://tieba.baidu.com/p/2555125530"
s2=r'''http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word='''+key_code
i=0
#for i in range(0,5):
while True:
    page_number=i
    #print("page number={}".format(page_number))
    s3=r'''http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=''' + key_code + "&cg=girl&rn=60&pn=" + str(page_number)
    html = getHtml(s3)
    getImg(html)
    i=i+1


    if x>2600:
        break

print("finish!","!!!!"*10)