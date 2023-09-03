"""
Created at 2023/9/3

count 
repeat
cycle

accumulate()
chain()


"""
import itertools


def count_usage():
    count = itertools.count(start=0, step=2)

    # 获取前5个值  
    for i in range(5):
        print(next(count))


def chain_usage():
    for i in itertools.chain("xxxxxxxxx", [1, 2, 3, 4, 5]):
        print(i)


def permutation_usage():
    """
    排列组合
    
    可重排列、排列、组合
    
    排列： 有序 AB BA 不一样
    组合:  无序 AB BA 一样
    
    :return: 
    """

    # 相当于四个表迭代
    i1 = itertools.product('ABCD', '1234', repeat=2)

    for i in i1:
        print(i)

    # 相当于自连接3次
    i2 = itertools.product('ABC', repeat=3)

    for i in i2:
        print(i)

    print('==============================')

    # 排列
    i3 = itertools.permutations('ABCD', 2)
    for i in i3:
        print(i)

    print('==============================')

    # 组合
    i4 = itertools.combinations('ABCD', 2)
    for i in i4:
        print(i)

    print('==============================')

    i5 = itertools.combinations_with_replacement('ABCD', 2)

    for i in i5:
        print(i)


def run():
    nums = [0, 1, 2, 4]

    result = []

    for length in range(1, len(nums) + 1):
        iterator = itertools.combinations(nums, length)

        result.append(min(list(iterator)))

    print(result)


def run2():
    nums = [0, 1, 2, 4]

    # for i in nums:
    #     print(i)

    for i in nums:
        for j in nums:
            if i < j:
                print(i, j)

    for i in nums:
        for j in nums:
            for k in nums:
                if i > j > k:
                    print(i, j, k)

    i2 = itertools.combinations(nums, 3)

    for i in i2:
        print(i)


if __name__ == "__main__":
    # count_usage()
    # chain_usage()
    # permutation_usage()
    run2()
