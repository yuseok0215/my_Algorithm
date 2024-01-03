T = int(input())

for i in range(T):
    n,m = map(int, input().split())
    importance = list(map(int, input().split()))

    index = [i for i in range(n)] # 기존의 순서를 저장

    count = 0

    while True:
        if importance[0] >= max(importance):
            count += 1
            
            if index[0] == m:
                print(count)
                break
            else:
                importance.pop(0)
                index.pop(0)
        else:
            importance.append(importance[0])
            importance.pop(0)
            index.append(index[0])
        
"""
1. 접근 방법
어떻게 하면 기존의 순서를 가지고 있을 수 있을까?
-> 인덱스를 진행됨에 따라 마이너스하는 것은 너무 복잡해질 수 있다.
-> 인덱스 자체를 값으로 가지고 있으면 헷갈리지 않을 수 있다.
-> 가장 중요도가 높을 때 인덱스도 찾고자 하는 인덱스와 같은지만 확인하면 될 것 같다.

2. 핵심 알고리즘
인덱스를 값으로 가지고 있는 것을 떠올리는 것..!?

3. 시간 복잡도
O(n)

4. pop과 del의 차이
del은 인덱스를 이용하여 요소를 삭제하는 반면, pop은 인덱스를 이용하여 삭제하면서 삭제한 요소를 반환한다. 
따라서 del 메서드는 삭제한 요소를 반환하지 않으므로 pop 메서드보다 불필요한 작업을 수행하지 않는다. 
또한 del 메서드는 인덱스를 이용해 삭제하므로 평균적으로 pop 메서드보다 약간 더 빠르게 작동한다.
다만 pop과 동시에 해당 값을 사용해야 하는 경우에는 pop이 더 편할 수 있다.
"""
    


