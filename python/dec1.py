def mobile(func):
    def inner(s):
        return sorted([func(i) for i in s])
    return inner

@mobile
def f(num):
    return "+91" + " " + num[-10:-5] + " " + num[-5:]

n = int(raw_input())
s = [raw_input() for _ in xrange(n)]
print "\n".join(f(s))