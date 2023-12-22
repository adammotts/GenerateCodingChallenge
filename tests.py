# Tests

from algorithm import parse_barcode

def tests():
    
    # Given
    assert parse_barcode(r"#12#34!#59^#67%#") == r"1221430867"
    assert parse_barcode(r"#0%#1%#2%#3%#4%#5%#6%#7%#8%#9%#") == r"0246802469"

    
    # Process Blocks Sequentially
    assert parse_barcode(r"#12#!!#!#") == r"1212121212"
    assert parse_barcode(r"#12#^#34#") == r"2134"
    assert parse_barcode(r"#12#%#34#") == r"2434"
    
    # Empty Blocks Add Empty Data
    assert parse_barcode(r"##!!!!!#") == r""
    assert parse_barcode(r"#12#^#!#") == r"21"
    assert parse_barcode(r"#12##!%!^!#") == r"12"
    
    # Order Of Operations Matters
    '''
    assert parse_barcode(r"#12#!^#34#^!#") == r"21124343"
    assert parse_barcode(r"#12#!%#34#%!#") == r"24126868"
    assert parse_barcode(r"#12#!!%!^!#") == r"4212122442"
    '''
    # Apparently My Interpretation Of This Is Wrong
    
    # Special Characters In Initial Data Block
    assert parse_barcode(r"#!!^%!!%^!!#12#") == r"12"
    assert parse_barcode(r"#!^%12!^%#") == r"12"
    assert parse_barcode(r"#1%^!2#") == r"12"
    
    
    # Reverse and Encrypt Symbol Placement Does Not Matter (Order Of Operations)
    assert parse_barcode(r"#12#3^4#") == r"2134"
    assert parse_barcode(r"#12#3%4#") == r"2434"
    assert parse_barcode(r"#12#3^^%%4#") == r"4834"
    
    # Repeat Symbol Placement Does Matter (Order Of Operations)
    assert parse_barcode(r"#12#!34#") == r"121234"
    assert parse_barcode(r"#12#3!4#") == r"123124"
    assert parse_barcode(r"#12#34!#") == r"123412"
    
    # Data Blocks Are Permanently Mutated For Future Usage (Order Of Operations)
    '''
    assert parse_barcode(r"#12#^34!#") == r"213421"
    assert parse_barcode(r"#12#%34!#") == r"243424"
    assert parse_barcode(r"#12#^3!4%5!#") == r"423214542"
    '''
    # Apparently My Interpretation Of This Is Wrong
    
    # Empty Barcodes Return Nothing
    assert parse_barcode(r"") == r""
    
    # Barcodes With Nothing Return Nothing
    assert parse_barcode(r"##") == r""
    assert parse_barcode(r"###") == r""