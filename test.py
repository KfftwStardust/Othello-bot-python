import timeit
a=10
c=100
start_time = timeit.default_timer()
sum = 0
if a<c:
    t=10
if c<a:
    t=10
if a<c:
    t=10
if c<a:
    t=10
if a<c:
    t=10
if c<a:
    t=10
if a<c:
    t=10
if c<a:
    t=10
for b in range(t):
    sum += b
end_time = timeit.default_timer()
print(f"Time taken for get_best_move: {end_time - start_time} seconds")
print(sum)
start_time = timeit.default_timer()
sum = 0
for b in range(100):
    if b > 9:
        break
    sum += b
end_time = timeit.default_timer()
print(f"Time taken for get_best_move: {end_time - start_time} seconds")
print(sum)