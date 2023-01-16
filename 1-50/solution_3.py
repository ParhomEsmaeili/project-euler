import argparse 

def parser_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_val',
                        type=int,
    )
    args = parser.parse_args()
    return args


def prime_factors(val):
    '''
    Input: val, the value for which the prime factors are being found.'''
    #We will loop, and check whether each successive value is a divisible factor of the input value or not.
    factors_list = []
    current_divisible_factor = 2
    
    #We will do this while val > 1, if val <= 1 then there are no more divisible factors anyways.
    while val > 1:
        #we will factor out a given prime factor as many times as possible, i.e. as long as we continuously factor out a 
        #prime factor, but it is still a factor of the given value, then continue to factor it out. E.g. 36 = 2 * 2 * 3 * 3, 
        #we would factor out a factor of 2 twice, leaving only 9. Which we then check next for prime factors. 
        
        while val % current_divisible_factor == 0:
            factors_list.append(current_divisible_factor)
            val /= current_divisible_factor
        
        #Once we have exhausted the amount of factors we can extract, we move onto the next integer, until it finds another suitable divisible factor.
        current_divisible_factor += 1

        #In order to avoid excessive amount of loops, we can also terminate early. If our current divisible factor being tested is larger than the square 
        #root of the altered input value (after we have divided through by factors throughout this process), then we can have no more factors since a larger prime factor is impossible. 
        if current_divisible_factor ** 2 > val:
            if val > 1:
                factors_list.append(val)
                #If val > 1, then the current value must also be a prime factor, because we have exhausted all possible factors of the current value already thus far. 

            break 
       
    return factors_list

def main(input_value):
    sorted_factors_list = sorted(prime_factors(input_value))
    largest_prime_factor = sorted_factors_list[-1]
    return largest_prime_factor

if __name__=='__main__':
    args = parser_arguments()
    print(main(args.input_val))
