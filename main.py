import functools
import operator


def narancia_calculator(n1: int, n2: int) -> int:
    # 首先，天才儿童不认识负号
    n1 = abs(n1)
    n2 = abs(n2)
    # 其次，天才儿童九九乘法表还是会的
    if n1 < 10 and n2 < 10:
        return n1 * n2
    # 先竖着乘
    part1 = (n1 % 10) * (n2 % 10)
    # 再横着乘
    part2 = functools.reduce(operator.mul, map(lambda x: int(x), str(n2)))
    # 错位相加
    res = part1 + 10 * part2
    # ；如果末尾有零，福葛好像教过零等于没有，那就划掉吧～
    while res % 10 == 0:
        res /= 10
    return int(res)


if __name__ == '__main__':
    print(narancia_calculator(16, 55))
