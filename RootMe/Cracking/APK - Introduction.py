def make_flag(s):
    a = s[5]
    _b = s[2]

    for s_ in range(len(s)):
        # Calcul de b
        b = _b[max(len(_b) - s_, 0):] + _b[s_:]

        # Calcul de _b2
        if s_ >= 3:
            _b2 = _b + s[s_ - 3]
        else:
            _b2 = _b + s[len(s) - (3 - s_)]

        # Mise à jour de _b
        if s_ >= len(_b2):
            _b = _b2 + s[s_ - len(_b2)]
        elif len(s) >= len(_b2) - s_:
            _b = _b2 + s[len(s) - (len(_b2) - s_)]
        else:
            _b = _b2 + s[len(s) - ((len(_b2) - s_) - len(s))]

        # Mise à jour de a
        if len(b) > 0:
            index = (((len(s) + len(_b)) * s_) + len(_b)) % len(b)
            a += b[index]

    # Construction finale
    flag = a[:2] + s[3] + a[3] + '0' + a[5:7]
    return flag

seed = "1dndr@"
print("Flag:", make_flag(seed))  # Affiche "@n1d0r"
