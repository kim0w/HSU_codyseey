class Stack:
  
    MAX_SIZE = 10  # 스택의 최대 크기
    
    def __init__(self):
        """
        Stack 객체를 초기화
        
        """
        # 스택의 실제 내용을 저장할 리스트 (Python의 list를 사용)
        self._items = []  
        self._current_size = 0  # 현재 스택에 들어있는 요소의 개수

    def _visualize(self):
        """
        현재 스택의 상태를 시각적으로 출력(보너스 과제)
        """
        print('--- 스택 상태 시각화 ---')
        if self.empty():
            print('| (비어 있음) |')
            print('--------------')
            return

        # 스택은 LIFO이므로, 가장 위의 요소(_items[-1])가 가장 먼저 출력되도록 역순으로 순회
        # 시각화를 위해 고유 번호 부분을 포함하여 출력
        for i in range(len(self._items) - 1, -1, -1):
            item = self._items[i]
            # [TOP] 표시 추가
            if i == len(self._items) - 1:
                print(f'| {item} | <--- [TOP] (가장 최근 추가된 항목)')
            else:
                print(f'| {item} |')

        print('--------------')
        print(f'현재 항목 수: {self._current_size} / 최대 크기: {self.MAX_SIZE}')
        print('--------------------------')

    def push(self, item):
        """
        스택에 내용을 추가 (최대 10개)
        
        :param item: 스택에 추가할 내용
        :return: True (성공) 또는 False (실패)
        """
        if self._current_size >= self.MAX_SIZE:
            print('** 경고: 스택이 가득 찼습니다. 더 이상 항목을 추가할 수 없습니다. **')
            return False
        
        self._items.append(item)
        self._current_size += 1
        print(f' PUSH 성공: {item} 추가됨')
        self._visualize()
        return True

    def pop(self):
        """
        가장 마지막에 추가된 내용을 가져오고 스택에서 제거 (LIFO)
        
        :return: 가장 위의 항목 또는 None (스택이 비어있는 경우)
        """
        if self.empty():
            print('** 경고: 스택이 비어 있습니다. 가져올 내용이 없습니다. **')
            return None
        
        popped_item = self._items.pop()
        self._current_size -= 1
        print(f' POP 성공: {popped_item} 제거 및 반환')
        self._visualize()
        return popped_item

    def empty(self):
        """
        스택이 비어있는지 확인
        
        :return: 스택이 비어 있으면 True, 아니면 False
        """
        return self._current_size == 0

    def peek(self):
        """
        가장 마지막에 추가된 내용을 삭제하지 않고 내용만 확인
        
        :return: 가장 위의 항목 또는 None (스택이 비어있는 경우)
        """
        if self.empty():
            print('** 경고: 스택이 비어 있습니다. 확인할 내용이 없습니다. **')
            return None
        
        # 가장 마지막 항목은 인덱스 -1
        peek_item = self._items[-1]
        print(f'🧐 PEEK 확인: {peek_item} (삭제되지 않음)')
        return peek_item

    def get_size(self):
        """
        현재 스택에 들어있는 항목의 개수를 반환
        """
        return self._current_size
    # 1. Stack 클래스 인스턴스 생성
my_stack = Stack()
print('>>> 스택 인스턴스 생성 완료')

# 2. empty() 함수로 초기 상태 확인
print('\n--- [TEST 1] 초기 상태 확인 ---')
print(f'스택이 비어 있나요? {my_stack.empty()}') # True 출력 예상

# 3. pop() 함수로 비어 있을 때 경고 메시지 확인
my_stack.pop() # 경고 메시지 출력 예상
print('-------------------------------')

# 4. peek() 함수로 비어 있을 때 경고 메시지 확인
my_stack.peek() # 경고 메시지 출력 예상
print('-------------------------------')

# 5. push() 함수로 내용 입력 (고유 번호 포함)
print('\n--- [TEST 2] PUSH 동작 확인 (5개 추가) ---')
for i in range(1, 6):
    item_data = f'항목_{i:02d}'  # 고유 번호 '01', '02' 등으로 구성
    my_stack.push(item_data)
    
# 6. peek() 함수로 가장 마지막 항목 확인 (삭제 안됨)
print('\n--- [TEST 3] PEEK 동작 확인 ---')
print(f'현재 TOP 항목: {my_stack.peek()}') # 항목_05 출력 예상
print(f'현재 항목 수: {my_stack.get_size()}') # 5 출력 예상
print('-------------------------------')

# 7. pop() 함수로 내용 가져오기 (LIFO 확인)
print('\n--- [TEST 4] POP 동작 확인 (3개 가져오기) ---')
item_1 = my_stack.pop() # 항목_05 반환 및 제거 예상
item_2 = my_stack.pop() # 항목_04 반환 및 제거 예상
item_3 = my_stack.pop() # 항목_03 반환 및 제거 예상

print(f'\n가져온 항목 순서: {item_1}, {item_2}, {item_3}')
print(f'스택이 비어 있나요? {my_stack.empty()}') # False 출력 예상
print(f'현재 항목 수: {my_stack.get_size()}') # 2 출력 예상
print('-------------------------------')

# 8. 스택 최대 크기(10개) 초과 시 경고 메시지 확인을 위한 PUSH
print('\n--- [TEST 5] 스택 최대 크기 초과 확인 (8개 추가 -> 총 10개 -> 11개째 시도) ---')
# 현재 2개 남아있음 (항목_01, 항목_02)
for i in range(6, 14): # i=6부터 13까지 총 8번 PUSH 시도
    item_data = f'항목_{i:02d}' 
    my_stack.push(item_data)
    
# 11번째 PUSH 시도 (i=12)에서 경고 메시지 출력 예상
print('-------------------------------')

# 9. empty() 함수로 가득 찬 상태 확인
print('\n--- [TEST 6] 최종 상태 확인 ---')
print(f'스택이 비어 있나요? {my_stack.empty()}') # False 출력 예상
print(f'최종 항목 수: {my_stack.get_size()}') # 10 출력 예상
print('-------------------------------')

# 10. 스택 내용 모두 POP
print('\n--- [TEST 7] 스택 전체 POP ---')
while not my_stack.empty():
    my_stack.pop()
    
# 11. 스택이 완전히 비었는지 확인
print('\n--- [TEST 8] 스택 완전 비움 확인 ---')
print(f'스택이 비어 있나요? {my_stack.empty()}') # True 출력 예상
print('-------------------------------')