# Operations

def repeat(
    blocks: list[str],
    index: int,
    previous_block_initial_state: str
) -> None:
    
    assert index != 0
    
    # Repeat the previous block of data (the original state, not any mutated state)
    blocks[index] = blocks[index].replace("!", previous_block_initial_state, 1)
    
def reverse(
    blocks: list[str],
    index: int,
    previous_block_initial_state: str
) -> None:
    
    assert index != 0
    
    blocks[index] = blocks[index].replace("^", '', 1)

    # Reverse the previous block of data
    blocks[index-1] = blocks[index-1][::-1]
    
def encrypt(
    blocks: list[str],
    index: int,
    previous_block_initial_state: str
) -> None:
    
    assert index != 0
    
    blocks[index] = blocks[index].replace("%", '', 1)
                
    # Parse each character as a digit, double, take the ones digit, then convert back into string
    blocks[index-1] = "".join([str((int(char) * 2) % 10) for char in blocks[index-1]])


OPERATIONS = {"!": repeat, "^": reverse, "%": encrypt}