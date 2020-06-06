import random


def findwithoutbinarysearch(lst, a):
    for x in lst:
        if x == a:
            print(str(a) + " is in the list")
            break
        else:
            print(str(a) + " is not in the list")
            break


def findwithbinarysearch(lst, l, r, a):
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if lst[mid] == a:
            return mid

            # If element is smaller than mid, then it
        # can only be present in left subarray
        elif lst[mid] > a:
            return findwithbinarysearch(lst, l, mid - 1, a)

            # Else the element can only be present
        # in right subarray
        else:
            return findwithbinarysearch(lst, mid + 1, r, a)

    else:
        # Element is not present in the array
        return -1




if __name__ == "__main__" :
    l1 = random.sample(range(1, 101), 6)
    l1 = sorted(l1)
    print(l1)
    so = input("enter a number:")
    findwithoutbinarysearch(l1, so)
    print("...")
    l2 = random.sample(range(1, 101), random.randint(6, 11))
    l2 = sorted(l2)
    print(l2)
    so2 = int(input("enter a number:"))
    x = len(l2)
    result = findwithbinarysearch(l2, 0, x-1, so2)
    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")

