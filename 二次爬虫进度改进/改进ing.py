
import urllib.request
import re
from bs4 import BeautifulSoup as BS
import datetime

myt1=datetime.datetime.now()
myt2=datetime.datetime.now()
my_count=0
def getHtml(url):
    global my_count
    page = urllib.request.urlopen(url)
    html = page.read()
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

    return html
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
                urllib.request.urlretrieve(imgurl,'D:\pic_down2\jpg\%s.jpg' %x)
            elif str(imgurl).find('.jpeg')>=0:
                urllib.request.urlretrieve(imgurl,'D:\pic_down2\jpeg\%s.jpeg' %x)
            elif str(imgurl).find('.png')>=0:
                urllib.request.urlretrieve(imgurl,'D:\pic_down2\png\%s.png' %x)
            else:
                urllib.request.urlretrieve(imgurl, 'D:\pic_down2\else\%s' % x)
            x=x+1
            if x % 250 == 1:
                myt2=datetime.datetime.now()
                xx0=(myt2-myt1).seconds
                print(x, "==", xx0)


        except:
            pass

if __name__ == '__main__':
    keyword="灾害"
    key_code = urllib.request.quote(keyword) # 对关键词编码
    s1=r"https://tieba.baidu.com/p/2555125530"
    s2=r'''http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word='''+key_code
    i=0

    while True:
        page_number=i
        s3=r'''http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=''' + key_code + "&cg=girl&rn=60&pn=" + str(page_number)
        html = getHtml(s3)
        getImg(html)
        i=i+1

        if x>2600:
            break

    print("finish!","!!!!"*10)