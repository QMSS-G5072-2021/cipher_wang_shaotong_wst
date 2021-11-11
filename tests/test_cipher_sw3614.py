from cipher_sw3614 import cipher_sw3614
import pandas as pd

def test_cipher_single():
    actual = cipher_sw3614.cipher('bread',1)
    expected = 'csfbe'
    assert actual == expected
