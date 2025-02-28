#####
# 1. 리스트 컴프리헨션 => 리스트를 초기화하는 방법 중 하나로,
# 대괄호 안에 조건문과 반복문을 넣는 방식으로 조건문을 초기화할 수 있음.
# 1-1. 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i%2 ==1]

print(array)

# 1-2. 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array2 = [i*i for i in range(1,10)]

print(array2)

# 1-3. ***** '특정 크기의 2차원 리스트를 초기화'할 때는 반드시 리스트 컴프리헨션을 이용해야 한다. *****
# N*M 크기의 2차원 리스트 초기화(잘못된 방법)
n = 3
m = 4
array3 = [[0] * m] * n
print(array3)

array3[1][1]=5 # 분명 하나만 바꿨는데
print(array3) # 3개의 리스트에서 인덱스 1에 해당하는 원소들의 값이 모두 5로 바뀜
# 내부적으로 포함된 3개의 리스트가 모두 동일한 객체에 대한 3개의 '레퍼런스'로 인식되기 때문.
# 그러므로, 특정 크기의 2차원 리스트를 초기화할 때는 리스트 컴프리헨션을 사용해야 함.
# 올바른 방법
n = 3
m = 4
array5 = [[0] * m for _ in range(n)]
print( array5 )
array5[1][1] = 5
print(array5)


#####
# 2. 리스트 관련 메서드
# name.append(you want) -> O(1)
# name.sort() -> O(NlogN)
# name.sort(reverse=True) -> O(NlogN)
# name.reverse() -> O(N)
# name.insert(index, you want) -> O(N)
# name.remove(you want) -> O(N)
# insert, remove의 경우 너무 많이 쓰면 시간초과 발생함
# 그렇다면 특정 값의 원소를 모두 제거하려면 어떻게 해야하는가?
a = [1,2,3,4,5,5,5]
remove_set = {3,5}#지우고자 하는 애들

# 리스트 순회하며 remove_set에 들어있지 않은 원소를 result에 저장
result = [i for i in a if i not in remove_set]
print(result)




#####
# 3. 파이썬 표준 라이브러리
# print(), input() //import 필요 없음
-> sum, min, max, sorted
-> eval() : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환함.
# itertools : 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리. 순열과 조합 라이브러리를 제공. //from itertools import name
-> permutations(name, n) : name list에서 n개를 뽑아 나열(순서 고려 O, 중복 허용 X)
-> combinations(name, n) : name list에서 n개를 뽑아 나열(조합)(순서 고려 X, 중복 허용 X)
-> product(name, repeat=n) : name list에서 중복을 허용하여 n개를 뽑아 나열(조합)(순서 고려O, 중복 허용 O)
-> combiantions_with_replacement(name, n) : name list에서 중복을 허용하여 n개를 뽑아 나열(순서 고려 X, 중복 허용 O)
# heapq : Heap의 기능을 제공하는 라이브러리로, 우선순위 큐 기능을 구현하기 위해 사용함
-> import heapq
-> heapq.heappush(name, value)
-> heapq.heappop(name)
-> heapsort(name)
-> python에서는 min heap을 지원함(max heap 없음). 따라서, heapq를 통해 정렬을 하면 맨 위 노드는 가장 작은 값임.
-> 만약 오름차순이 아니라 내림차순으로 정렬하고 싶다면, heapq에 입력값을 줄 떄, '-'부호를 임시로 붙여서 넣고 출력할 때, -부호를 떼어주면 내림차순이 됨
# bisect : Binary Search 기능을 제공하는 라이브러리
-> from bisect import bisect_left, bisect_right
-> bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽일할 가장 왼족 인덱스를 찾는 메서드
-> bisect_right(a, x) : 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
# collections : deque, counter 등의 유용한 자료구조를 포함하고 있는 라이브러리
# math : 필수적인 수학적 기능을 제공하는 라이브러리. 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함하고 있음.