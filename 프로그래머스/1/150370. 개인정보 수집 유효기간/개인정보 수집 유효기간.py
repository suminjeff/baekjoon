def solution(today, terms, privacies):

    answer = []
    year, month, day = map(int, today.split("."))
    today = year*12*28 + month*28 + day
    for idx, privacy in enumerate(privacies):
        start_date, term_type = privacy.split()
        year, month, day = map(int, start_date.split("."))
        start_date = year*12*28 + month*28 + day
        for term in terms:
            term_policy, duration = term.split()
            duration = int(duration) * 28
            if term_type == term_policy and start_date + duration <= today:
                answer.append(idx+1)

    return answer