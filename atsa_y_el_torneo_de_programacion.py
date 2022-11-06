
def compute(A, n):
    array_sum = 0
    for i in range(0, n, 1):
        array_sum = array_sum + A[i]

    array_sum_square = array_sum * array_sum

    individual_square_sum = 0
    for i in range(0, n, 1):
        individual_square_sum += A[i] * A[i]

    return int((array_sum_square - individual_square_sum) / 2)

if __name__ == '__main__':
    n = int(input())
    nums = [int(x) for x in input().split()]
    print(compute(nums, n))
