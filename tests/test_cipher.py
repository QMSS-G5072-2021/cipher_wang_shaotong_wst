import pytest
def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    assert isinstance(shift,str) == False, "Shift cannot be strings"
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

def test_cipher_single():
    actual = cipher('bread',1)
    expected = 'csfbe'
    assert actual == expected

def test_cipher_negative():
    actual = cipher('dog',-1)
    expected = 'cnf'
    assert actual == expected

def test_cipher_none():
    actual = cipher('@jessica',1)
    expected = '@kfttjdb'
    assert actual == expected

def test_cipher_exception_string():
    with pytest.raises(AssertionError):
        cipher('dog','one')