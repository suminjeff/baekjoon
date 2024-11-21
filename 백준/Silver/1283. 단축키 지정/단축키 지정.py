import sys


def transform(option, word_idx, letter_idx):
    result = []
    for i in range(len(option)):
        word = option[i]
        if i == word_idx:
            word = list(word)
            word.insert(letter_idx+1, "]")
            word.insert(letter_idx, "[")
            result.append("".join(word))
        else:
            result.append(word)
    return result


def solve(n: int, options: list[str]) -> list:
    answer = []
    shortcut = [0]*26

    for i in range(n):
        option = options[i].split()
        rule = False
        for j in range(len(option)):
            word = option[j]
            first_letter = word[0].upper()
            idx = ord(first_letter) - ord('A')
            if shortcut[idx] == 0:
                shortcut[idx] = 1
                answer.append(" ".join(transform(option, j, 0)))
                rule = True
                break
        if rule:
            continue
        for j in range(len(option)):
            word = option[j]
            for k in range(len(word)):
                letter = word[k].upper()
                idx = ord(letter) - ord('A')
                if shortcut[idx] == 0:
                    shortcut[idx] = 1
                    answer.append(" ".join(transform(option, j, k)))
                    rule = True
                    break
            if rule:
                break
        if rule:
            continue
        answer.append(" ".join(option))

    return answer


if __name__ == "__main__":
    N = int(input())
    OPTIONS = [input() for _ in range(N)]
    ANSWER = solve(N, OPTIONS)
    print(*ANSWER, sep='\n')
