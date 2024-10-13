import collections

Item = collections.namedtuple('Item', ['profit', 'weight'])

def FractionalKnapsack(arr, W):
    arr.sort(key=lambda x: (x.profit/x.weight), reverse=True)
    # print(arr)
    ans = 0.0
    for i in arr:
        if(i.weight <= W):
            W -= i.weight
            ans += i.profit
        else:
            ans += i.profit * W // i.weight
            break
    return ans


def main():
    # # characters for huffman tree & # frequency of characters
    arr = [Item(20, 15), Item(40, 40), Item(50, 70)]
    print(FractionalKnapsack(arr, 50))


main()