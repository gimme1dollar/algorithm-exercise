def parse(a: int) -> str:
    return str(a + 1)


def search(N, M, curr, buffer):
    if len(buffer) == M:
        print(" ".join(map(parse, buffer)))

    for i in range(curr + 1, N):
        search(N, M, i, buffer + [i])

    return


if __name__ == "__main__":
    N, M = map(int, input().split())

    search(N, M, 0, [0])
    search(N, M, 0, [])