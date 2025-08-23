def solution(A, K):
    # Implement your solution here
    if len(A) > 1:
        for i in range(K):
            a = A.pop()
            A.insert(0, a)

    return A
