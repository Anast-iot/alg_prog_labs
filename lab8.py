import math


def string_to_int_list(s):
    """Перетворює рядок з числами у список цілих чисел без split()."""
    result = []
    current = ""
    for ch in s:
        if ch == " " or ch == "\t":
            if current != "":
                result += [int(current)]
                current = ""
        else:
            current += ch
    if current != "":
        result += [int(current)]
    return result


def list_length(lst):
    """Повертає довжину списку без len()."""
    count = 0
    for _ in lst:
        count += 1
    return count


def wire_segment_length(w, h1, h2):
    """Довжина дроту між двома сусідніми опорами (теорема Піфагора)."""
    return math.sqrt(w * w + (h1 - h2) * (h1 - h2))


def find_max_wire_length(w, heights):
    """
    Знаходить максимальну довжину дроту за допомогою динамічного програмування.

    Кожен стовп i може мати висоту або 1 (мінімум) або heights[i] (максимум).
    dp[i][0] = макс довжина дроту до стовпа i включно, якщо він має висоту 1
    dp[i][1] = макс довжина дроту до стовпа i включно, якщо він має висоту heights[i]
    """
    n = list_length(heights)

    if n <= 1:
        return 0.0

    # Ініціалізуємо таблицю dp: для кожного стовпа два варіанти висоти
    dp = []
    i = 0
    while i < n:
        dp += [[0.0, 0.0]]
        i += 1

    i = 1
    while i < n:
        prev_h_min = 1
        prev_h_max = heights[i - 1]
        cur_h_min = 1
        cur_h_max = heights[i]

        # Поточний стовп має висоту 1 (мінімум)
        option_a = dp[i - 1][0] + wire_segment_length(w, prev_h_min, cur_h_min)
        option_b = dp[i - 1][1] + wire_segment_length(w, prev_h_max, cur_h_min)
        dp[i][0] = option_a if option_a > option_b else option_b

        # Поточний стовп має висоту heights[i] (максимум)
        option_c = dp[i - 1][0] + wire_segment_length(w, prev_h_min, cur_h_max)
        option_d = dp[i - 1][1] + wire_segment_length(w, prev_h_max, cur_h_max)
        dp[i][1] = option_c if option_c > option_d else option_d

        i += 1

    # Відповідь — найбільше з двох варіантів для останнього стовпа
    return dp[n - 1][0] if dp[n - 1][0] > dp[n - 1][1] else dp[n - 1][1]


def format_result(value):
    """Форматує результат до 2 знаків після коми."""
    s = str(round(value, 2))
    if "." not in s:
        s += ".00"
    else:
        decimal_part = s.split(".")[1]
        while list_length(list(decimal_part)) < 2:
            s += "0"
            decimal_part += "0"
    return s


def main():
    w = int(input())
    heights = string_to_int_list(input())
    result = find_max_wire_length(w, heights)
    print(format_result(result))


if __name__ == "__main__":
    main()