
n = int(input())
s = input()

ans = n

for i in range(n + 1):
    for a in range(2):
        for b in range(2):

            count = 0

            for j in range(i):
                if int(s[j]) != a:
                    count += 1

            for j in range(i, n):
                if int(s[j]) != b:
                    count += 1

            if count < ans:
                ans = count

print(ans)
