# a = 1,2,3,4,
# print(a)
#
# a,b,c, = (1,2,3)
# print(a)
# print(b)
# print(c)

# a,b,c, = {1,2,3,}
# print(a)
#
# a,b,c, = ("肖战","王一博","王肖")
# print(a)
#
# a,b,c,d, = ("列表","元组","集合","字典")
# print(a)
# print(a + b)
# list = "列表"
# Tuble = "元组"
# set = "集合"
# dict = "字典"
# print(list)
# a = ("1","2","3","4")
# h,y,*z = (a)
# print(h)
# print(y)
# print(z)
#
# a = 10
# b = 20
# #c = (a // b)
# print(a and b)
#
# z = 123456
# print(z % 10)
# #z //= 100
#
# a = (0-60)
# if ((0-59) >= a):
#     print("不及格")
# else:
#     print("及格")
#
# a_1 = [60,70,80,90,100]
# for a in a_1:
#     if (a>0 and a<60) :
#         print("不及格")
#     elif (a>=60 and a<70):
#         print("及格")
#     elif (a>=70 and a<80):
#         print("良好")
#     elif (a>=80 and a<100):
#         print("优秀")
#     else:
#         print("请输入正确的成绩")
#
#
#
# z = 456789
# print(z % 10)
# print(z // 10)
# z //= 10
# print(z)
# print(z % 10)
# print(z // 10)
# z //= 10
# print(z)
# print(z % 10)
#
#
# s = 1
# for i in range(10,0,-1):
#     s = s * i
# print(s)
#


# flag = True
# a=41
# while flag:
#     b = int(input("请输入数字"))
#     if b > a :
#         print("大了")
#     elif (b < a) :
#         print("小了")
#     else:
#         print("猜对了")
#         flag = False


# for i in range(1,100):
#     a_1 = [60, 70, 80, 90, 100]
#     for a in a_1:
#         if (a > 0 and a < 60):
#             print("不及格")
#         elif (a >= 60 and a < 70):
#             print("及格")
#         elif (a >= 70 and a < 80):
#             print("良好")
#         elif (a >= 80 and a < 100):
#             print("优秀")
#         else:
#             print("请输入正确的成绩")

#
# def xz(c,d):
#     if(d==0):
#         return None
#     else:
#         return(c//d,c%d)
# i = 70
# z = 20
# res = xz(i,z)
# if res is None :
#     print("参数错误")
# else:
#     print("商为:",res[0],"余为",res[1])
#
#
# def wyb(q,w=3):
#     return q+
# print(wyb(6,9))
#
# c = 1,2,3,4,5,6,7
# a,*b=(1,2,3,4,5,6,7)
# print(b)
#
# def xz(*b):
#     s = 0
#     for i in b:
#         s = s + i
#     return s
# print(xz(1,2,3))


# class bbbb():
#     res = None
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#
#     def cccc(self):
#         print(self.res)
#
#
# c = bbbb(10,30)
#
# # c.input(10,30)
# c.sum()
# c.cccc()
# c.div()
# c.cccc()
#
# def c(cls):
#     print(cls)0.

# for i in range(1,10):
# #     for j in range(1,i+1):
# #         print("jijiu",end="\t")
# #     print()

# l = [1,23,464,548,241,57,12,4,102,4,142,4,16,456,41]
#
# length = len(l)
# print (l[0])
# for i in range(length-1,0,-1):
#     for j in range(i):
#         if (l[j] > l[j+1]):
#             l[j] ,l[j+1] = l[j+1],l[j]
# print(l)
a = [12,54,74,89,4,3,55,64,1]
class Father():
    money = 100
    house = 5
    __yi_wu = "裤子"
    def shou_yi(self):
        print("点石成金")

class Myself(Father):
    ai_hao = "花钱"
    def __yi_wu(self,a):
     super.__yi_wu = "裤子"

    pass
c = Myself()
print(c.ai_hao)
print(c.money)
print(c.house)
print(c.shou_yi())


a = {1,235,32,456,5,12,3,131,3}
b = [1,456,3,546,354,1,54,6,456,6,46]
print(a)
print(list(a))
print(tuple(a))
print(set(b))

f = open("heihei.txt","w")
f.write("hahahahahha")
f.close

f = open("haha.txt","w")

n = """kjhlklkklhi
gtuygjguk
ufghkbj
gygjhkljnlkjl
ojhkhjkhlkygtyufy
jhghgjhbjghkhbjug
"""
f.write(n)
f = open("haha.txt","r")

print(f.read(3))


f.close()

c = "djkahjdkhajshdxadjklas"
print(c[0])
print(c[1:])
print(c[::-2])
print(c[-3:0:-2])
print(c[:2])

for i in range(1,10):
    for j in range(1,i+1):
        print("%d x %d = %d"%(j,i,i*j), end="\t")
    print()

for i in range(1,10):
    for j in range(1,i+1):
        print("{} x {} = {}".format(j,i,i*j), end="\t")
    print()


#l = [1,65,12,3,47,3,23,74]

# l[0] = 25
# print(l)
# l[1:4] = 67,26,65
# print(l)
# l = [2,3,4,5,6,2]
# l.append("肖战")
# l.append("肖战")
# l.extend({'123',123})
# print(l)
# print(l.pop())
# print(l)
# print(l.pop(1))
# l.remove(2)
# l.remove(2)
# print(l)

# l.clear()
# print(l)
# a.sort()
# print(l)

d = {"name":"小明","age":"18","sex":"男"}

d.update({"addr":"上海闵行","学历":"本科"})
print(d)

def div(a,b):
    try:
        return a / b
    except:
        return
print(div(10,20))


class CustomException(Exception ):
    def __init__(self,value="值不能为0"):
        self.value = value

    def __str__(self):
        return self.value

a = 0
try:
    if a == 0 :
        print("a = {} 触发异常".format(a))
        raise CustomException
    print("a = {} 未触发异常".format(a))
except CustomException as e:
    print(e)