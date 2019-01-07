def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    temp = data[0]
    count = 0
    top = 0
    answer = ""
    print(sorted(data))
    for i in sorted(data):
        if temp == i:
            count += 1
            if count > top:
                top = count
                answer = i
        else:
            count = 1
        print(i, count)
        temp = i
    print("answer = ", answer)
    print("max experiment = ", max(data, key=data.count))
    return answer

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]))

    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
