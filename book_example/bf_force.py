def bf_match(txt, pat):
    pt, pp = 0, 0

    while pt < len(txt) and pp < len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0
        return pt-pp if len(pat) == pp else -1