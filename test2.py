def test(people=list(range(20)),count=7):
    # num = len(people)
    if len(people) == 2:
        return people
    for i in people:
        count += 1
        # print(i, count)
        if count % 3 == 0:
            people.remove(i)
            # 由于列表的元素i已经删除，元素i的下一个元素移动到i的位置，下一次循环会跳过i+1，由于i+1决定安全，手动count+1
            count += 1  
            # print('del')
    # print(people)
    return test(people,count)


def main():
    a = test()
    str_a = ','.join(str(i) for i in a)
    print('剩下的２个人的位置是：', str_a)


if __name__ == '__main__':
    main()
    




# a = [1,2,3]
# a.remove(2)
# print(a)
# print(len(a))
0 - 8
1 - 9
2 - 10
3 - 11
4 - 12