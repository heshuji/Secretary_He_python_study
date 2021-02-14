print('目前只支持Excel,也就是后缀为.xls 和.xlsx 两种格式')
print('对比的到底是啥?')
print('不同的两个表格的不同的两列')
print('所以你需要输入4个值:两个路径,两个表格中要对比的列的第一行的值')
print('什么是路径?我举个例子:')
print('像这样的  c:\work\食科3班.xlsx')
print('什么是列的第一行的值,举个例子')
print('你要对比一下你们班有谁没有交作业,一个是有你们班全部名字的表格,我叫他标准表格,另一个只有部分人员的表格,我叫他对比表格')
print('那么列的第一行的值应该都是姓名')
print('如果出现了什么问题,请向我反馈 QQ:614233664')
print("输入表格路路径最好将 \ 换为 /  或者将大写的盘符改为小写的也可以")
road1=input('请输入标准表格路径')
import pandas as pd#导入pandas函数
no_student=[]#建立一个到时候两表格都没有人的列表
data=pd.read_excel(road1)#读取表格数据,写入你的标准表格路径
liename1=input('请输入标准的列的第一行的值')
data2=data.loc[:,liename1]#调取表格中的某一列数据
student_enter=[]#建立一个装标准数据的列表
student_bijiao={}#建立一个装被对比的字典
for name1 in data2:
    student_enter.append(name1)#将所有装标准数据装入列表
road2=input('请输入对比表格路径')
data3=pd.read_excel(road2)#写入你要对比的表格的路径
liename2=input('请输入要对比的列的第一行的值')
dat4=data3.loc[:,liename2]#调取表格中的某一列数据
for name2 in dat4:
    student_bijiao[name2]=1#将某一列数据导入字典,其中1可以用任何str代替
for student in student_enter:#
    try:
        student_bijiao[student]
    except KeyError:
        no_student.append(student)
    finally:
        print(student,'已经对比')
print("让我看看谁不在：", no_student)
input('按任意键退出')
