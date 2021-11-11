def cipher(text, shift, encrypt=True):

    """
    This is a package to encrypt sth.
    Caesar cipher is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
    
    Inputs
    ------
    text: str. A set of string we want to encrypt or decrypt.
    shift: int. The process and location we want the cipher to encrypt or decrypt words in the alphabet.
    encrypt: boolean. Encrypt if True. Decrypt if False.
    
    Outputs
    -------
    test: string after being encrypted or decrypted.
    
    Examples of encrypting and decrypting
    -------------------------------------
    >>> from cipher_sw3614 import cipher_sw3614
    >>> text = 'bread'
    >>> shift = 1
    >>> cipher_sw3614.cipher(“bread”,1)
    csfbe
    
    """


    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
