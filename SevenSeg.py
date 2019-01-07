def seven_segment(lit_seg, broken_seg):
    seg = {"one" : ['B', 'C'],
        "two" : ['A', 'B', 'D', 'E', 'G'],
        "three" : ['A', 'B', 'C', 'D', 'G'],
        "four" : ['B', 'C', 'F', 'G'],
        "five" : ['A', 'C', 'D', 'F', 'G'],
        "six" : ['A', 'C', 'D', 'E', 'F', 'G'],
        "seven" : ['A', 'B', 'C',],
        "eight" : ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        "nine" : ['A', 'B', 'C', 'D', 'F', 'G'],
        "zero" : ['A', 'B', 'C', 'D', 'E', 'F']}

    # one = ['B', 'C']
    # two = ['A', 'B', 'D', 'E', 'G']
    # three = ['A', 'B', 'C', 'D', 'G']
    # four = ['B', 'C', 'F', 'G']
    # five = ['A', 'C', 'D', 'F', 'G']
    # six = ['A', 'C', 'D', 'E', 'F', 'G']
    # seven = ['A', 'B', 'C',]
    # eight = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    # nine = ['A', 'B', 'C', 'D', 'F', 'G']
    # zero = ['A', 'B', 'C', 'D', 'E', 'F']

    for i in seg:
        print(lit_seg)
        print(seg[i])
        #print(list(map(lambda x:x.lower(), seg[i])))
        if seg(i).issubset(lit_seg):
            print(i)
        if list(map(lambda x:x.lower(), seg[i])).issubset(lit_seg):
            print(i)
    return 0


if __name__ == '__main__':
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')
