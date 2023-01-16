from math import floor
import argparse

def parser_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--upper_lim',
                        type=int,
    )
    args = parser.parse_args()
    return args



def count_multiples(n=int, multiple=int):
    ratio = n/multiple
    if (ratio).is_integer():
        return ratio - 1
    else:
        return floor(ratio)

def multiples_sum(n=int):
    '''
    Input: int: n - The integer which we are finding the sum up to
    '''
    #We will use the fact that we can find arithmetic series sums with relative ease, to do so we recall that we just need
    #to find the number of multiples of 3, or 5, from 0 to n. E.g between 0 and 1000, we will have 333. 

    #If n/factor is not an integer, then this value is given by floor(n/factor). If it is an integer, then exclusive of n, we have
    #integer - 1 multiples.

    #upper index limit of multiples of 3, 5 and 15 respectively:
    upper_index_three = count_multiples(n, 3)
    upper_index_five = count_multiples(n, 5)
    upper_index_fifteen = count_multiples(n, 15)
    
    print(upper_index_three)
    print(upper_index_five)
    print(upper_index_fifteen)

    #sum is given by 1/2 n(n+1) 
    multiple_of_three_sum = (3/2) * (upper_index_three * (upper_index_three + 1))
    multiple_of_five_sum = (5/2) * (upper_index_five * (upper_index_five + 1))
    multiple_of_fifteen_sum = (15/2) * (upper_index_fifteen * (upper_index_fifteen + 1))

    #For the sum of multiples of 3 and 5, we sum the two separate and subtract the intersection:

    return multiple_of_three_sum + multiple_of_five_sum - multiple_of_fifteen_sum


def main():
    args = parser_arguments()
    n = args.upper_lim
    return multiples_sum(n)

if __name__=="__main__":
    total_sum = main()
    print(total_sum)