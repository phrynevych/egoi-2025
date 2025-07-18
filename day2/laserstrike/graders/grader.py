import sys

def first_error(verdicts):
    for verdict in verdicts:
        if verdict != 'AC':
            return verdict
    return 'AC'

assert sys.argv[1] == "rescale"
rescale_from = int(sys.argv[2])
rescale_to = int(sys.argv[3])

data = sys.stdin.read().split()
verdicts = data[0::2]
scores = list(map(float, data[1::2]))
assert len(verdicts) == len(scores)

verdict = first_error(verdicts)
score = min(scores)

score = score * rescale_to / rescale_from

# Round to nearest integer, per problem statement
# (rounding x.5 up, rather than to even as Python's round() function does)
score = int(score + 0.49999999999999994)

print('%s %f' % (verdict, score))
