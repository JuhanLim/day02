# 단일라인 주석

# name = '파이썬'  # 단일라인 주석 
# age = 20
# comment = """
#     여러라인 주석
#      단일 따옴표3개 ''' 를 이용할 수도 있다. 
     
#     """
# print(name,age)

# def func():
    
#     """_summary_
#     """
    
#     pass

# name = None
# age = None
# print(name,type(name))
# print(age,type(age))

# age =20
# print(name,type(name),id(age))
# age=3.14
# print(age,type(age),id(age))

# print(name2)

# age = 10
# print(age)
# age=0x10
# print(age)
# age = 0o10
# print(age)
# age=0b10 # 2진수  
# print(age)

# number = -0b1
# print(num)

# obj = 'Hello'
# print(obj==True)

# mylist = ['one', 'two','three']
# mylist =[]
# mylist = ' '
# print(bool(mylist))

# try:
#     var = 10 
# except : 
#     print('에러발생')
# finally:
#     print(var)

# nums = [1,2,3,4,5,6,7,8,9,10]
# nums[0] = 10
# print(nums[0])
# nums = (1,2,3,4,5,6,7,8,9,10)
# nums[0] = 10

# print(nums[0])

# dict = {'name':'홍길동' , 'age':20}
# print(dick['name'],dick['age'])
# dick['major'] = '전산' 
# print(dict['major'])

# set = {1,2,3,4,5,5,5}
# print(set)

# A = {1,2,3}
# B = {2,3,4}
# print(A&B) # 2,3 ( 합치는게 아닌 합집합 )
# print(A-B) # 1
# print(A|B) # 1,,2,3,4 ( 이게 합집합 )  
# print(B-A) # 4

# nums = [1,1,2,3,4,2,4,5,2,4,1]
# print(list(set(nums))) # set 으로 중복제거 ,

# str = 'ABCDE'
# print(str[2:])

# r = range(10)
# print(r)

# a,b = input('두 숫자 입력: ')      
# print('hello', a,b)

# a = 10 
# b = 20
# print(a,b,sep=',',end=' ')
# print(a,b)
# import sys
# sys.stdin # 콘솔과 연결된 표준 입력 
# sys.stdout # 콘솔과 연결된 표준 출력 
# sys.stderr # 콘솔과 연결된 에러 출력 // 

# # fp = open('data.txt','w')
# #print('hello',file=sys.stdout) 
# # fp.close

# try :
#     print ( 10/0)
# except : 
#     print('에러가 발생하였습니다',file=sys.stderr)
    
# nums = [1,2,3,4,5]
# # 문제 1. nums 내에 3값이 있는가? 
# print (3 not in nums)

# a = 10
# b = 10
# print(a is b)
# print (a == b)
# print (id(a),id(b))


# print (10 in [2,6,7,10,12])

# names = 'Python'
# print(names[0])
# print(names[5])
# print(names[-1])
# print(names[-6])
# print(names[len(names)-1]) # 0부터 시작하므로 마지막 단어는 무조건 -1 해주어야함 
# print(names[-(len(names))]) ## 하지만 첫번째 글짜는 음수사용시 글자의 길이와 같다. 

# print(names[:])
# print(names[3:])
# print(names[:3])
# print(names[:-3]) 

# name = "홍길동"
# age = 20
# print(f'이름 : {name}, 연령 : {age}')
# print("이름 : %s" % name)
# print("이름 : %s,연령 : %010d" %(name,age))

# pi = 3.14195
# print("원주율 : %f " % pi)
# print("원주율 : %f " % pi)
# print("원주율 : %f " % pi)
# print("원주율 : %f " % pi)

# name = '홍길동'
# obj = "이름 : {name}, 연령 : {age}"
# age = 20 
# # print(type(name))
# # print(type(format))
# print(obj.format(age=age,name=name)) # == print("이름 : {}".format(name)) 객체로 본다는 뜻 . 
# print(obj.format(age=age,name=name)) 

# person = { 'name': '홍길동','age':20}
# print('이름 : {0[name]}, 연령 : {1[age]}'.format(person))

# def func():
#     print('A')
#     print('B')
#     print('C')

# func()

# def func(name,age):
#     print(f"이름 : {name}, 연령: {age}")

# func('홍길동',20)



# def printPerson(name,age=20):
#     pass 

# printPerson()
# printPerson('홍길동')
# printPerson('홍길동',20)
# ## 이름은 디폴트로 , age 만 넘기고싶다면
# printPerson(age=20, name='에디슨') # 키워드 파라미터를 이용하면 전달 순서를 변경할 수있따.  

# def func(*args):
#     print(args)
#     print(len(args))
#     print('-----------')

# names = ['홍길동','이순신','심청이']
# # func('one')
# # func('one','two')
# # func('one','two','three')
# func(*names)

# def func(**kwargs): # keyWardArgs 
#     if 'name' in kwargs:
#         print(kwargs['name'])
#     else :
#         print("name 키가 없습니다")

# # func()
# # func(one=1)
# # func(one=1,two=2)

# person = {'name' : '홍길동','age' :20}
# func(**person) # ** 의 역할 -> 키 = 값 , 키 = 값 이런식으로 분해해준다. 
#         #  == func(name='홍길동',age=20)

# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     pass

# func(10,20,30, one = 10, two= 20, three=30 )
# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)


# person = {'name': '홍길동','age': 20}
# func(**person)
# print('작업종료')

# def func(*args, **kwargs):
#     if 'name' in kwargs:
#         return True
#     else : 
#         return False 
    
# person = {'name': '홍길동','age' : 20}
# func(**person)
# print('작업종료')

# def func():
#     return 10,20

# a,b = func()
# print(a,b)

# import mymode ## 아직 불러온거 아님 . 참조할라고만 선언

# mymode.func('홍길동') 
# print(mymode.count)

# def func():
#     return 10 

# func = lambda : 10

# def func(x):
#     return x*x 

# func = lambda x: x*x 
# print(func(10))

# def max(a,b):
#     if a>b:
#         return a 
#     else : 
#         return b
    
# max = lambda a,b: a if a>b else b (10,20)## else if 가 나온다면 정의식을 쓰는게 편함. 
# ## 람다식을 써야하는이유? - 함수의 표현식인 람다식을 정의합과 동시에 호출할 수있기 떄문.
# ## 보통의 함수는 def 로 먼저 정의하는 반면에. 

# def func(callback , a,b):
#     return callback(a,b) ## callback 이 함수가 되어야함 

# value = func(max,10,20) ## 이런경우에 max 함수는 이때만 필요하기떄문에 람다식을 사용하는게좋음

# x = 100
# def func(y):
    
#     print(y+x)
   
    
# func(100) 
# print(x)

# x =100 

# def outer(y):
#     def inner():
#         print(x)
#         print(y)
#         y += 10 
#         x += y 
#     return inner()

# outer(100)
# print(x)

def personPrint(name,age,job):
    print(f"이름:{name},연령 :{age},직업 :{job}")

person = {'mwm':'김기희','age':20,'job':'강사'}
personPrint(**person)
