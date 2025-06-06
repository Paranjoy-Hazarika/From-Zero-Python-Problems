msg = "Hello human"

counts = {}

for i in msg.lower():
    if i == " ":
        continue
    if i not in counts:
        counts[i] = 1
        continue

    counts[i] += 1

for i, values in enumerate(counts, 1):
    print(f"{i}. {values} - {counts[values]}")