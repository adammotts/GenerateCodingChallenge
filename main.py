# Generate Coding Challenge - Algorithm

from route import ENDPOINT, register_user, forgot_token, get_challenge, submit_solution
from algorithm import parse_barcode
from tests import tests

NAME = "Adam Ma"
NUID = "002942147"

def main():
    
    '''
    token, challenge = register_user(
        ENDPOINT,
        NAME,
        NUID
    )
    '''

    token = forgot_token(
        ENDPOINT,
        NUID
    )
    
    challenge = get_challenge(
        ENDPOINT,
        token
    )
        
    decoded_data = [parse_barcode(barcode) for barcode in challenge]
    
    correct, feedback = submit_solution(
        ENDPOINT,
        decoded_data,
        token
    )
    
    print(f'{feedback}')
    
    assert correct == True


if __name__ == "__main__":
    tests()
    main()