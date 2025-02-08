def judge_hero_name(hero_name: str) -> str:
    g_count = hero_name.lower().count('g')
    b_count = hero_name.lower().count('b')

    if g_count > b_count:
        result = "GOOD"
    elif g_count < b_count:
        result = "A BADDY"
    else:
        result = "NEUTRAL"

    return f"{hero_name} is {result}"


def main():
    n = int(input())  
    for _ in range(n):
        hero_name = input().strip()
        print(judge_hero_name(hero_name))


if __name__ == "__main__":
    main()
