words = [q.lower().replace(".", "").replace(",", "") for q in ga]
unique_words = set(words)
count = {}
for uw in unique_words:
    count[uw] = words.count(uw)

count

count = {}
for uw in unique_words:
    count[uw] = words.count(uw)

count
c = {uw: count[uw] for uw in unique_words}
