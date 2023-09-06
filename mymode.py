count = 10

def func(string) :
    ''' 함수명 : func 
    전달인자 : string 문자열 타입으로 문자열 출력에 사용된다. 
    반환값 : 없음
    
    func() 함수에 대한 설명 '''
    print('hello %s' % string)
    
    
if __name__=='__main__ ':
    print(func.__doc__)
    