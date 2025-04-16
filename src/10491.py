# Quite a problem
# https://www.acmicpc.net/problem/10491
# 문자열, 파싱

# =======================================
import sys, re

for line in sys.stdin:
    line = line.rstrip().lower()
    print("yes" if re.search('problem', line) else "no")
