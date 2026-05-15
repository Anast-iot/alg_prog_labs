def str_len(s):
    count = 0
    for _ in s:
        count += 1
    return count


def build_lps(needle):
    m = str_len(needle)
    lps = [0] * m
    length = 0  
    i = 1

    while i < m:
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  
            else:
                i += 1  

    return lps

def kmp_search(haystack, needle):
    if not isinstance(haystack, str) or not isinstance(needle, str):
        raise TypeError("Обидва аргументи повинні бути рядками (str).")
    if str_len(needle) == 0:
        raise ValueError("needle не може бути порожнім рядком.")

    n = str_len(haystack)
    m = str_len(needle)

    if m > n:
        return []

    lps = build_lps(needle)
    result_buf = [0] * (n - m + 1)  
    result_count = 0
    i = 0  
    j = 0  

    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1

        if j == m:                          
            result_buf[result_count] = i - m
            result_count += 1
            j = lps[j - 1]                  
        elif i < n and haystack[i] != needle[j]:
            j = lps[j - 1] if j != 0 else 0
            if j == 0:
                i += 1

    result = [0] * result_count
    k = 0
    while k < result_count:
        result[k] = result_buf[k]
        k += 1

    return result

if __name__ == "__main__":
    examples = [
        ("hello world, hello Python", "hello"),
        ("AABAACAADAABAABA",          "AABA"),
        ("abcabcabc",                 "abc"),
        ("AAAA",                      "AA"),   
        ("abcdef",                    "xyz"),  
        ("banana",                    "a"),
    ]

    for haystack, needle in examples:
        result = kmp_search(haystack, needle)
        print(f"haystack: {haystack!r:30}  needle: {needle!r:6}  {result}")