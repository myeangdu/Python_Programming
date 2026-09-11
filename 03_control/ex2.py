# 반복문 :while문, for문

# while문
# 1 ~ 10까지 반복 출력

i = 1
while i <= 10:
    print(i)
    i+=1

nums = [1, 3, 5, 7, 9]
target = 2
i = 0

while i < len(nums):
    if nums[i] == target:
        print(f"{target}found")
        break
    i += 1
else:
    print(f"{target} not found")

# 1 ~ 10 까지의 합
i = 1
tot = 0
while i <= 10:
    tot += i
    i += 1

print(f"tot : {tot}")

i = 1
tot = 0
while i <= 10:
    if i % 2 == 1:
        tot += i
        i += 1
    else:
        continue

print(f"tot : {tot}")