# Generate Coding Challenge - Algorithm

from route import ENDPOINT, register_user, forgot_token, get_challenge, submit_solution
from algorithm import parse_barcode
from tests import tests
import random

NAME = "Adam Ma"
NUID = "002942147"

def main():
    
    try:
        token, challenge = register_user(
            ENDPOINT,
            NAME,
            NUID
        )

    except:
        token = forgot_token(
            ENDPOINT,
            NUID
        )
        
        challenge = get_challenge(
            ENDPOINT,
            token
        )
        
    decoded_data = [parse_barcode(barcode) for barcode in challenge]
    
    # View Of All Barcodes -> Decoded Data
    '''
    print("\n".join(f'{barcode} -> {data}' for barcode, data in zip(challenge, decoded_data)))
    '''
    
    # Random Example
    print(f'\nEnd Result: "{parse_barcode(challenge[random.randint(0, len(challenge) - 1)], demo_mode=True)}"\n\n')
    
    correct, feedback = submit_solution(
        ENDPOINT,
        decoded_data,
        token
    )
    
    print(f'{feedback}\n\n')
    
    assert correct == True


if __name__ == "__main__":
    tests()
    main()