from helloword import fb

a = [1, 3, 5, 15]
b = [1, "fizz", "buzz", "fizzbuzz"]
for i in range(len(a)):
    assert (fb(a[i]) == b[i])
