
def topKFrequent(nums, k):
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    arr = []
    for num, cnt in count.items():
        arr.append([cnt, num])
    arr.sort()

    res = []
    while len(res) < k:
        res.append(arr.pop()[1])
    return res
    


def main():
    nums = [1, 1, 2, 3, 3, 3]
    k = 2
    answer = topKFrequent(nums, k)
    print(answer)

if __name__ == "__main__":
    main()