N = int(input())
MOD = 9901

prev_no_lion = 1
prev_left_lion = 1
prev_right_lion = 1

for _ in range(2, N + 1):
    new_no_lion = (prev_no_lion + prev_left_lion + prev_right_lion) % MOD
    new_left_lion = (prev_no_lion + prev_right_lion) % MOD
    new_right_lion = (prev_no_lion + prev_left_lion) % MOD

    prev_no_lion, prev_left_lion, prev_right_lion = new_no_lion, new_left_lion, new_right_lion

result = (prev_no_lion + prev_left_lion + prev_right_lion) % MOD
print(result)