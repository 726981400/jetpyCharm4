import os
#mypath1为该文件夹第一个图片
# mypath1="d:\\pic_down\\"
x ="d:\\pic_down\\"
mylist=os.listdir(x)
pic1 = []
pic2 = []
pic3 = []
for i in range(len(mylist)):
    x1 = x + mylist[i]
    try:
        fsize1 = os.path.getsize(x1)
        # print(fsize1)
    except:
        continue
    if fsize1<=100*1024:
        pic1.append(x1)
    elif fsize1<=600*1024:
        pic2.append(x1)
    else:
        pic3.append(x1)
print(pic1)
print(pic2)
print(pic3)

# print(mylist)
# for i in range(len(mylist)):
#     mypath2=mypath1+mylist[i]
#     try:
#         fsize1=os.path.getsize(mypath2)
#     except:
#         continue
#     #print(mypath2, fsize1)
#     for j in range(i+1,len(mylist)):
#         mypath3=mypath1+mylist[j]
#         try:
#             fsize2= os.path.getsize(mypath3)
#         except:
#             continue
#         if fsize1==fsize2:
#             os.remove(mypath3)
#             #print(mypath2,mypath3,fsize1,fsize2)