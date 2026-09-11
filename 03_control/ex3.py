# for문

# for (int i = 0;i < 10;i++)
# for i in iterable 객체

for i in range(5):
    print(i, end='')

print()

a = range(5)
print(a.start, a.stop, a.step)
print(a)

for i in range(1, 6):
    print(i, end='')
print()

# 5 4 3 2 1
for i in range(5, 0, -1):
    print(i, end='')
print()

tot = 0
for i in range(1, 11):
    tot += i

print(f"tot:{tot}")

print(sum(range(1, 11)))

s = "hi123123한😊😘(●'◡'●)ಥ_ಥ<3"

print(len(s))

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}x{j}={i*j} ", end = '')
    print()

