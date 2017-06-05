# https://www.hackerrank.com/challenges/most-commons
from collections import Counter

chars = Counter(raw_input()).items()

for ch_, n in sorted(chars, key=lambda c: (-c[1], c[0]))[:3]:
    print ch_, n
