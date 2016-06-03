# License MIT Ahmad Retha 2016

def naive(t, n, p, m):
    for i in range(n - m + 1):
        matchLen = 0
        for j in range(m):
            if t[i + j] == p[j]:
                matchLen += 1
                if matchLen == m:
                    print "Match found at pos: %d" % (i)
            else:
                break

def prefix_table(p, m):
    pt = [0] * m
    i = 1
    matchLen = 0
    while i < m:
        while i < m and p[i] == p[matchLen]:
            matchLen += 1
            pt[i] = matchLen
            i += 1
        matchLen = 0
        i += 1
    return pt

def KMP(t, n, p, m):
    i = 0
    while i < n - m + 1:
        j = 0
        matchLen = 0
        while j < m:
            if t[i + j] == p[j]:
                matchLen += 1
                if matchLen == m:
                    print "Match found at pos: %d" % (i)
                    i += 1
                    break
                j += 1
            elif matchLen > 0 and lookup[matchLen] > 1:
                i = i + lookup[matchLen]
                break
            else:
                i += 1
                break

t = "bacbababaabcbababababca"
n = len(t)
p = "abababca"
m = len(p)

print "Finding p in t:"
print
print "t = ", t
print "p = ", p
print

print "Naive algorithm result:"
naive(t, n, p, m)
print

print "KMP algorithm prefix_table:"
lookup = prefix_table(p, m)
print lookup
print

print "KMP algorithm result:"
KMP(t, n, p, m)
