
def main():
    print(maximum_in_list([1,3,4,4,2,3,5,12,6]))

def maximum_in_list(nums):
    length = len(nums)
    if length == 1:
        return nums[0]
    m1 = maximum_in_list(nums[0:length//2])
    m2 = maximum_in_list(nums[length//2:length])
    if m1 > m2:
        return m1
    else:
        return m2

main()

