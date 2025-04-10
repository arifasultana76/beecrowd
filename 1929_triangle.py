a, b, c, d = map(int, input().split())


def is_triangle(x, y, z):
    return x + y > z and x + z > y and y + z > x


if (is_triangle(a, b, c) or
    is_triangle(a, b, d) or
    is_triangle(a, c, d) or
        is_triangle(b, c, d)):
    print('S')
else:
    print('N')
