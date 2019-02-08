import string_matches as match


def test_string_matches():
    assert match.find_longest('ABAXDC', 'BACBAD') == 'ABAD'
    assert match.find_longest('aaaa', 'aa') == 'aa'
    assert match.find_longest('AGGTAB', 'GCTXAYB') == 'GTAB'
    assert match.find_longest('seanbudhram', 'sxecadn') == 'sean'
    assert match.find_longest(
        'seanbudhram', 'seanbudhram') == 'seanbudhram'
