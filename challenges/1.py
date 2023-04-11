def decrypt_rail_fence(cipher, key):
    rail = [['\n' for j in range(len(cipher))] for i in range(key)]
    downlink = False
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            downlink = True
        if row == key - 1:
            downlink = False
        rail[row][col] = '*'
        col += 1
        row = row + 1 if downlink else row - 1

    c = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and c < len(cipher):
                rail[i][j] = cipher[c]
                c += 1

    final = ''
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            downlink = True
        if row == key - 1:
            downlink = False
        if rail[row][col] != '*':
            final += rail[row][col]
            col += 1
        row = row + 1 if downlink else row - 1

    return final


def decrypt_word_rail_fence(cipher, key):
    rail = [[['-' for k in range(100)] for j in range(len(cipher))] for i in range(key)]
    downlink = False
    row, col = 0, 0
    num_space = cipher.count(' ')

    for i in range(num_space):
        if row == 0:
            downlink = True
        if row == key - 1:
            downlink = False
        rail[row][col][0] = '*'
        col += 1
        row = row + 1 if downlink else row - 1

    c = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j][0] == '*' and c < len(cipher):
                a = ''
                while True:
                    a += cipher[c]
                    if cipher[c] == ' ':
                        c += 1
                        break
                    c += 1
                for k in range(len(a)):
                    rail[i][j][k] = a[k]

    final = ''
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            downlink = True
        if row == key - 1:
            downlink = False
        if rail[row][col][0] != '*':
            for k in range(20):
                final += rail[row][col][k]
                if rail[row][col][k] == ' ':
                    break
            col += 1
        row = row + 1 if downlink else row - 1

    return final[:-1]


if __name__ == '__main__':
    N = int(input())
    n = int(input())
    M = int(input())
    m = int(input())
    X = input().strip()
    message = input().strip()

    for i in range(M):
        message = decrypt_rail_fence(message, m)

    replace_with = ' '
    pos = 0
    while True:
        pos = message.find(X, pos)
        if pos == -1:
            break
        message = message[:pos] + replace_with + message[pos+len(X):]
        pos += len(replace_with)

    num_space = message.count(' ')
    message += ' '

    print(message)

