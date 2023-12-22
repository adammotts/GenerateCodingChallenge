# Parsing Algorithm

from operations import OPERATIONS

# Parse the given barcode and return the decoded data
def parse_barcode(
    barcode: str,
    demo_mode: bool = False
) -> str:
    
    # Valid barcodes must start and end with "#" (or be empty)
    assert ((barcode.startswith("#") and barcode.endswith("#") and len(barcode) > 1) or barcode == "") == True
    
    # Split the barcode into blocks of data
    blocks = barcode.split("#")
    
    if (demo_mode):
        count = 0
        print(f'\n{barcode}\n{"_" * len(barcode)}')
        print(f'{blocks}\n')
    
    # Nested for loop to iterate through each block and character
    for i in range(len(blocks)):
        for char in blocks[i]:
            
            if (demo_mode):
                if barcode[count] == "#":
                    count += 1
            
            # For each character, check if it is an operation symbol. If so, apply
            if char in OPERATIONS:
                OPERATIONS[char](blocks, i)
                
                if (demo_mode):
                    print(f'\n{barcode}\n{"_" * count}{char}{"_" * (len(barcode) - count - 1)}')
                    print(f'Operation: {OPERATIONS[char].__name__.capitalize()}{" - Does Nothing For First Block" if i == 1 else ""}')
                    print(f'{blocks}\n')
                    
            if (demo_mode):
                count += 1
            
        # After applying all operations, the resultant block should no longer contain any symbols
        assert (blocks[i].isdigit() or blocks[i] == "") == True
            
    # Join the blocks back together to form the decoded data
    data = "".join(blocks)
    
    # After processing the barcode, the resultant data should no longer contain any symbols
    assert (data.isdigit() or data == "") == True
            
    return data