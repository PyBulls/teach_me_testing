
def to_upper(instr):
    r"""1l: accepts a str and ret that string's ``upper()``

    Longer Description:  
    string converted to UPPER case
    # ProTip: prepend r to avoid / problems
    
        >>> to_upper("foo")
        'notfoo'

        >>> to_upper("foo")
        'FOO'
    
    test mixed case

        >>> to_upper("fOo")
        'FOO'

        >>> type(to_upper("foo")) == str
        True

        >>> type(to_upper("foo")) is str
        True

        >>> isinstance(to_upper("foo"),str)
        True

    """
    return instr.upper()

def strip_and_upper(instr):
    r"""
        >>> strip_and_upper("FooBar\n")
        'FOOBAR'
    """    
    return to_upper(instr).strip()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print "Running tests..."


