
# Dictionaries

# 키와 값의 쌍으로 구성된 데이터 구조로, 키를 통해 값을 찾을 수 있으므로 매우 빠른 조회 성능을
# 보여준다.

teacher = {'name': 'pig', 'team' : 'ohgiraffers'}

print(type(teacher))
print(teacher['name'])
print(teacher['team'])

# 생성 후 키-값 쌍 추가/ 수정/ 삭제
teacher ['age'] = 20
print(teacher['age'])


# in 키워드
print('name' in teacher) # key값의 존재 여부를 확인할 수 있다.

# 1. get()
# 매개변수로 전달받은 key에 해당하는 값을 반환한다.
print(teacher.get('name'))

# 2. keys()
# dict안에있는 모든 key값을 받아올 수 있다.
print(teacher.keys())

# 3. values()
# dict안에있는 모든 values값을 받아올 수 있다.
print(teacher.values())

# 4. items()
# dict안에있는 모든 값을 받아올 수 있다.
print(teacher.items())
print(teacher)

# 5. pop(키)
# 특정 항목을 제거하는 메소드
print(teacher.pop('age'))
print(teacher)

# 6. clear()
# 모든 항목을 제거하는 메소드
teacher.clear()
print(teacher)