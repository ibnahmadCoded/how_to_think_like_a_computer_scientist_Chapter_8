import time

def do_my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum

sz = 10000000
testdata = range(sz)

t0 = time.time()
my_result = do_my_sum(testdata)
t1 = time.time()
print("my_result = {0} (time taken = {1: 4f} seconds)"
      .format(my_result, t1 - t0))

t2 = time.time()
thier_result = sum(testdata)
t3 = time.time()
print("thier_result = {0} (time taken = {1: 4f} seconds)"
      .format(thier_result, t3 - t2))
