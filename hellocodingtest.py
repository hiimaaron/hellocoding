# '토끼야 안녕!'을 출력하는 코드
print('토끼야 안녕!')

# 다양한 숫자를 출력하는 코드
print(1)
print(-2)
print(3.14)

# 더하기, 빼기, 곱하기, 나누기를 하는 코드
print(1+2) # 더하기
print(3-2) # 빼기
print(2*4) # 곱하기
print(6/3) # 나누기

# 제곱, 몫, 나머지를 구하는 코드
print(5**2) # 제곱 구하기
print(5//2) # 몫 구하기
print(5%2) # 나머지 구하기

print(3+7)
print(6*3)
print(4**2)
print(9%5)

# 문자열 출력
print('Hello World')
print('3.14')
print('토끼야 안녕!')
print("토끼야 안녕!")

# 문자열 연산하기
print('토끼'+'야 안녕!') # +는 문자열 연결
print('다람쥐'+'야 안녕!')

print('데굴'*2) # *는 문자열 반복
print('''데굴
데굴''') # 여러 줄 표현

print('빨'+'주'+'노'+'초'+'파'+'남'+'보')


# 변수에 저장한 문자열을 출력하는 코드
rainbow = '빨주노초파남보'
print(rainbow)


# 변수에 저장한 값을 변경하는 코드
count = 0
print(count)

count = 1
print(count)

count = count + 1
print(count) # 변수의 값은 언제든지 변할 수 있다


# 변수를 사용해 음료의 총 금액을 계산하는 코드
coffee = 4000
juice = 5000
tea = 4500

print(coffee*3 + juice*2 + tea*1)
print(coffee*4 + juice*3 + tea*3)
print(coffee*1 + juice*1 + tea*2)


# 여러 개의 변수에 사탕을 저장하는 코드
candy0 = '딸기맛'
print(candy0)

candy1 = '레몬맛'
print(candy1)

candy2 = '수박맛'
print(candy2)

candy3 = '박하맛'
print(candy3)

candy4 = '우유맛'
print(candy4)

# 여러 개의 사탕을 하나의 변수에 저장하는 코드
candies = ['딸기맛', '레몬맛', '수박맛', '박하맛', '우유맛']
print(candies)

# 리스트 만드는 코드
my_list1 = []
print(my_list1)

my_list2 = [1, -2, 3.14]
print(my_list2)

my_list3 = ['앨리스', 10, [1.0, 1.2]]
print(my_list3)

# 리스트에 값을 추가하는 코드
clovers = []
clovers.append('클로버1')
print(clovers)

clovers.append('하트2')
print(clovers)

clovers.append('클로버3')
print(clovers)

# 원하는 위치에 값 추가
print(clovers)
clovers.insert(1, '하트4')
print(clovers)

# 리스트의 값에 접근하는 코드
clovers = ['클로버1', '하트2', '클로버3']
print(clovers[1])
clovers[1] = '클로버2' # 변경 코드
print(clovers[1])

# 리스트의 마지막 값 가져오기
print(clovers[-1])

# 리스트에서 값을 제거하는 코드
clovers = ['클로버1', '클로버2', '클로버3']
print(clovers[1])
del clovers[1]
print(clovers)
print(clovers[1])

# 사탕을 추가하고 제거하는 코드
print(candies)
candies.append('콜라맛')
candies.append('포도맛')
print(candies)
del candies[3]
print(candies)

