import re
s = [
          "X-Sieve: CMU Sieve 2.3",
          "X-DSPAM-Result: Innocent",
          "X-DSPAM-Confidence: 0.8475",
          "X-Content-Type-Message-Body text/plain",
          "X-Plane is behind schedule: two weeks"
]

print("Match with ^X.*:")
for line in s:
          if re.search('^X.*:', line):
                    print(line)

print("Match with ^X-\S+:")
for line in s:
          if re.search('^X-\S+:', line):
                    print(line)