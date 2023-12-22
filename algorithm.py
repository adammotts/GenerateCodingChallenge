# Parsing Algorithm

from operations import OPERATIONS

# Parse the given barcode and return the decoded data
def parse_barcode(
    barcode: str
) -> str:
    
    # Valid barcodes must start and end with "#" (or be empty)
    assert ((barcode.startswith("#") and barcode.endswith("#") and len(barcode) > 1) or barcode == "") == True
    
    # Split the barcode into blocks of data
    blocks = barcode.split("#")
    
    # Nested for loop to iterate through each block and character
    for i in range(len(blocks)):
        
        # Keep the initial state of the previous block stored so that future usages use this, instead of any post mutation states
        previous_block_initial_state = blocks[i-1]
        
        for char in blocks[i]:
            
            # For each character, check if it is an operation symbol. If so, apply
            if char in OPERATIONS:
                OPERATIONS[char](blocks, i, previous_block_initial_state)
            
        # After applying all operations, the resultant block should no longer contain any symbols
        assert (blocks[i].isdigit() or blocks[i] == "") == True
            
    # Join the blocks back together to form the decoded data
    data = "".join(blocks)
    
    # After processing the barcode, the resultant data should no longer contain any symbols
    assert (data.isdigit() or data == "") == True
            
    return data