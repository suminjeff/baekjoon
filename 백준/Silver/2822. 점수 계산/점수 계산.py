
scores = []
for i in range(8):
    score = int(input())
    scores.append((score, i + 1))

scores.sort(reverse=True, key=lambda x: x[0])

top_scores = scores[:5]

total_score = sum(score for score, _ in top_scores)

problem_numbers = sorted(problem for _, problem in top_scores)

print(total_score)
print(*problem_numbers)
