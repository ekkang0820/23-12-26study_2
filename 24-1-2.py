#백준 15662번
def do_rotate(gear, dir):
    if dir:
        return gear[-1] + gear[:-1]
    else:
        return gear[1:] + gear[0]

def main():
    T = int(input())
    gears = [input() for _ in range(T)]

    K = int(input())
    for _ in range(K):
        n, d = map(int, input().split())
        n -= 1
        dir = d == 1

        left = n
        while left > 0 and gears[left][6] != gears[left - 1][2]:
            left -= 1

        right = n
        while right < T - 1 and gears[right][2] != gears[right + 1][6]:
            right += 1

        for i in range(n, left - 1, -1):
            dir = not dir if i != n else dir
            gears[i] = do_rotate(gears[i], dir)

        dir = d == 1
        for i in range(n + 1, right + 1):
            dir = not dir
            gears[i] = do_rotate(gears[i], dir)

    ans = sum(1 for gear in gears if gear[0] == '1')
    print(ans)

if __name__ == "__main__":
    main()

