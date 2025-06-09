
def soma(arr):
    if len(arr) <= 0:
        return 0
    if len(arr) == 1:
        return arr.head()
    return arr.head() + soma(arr.tail())

print(soma([1,2,3]))
