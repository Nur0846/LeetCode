def longestspecifickdistinct(s, k):
    max_length = 0
    l = 0
    r = 0
    mpp = {}

    while r < len(s):
        # add character safely
        mpp[s[r]] = mpp.get(s[r], 0) + 1

        # shrink window if needed
        while len(mpp) > k:
            mpp[s[l]] -= 1
            if mpp[s[l]] == 0:
                del mpp[s[l]]
            l += 1

        # update result
        max_length = max(max_length, r - l + 1)

        r += 1

    return max_length
