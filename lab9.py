def compute_lps(needle):
    length = 0
    lps = [0] * len(needle)
    i = 1

    while i < len(needle):
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(haystack, needle):
    if not needle:
        return []

    m = len(needle)
    n = len(haystack)
    lps = compute_lps(needle)
    indices = []

    i = 0
    j = 0

    while i < n:
        if needle[j] == haystack[i]:
            i += 1
            j += 1

        if j == m:
            indices.append(i - j)
            j = lps[j - 1]
        elif i < n and needle[j] != haystack[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return indices
