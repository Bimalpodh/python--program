def can_transform(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]

        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                return False
        else:
            s_to_t[char_s] = char_t
        if char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                return False
        else:
            t_to_s[char_t] = char_s

    return True



print(can_transform("apple", "geekr"))  # Output: True
print(can_transform("moo", "ban"))      # Output: False
print(can_transform("moo", "kgg"))      # Output: True
print(can_transform("badc", "baba"))    # Output: False