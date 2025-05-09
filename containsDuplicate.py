
def hasDuplicate(nums) -> bool:
    hashtable = set()


    for i in nums:

        if i in hashtable:
            return True
        hashtable.add(i)
    return False
    

def main():
    nums = [1, 1, 2]
    answer = hasDuplicate(nums)
    print(answer)

if __name__ == "__main__":
    main()