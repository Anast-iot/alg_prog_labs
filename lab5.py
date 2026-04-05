# 8 можливих зміщень коня
MOVES = [
    (-2, -1), (-2, +1),
    (+2, -1), (+2, +1),
    (-1, -2), (-1, +2),
    (+1, -2), (+1, +2)
]

def bfs(n, start, end):
    if start[0] == end[0] and start[1] == end[1]:
        return 0

    max_size = n * n
    queue_row = [0] * max_size
    queue_col = [0] * max_size
    queue_steps = [0] * max_size
    queue_head = 0
    queue_tail = 0

    queue_row[queue_tail] = start[0]
    queue_col[queue_tail] = start[1]
    queue_steps[queue_tail] = 0
    queue_tail += 1

    visited = [[False] * n for _ in range(n)]
    visited[start[0]][start[1]] = True

    while queue_head < queue_tail:
        row = queue_row[queue_head]
        col = queue_col[queue_head]
        steps = queue_steps[queue_head]
        queue_head += 1

        for i in range(8):
            new_row = row + MOVES[i][0]
            new_col = col + MOVES[i][1]

            if 0 <= new_row < n and 0 <= new_col < n:
                if not visited[new_row][new_col]:
                    if new_row == end[0] and new_col == end[1]:
                        return steps + 1

                    visited[new_row][new_col] = True
                    queue_row[queue_tail] = new_row
                    queue_col[queue_tail] = new_col
                    queue_steps[queue_tail] = steps + 1
                    queue_tail += 1
    return -1

def clean_string(s):
    # Ручна реалізація strip() та видалення коментарів
    clean = ""
    for char in s:
        if char == "#": break
        clean += char
    
    # Видаляємо пробіли з початку
    i = 0
    while i < len(clean) and (clean[i] == " " or clean[i] == "\r" or clean[i] == "\t"):
        i += 1
    # Видаляємо з кінця
    j = len(clean) - 1
    while j >= i and (clean[j] == " " or clean[j] == "\r" or clean[j] == "\t"):
        j -= 1
    return clean[i : j + 1]

def parse_pair(s):
    # Ручний пошук коми без split()
    s = clean_string(s)
    comma_i = -1
    for i in range(len(s)):
        if s[i] == ",":
            comma_i = i
            break
    
    num1 = int(clean_string(s[:comma_i]))
    num2 = int(clean_string(s[comma_i + 1:]))
    return (num1, num2)

def read_input(filename):
    f = open(filename, "r", encoding="utf-8")
    content = f.read()
    f.close()

    lines = []
    current = ""
    # Додаємо \n в кінець для коректної обробки останнього рядка
    for ch in content + "\n":
        if ch == "\n":
            cleaned = clean_string(current)
            if cleaned != "":
                lines = lines + [cleaned]
            current = ""
        else:
            current += ch

    n = int(lines[0])
    start = parse_pair(lines[1])
    end = parse_pair(lines[2])
    return n, start, end

def write_output(result, filename):
    f = open(filename, "w", encoding="utf-8")
    f.write(str(result))
    f.close()

def main():
    try:
        n, start, end = read_input("input.txt")
        result = bfs(n, start, end)
        write_output(result, "output.txt")
    except Exception as e:
        # Для дебагу, якщо файл не знайдено
        print("Error: " + str(e))

if __name__ == "__main__":
    main()