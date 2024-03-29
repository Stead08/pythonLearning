#配列の要素数
n = int(input())
#配列[A_1 A_2 ... A_n]の入力を想定
A = list(map(int, input().split()))

def insertion_sort(A, n):
    for i in range(1, n):
        #A[i] を、整列済みの A[0] ~ A[i-1] の適切な位置に挿入する
        #実装の都合上、A[i] の値が上書きされてしまうことがあるので、予め A[i] の値をコピーしておく
        x = A[i]
        #A[i] の適切な挿入位置を表す変数 j を用意
        j = i - 1
        #A[i] の適切な挿入位置が見つかるまで、A[i] より大きい要素を1つずつ後ろにずらしていく
        while j >= 0 and A[j] > x:
            A[j+1] = A[j]
            j -= 1
        #A[i]を代入
        A[j+1] = x
        print(*A)
insertion_sort(A,n)
