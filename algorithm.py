# Parsing Algorithm

from operations import OPERATIONS

# Parse the given barcode and return the decoded data
def parse_barcode(
    barcode: str,
    demo_mode: bool = False
) -> str:
    
    assert ((barcode.startswith("#") and barcode.endswith("#")) or barcode == "") == True
    
    blocks = barcode.split("#")
    
    if (demo_mode):
        count = 0
        print(f'\n{barcode}\n{"_" * len(barcode)}')
        print(f'{blocks}\n')
    
    for i in range(len(blocks)):
        
        for char in blocks[i]:
            
            if (demo_mode):
                if barcode[count] == "#":
                    count += 1
            
            if char in OPERATIONS:
                OPERATIONS[char](blocks, i)
                
                if (demo_mode):
                    print(f'\n{barcode}\n{"_" * count}{char}{"_" * (len(barcode) - count - 1)}')
                    print(f'Operation: {OPERATIONS[char].__name__.capitalize()}{" - Does Nothing For First Block" if i == 1 else ""}')
                    print(f'{blocks}\n')
                    
            if (demo_mode):
                count += 1
            
        assert (blocks[i].isdigit() or blocks[i] == "") == True
            
    data = "".join(blocks)
    
    assert (data.isdigit() or data == "") == True
            
    return data