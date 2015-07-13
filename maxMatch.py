# Find the best match
#       % python maxMatch.py pat text1 

import sys      # Used for Command Line Parameters

# How many characters match in this position?
def score(pat, text):
    """How many characters match?"""
    count = 0;
    # Compare each character in the pattern with matching element in text
    for x in xrange(len(pat)):
        # Was there a match
        if (text[x] == pat[x]):
            count = count + 1

    return count

# Find the best match
def  maxMatch(pat, text):
    """Look for the best match for pat in the string text."""
    best = -1
    spot = -1
    ln = len(pat)
    # Try each possible starting spot in text
    for x in xrange(len(text) - ln + 1):
        result = score(text[x:x+ln], pat);
        if (result > best):
            print "New best score", result, text[x:x+ln]
            best = result
            spot = x

    return spot

if (len(sys.argv) < 3):
    print "Usage:   python", sys.argv[0], "<pattern> <text>"
else:
    pattern = sys.argv[1]
    text    = sys.argv[2]
    print maxMatch(pattern, text)
