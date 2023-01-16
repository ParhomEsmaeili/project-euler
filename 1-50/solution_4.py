import argparse

def parser_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-values',
                        '--upper_and_lower_vals',
                        action = 'append',
                        help = 'Generates a list containing info about the upper and lower bounds from which to loop'
                        )
    args = parser.parse_args()
    return args

def is_palindrome(val):
    string_form = str(val)
    return string_form == string_form[::-1]

def largest_palindrome_search(n_up, n_low):
    '''
    n_up is the largest value the numbers we can have in the products
    n_low is the smallest value the numbers we can have'''

    current_max = 0

    for i in range(n_up - 1, n_low, -1):
        for j in range(i, n_low, -1):
            #By starting at i for the loop in j, we will skip any repeats and save time in computation. 
            product = i * j

            if is_palindrome(product):
                if product > current_max:
                    current_max = product


    return current_max

def main(args):
    n_up, n_low = int(args.upper_and_lower_vals[0]), int(args.upper_and_lower_vals[1])
    largest_palindrome = largest_palindrome_search(n_up, n_low)
    return largest_palindrome

if __name__ == '__main__':
    args = parser_arguments()
    print(main(args))