def solution(arr):
    lo = arr[0]
    hi = arr[0]
    lob = 0
    hib = 0
    for i in range(1,len(arr)):
        if arr[i] < lo:
            lob += 1
            lo = arr[i]
        if arr[i] > hi:
            hib += 1
            hi = arr[i]
    return [hib, lob]

if __name__ == "__main__":
    size = int(input())
    arr = [int(t) for t in input().strip().split()]
    ans = solution(arr)
    print(str(ans)[1:-1].replace(",",""))