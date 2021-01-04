# https://www.codewars.com/kata/5b5fe164b88263ad3d00250b
def perm(p, l):
    if l == 0:
        yield p
    else:
        for i in range(10):
            if (i not in p):
                yield from perm(p + [i], l - 1)


def alphametics(puzzle):
    puzzleTrimmed = puzzle.replace(" ", "")
    charAddends = puzzleTrimmed.split("=")[0].split("+")
    charResult = puzzleTrimmed.split("=")[1]
    charDigits = list(set(puzzleTrimmed.replace('+', '').replace('=', '')))

    longestAddendLen = max(len(a) for a in charAddends)
    iAddends = [list() for _ in range(longestAddendLen)]
    for charAddend in charAddends:
        for i, charDig in enumerate(charAddend[::-1]):
            iAddends[i].append(charDigits.index(charDig))

    iResult = [charDigits.index(c) for c in charResult[::-1]]

    for p in perm([], len(charDigits)):
        carry = 0
        i = 0
        # check leading 0
        if p[iResult[len(iResult) - 1]] == 0:
            continue
        if any(p[a] == 0 for a in iAddends[len(iAddends) - 1]):
            continue
        while i < len(iAddends):
            s = sum(p[a] for a in iAddends[i]) + carry
            carry = s // 10
            if p[iResult[i]] != s - carry * 10:
                break
            i = i + 1
        else:
            while i < len(iResult):
                oldCarry = carry
                carry = oldCarry // 10
                if p[iResult[i]] != oldCarry - carry * 10:
                    break
                i = i + 1
            else:
                return ''.join([str(p[charDigits.index(c)]) if c in charDigits else c for c in puzzle])

print(alphametics('KGKK + WMWDO + EMCKK + XEOGTEDE + KKMCWT + WKEKET + KEWCEW = XOMTDWMG'))
print(alphametics('THIS + A + FIRE + THEREFORE + FOR + ALL + HISTORIES + I + TELL + A + TALE + THAT + FALSIFIES + ITS + TITLE + TIS + A + LIE + THE + TALE + OF + THE + LAST + FIRE + HORSES + LATE + AFTER + THE + FIRST + FATHERS + FORESEE + THE + HORRORS + THE + LAST + FREE + TROLL + TERRIFIES + THE + HORSES + OF + FIRE + THE + TROLL + RESTS + AT + THE + HOLE + OF + LOSSES + IT + IS + THERE + THAT + SHE + STORES + ROLES + OF + LEATHERS + AFTER + SHE + SATISFIES + HER + HATE + OFF + THOSE + FEARS + A + TASTE + RISES + AS + SHE + HEARS + THE + LEAST + FAR + HORSE + THOSE + FAST + HORSES + THAT + FIRST + HEAR + THE + TROLL + FLEE + OFF + TO + THE + FOREST + THE + HORSES + THAT + ALERTS + RAISE + THE + STARES + OF + THE + OTHERS + AS + THE + TROLL + ASSAILS + AT + THE + TOTAL + SHIFT + HER + TEETH + TEAR + HOOF + OFF + TORSO + AS + THE + LAST + HORSE + FORFEITS + ITS + LIFE + THE + FIRST + FATHERS + HEAR + OF + THE + HORRORS + THEIR + FEARS + THAT + THE + FIRES + FOR + THEIR + FEASTS + ARREST + AS + THE + FIRST + FATHERS + RESETTLE + THE + LAST + OF + THE + FIRE + HORSES + THE + LAST + TROLL + HARASSES + THE + FOREST + HEART + FREE + AT + LAST + OF + THE + LAST + TROLL + ALL + OFFER + THEIR + FIRE + HEAT + TO + THE + ASSISTERS + FAR + OFF + THE + TROLL + FASTS + ITS + LIFE + SHORTER + AS + STARS + RISE + THE + HORSES + REST + SAFE + AFTER + ALL + SHARE + HOT + FISH + AS + THEIR + AFFILIATES + TAILOR + A + ROOFS + FOR + THEIR + SAFE = FORTRESSES'))