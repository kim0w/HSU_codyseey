class Stack:
    def __init__(self, max_size=10):
        self.stack = []
        self.max_size = max_size

    def push(self, item):
        if len(self.stack) >= self.max_size:
            print('경고: 스택이 가득 찼습니다. 더 이상 추가할 수 없습니다.')
        else:
            self.stack.append(item)
            print(f'추가됨: {item}')

    def pop(self):
        if self.empty():
            print('경고: 스택이 비어 있습니다. 꺼낼 내용이 없습니다.')
            return None
        else:
            item = self.stack.pop()
            print(f'꺼냄: {item}')
            return item

    def peek(self):
        if self.empty():
            print('경고: 스택이 비어 있습니다.')
            return None
        else:
            print(f'맨 위의 내용: {self.stack[-1]}')
            return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0

    def visualize(self):
        print('\n[스택 상태]')
        if self.empty():
            print('(비어 있음)')
        else:
            for i, item in enumerate(reversed(self.stack), 1):
                print(f'{i}. {item}')
        print('------------------------')


def main():
    stack = Stack(max_size=10)

    # 내용 추가
    for i in range(1, 12):
        stack.push(f'항목_{i}')
        stack.visualize()

    # 내용 가져오기
    for _ in range(3):
        stack.pop()
        stack.visualize()

    # peek 확인
    stack.peek()

    # 모두 꺼내기
    while not stack.empty():
        stack.pop()
        stack.visualize()

    # 비었는지 확인
    print('\n스택이 비었나요?', stack.empty())


if __name__ == '__main__':
    main()
