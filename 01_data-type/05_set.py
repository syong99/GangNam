
# SET

# 중복을 허용하지 않으면 순서 없이 요소를 저장하는 컬렉션이다.
# 따라서 중복 제거가 필요할 때 유용하게 사용할 수 있다.
# {} 중괄호를 사용하여 집합을 생성한다.

ohgiraffers = {'pig', 'squirrel', 'bear', 'gorilla', 'pig'}

print(ohgiraffers)

#리스트로 set 생성
another_safari_set = set(['monkey', 'tiger', 'wolf'])

print(another_safari_set)

mixed_set = {1,'bear', (1,2,3)}

print(mixed_set)


ohgiraffers.remove('pig') # pig remove

print(ohgiraffers)

ohgiraffers.add('pig') # pig add

print(ohgiraffers)