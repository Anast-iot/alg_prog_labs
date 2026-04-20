def all_covered(chosen, worker_prefs, n, b):
    for i in range(n):
        satisfied = False
        for j in range(b):
            if chosen[j] == 1 and worker_prefs[i][j] == 'Y':
                satisfied = True
                break
        if not satisfied:
            return False
    return True

def count_chosen(chosen, b):
    count = 0
    for j in range(b):
        if chosen[j] == 1:
            count += 1
    return count

def backtrack(beer_index, chosen, worker_prefs, n, b):
    if all_covered(chosen, worker_prefs, n, b):
        return count_chosen(chosen, b)

    if beer_index == b:
        return b + 1 

    chosen[beer_index] = 0
    without = backtrack(beer_index + 1, chosen, worker_prefs, n, b)

    chosen[beer_index] = 1
    with_beer = backtrack(beer_index + 1, chosen, worker_prefs, n, b)

    chosen[beer_index] = 0

    if with_beer < without:
        return with_beer
    return without

def solve(worker_prefs, n, b):
    chosen = [0] * b
    return backtrack(0, chosen, worker_prefs, n, b)

def parse_input(raw_input):
    lines = []
    current = ""
    for ch in raw_input:
        if ch == '\n':
            if current != "":
                lines[len(lines):] = [current]
                current = ""
        else:
            current = current + ch
    if current != "":
        lines[len(lines):] = [current]

    first_line_tokens = []
    token = ""
    for ch in lines[0]:
        if ch == ' ':
            if token != "":
                first_line_tokens[len(first_line_tokens):] = [token]
                token = ""
        else:
            token = token + ch
    if token != "":
        first_line_tokens[len(first_line_tokens):] = [token]

    n = int(first_line_tokens[0])
    b = int(first_line_tokens[1])

    tokens = []
    token = ""
    for ch in lines[1]:
        if ch == ' ':
            if token != "":
                tokens[len(tokens):] = [token]
                token = ""
        else:
            token = token + ch
    if token != "":
        tokens[len(tokens):] = [token]

    matrix = [[' '] * b for _ in range(n)]
    for i in range(n):
        for j in range(b):
            matrix[i][j] = tokens[i][j]

    return n, b, matrix

def main():
    import sys
    raw = sys.stdin.read()
    n, b, matrix = parse_input(raw)
    result = solve(matrix, n, b)
    print(result)

if __name__ == "__main__":
    main()