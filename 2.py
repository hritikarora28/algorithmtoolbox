# python3
import time
def max_pairwise_fast(a):
 #   n = int(input())
 #   a = [int(x) for x in input().split()]

    n=len(a)
    a.sort()

    return a[n-1]*a[n-2]

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_fast(input_numbers))

