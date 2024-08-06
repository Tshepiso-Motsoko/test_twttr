from twttr import shorten

def test_shorten():
    assert shorten('hello') == 'hll'
    assert shorten('world') == 'wrld'
    assert shorten('twttr') == 'twttr'  # No vowels in the word
    assert shorten('AEIOU') == ''  # All characters are vowels
    assert shorten('aeiou') == ''  # All characters are vowels
    assert shorten('') == ''  # Empty string
    assert shorten('The quick brown fox jumps over the lazy dog') == 'Th qck brwn fx jmps vr th lzy dg'
    assert shorten('hello1') == 'hll1'  # Numbers should not be omitted
    assert shorten('hello, world!') == 'hll, wrld!'  # Punctuation should not be omitted
