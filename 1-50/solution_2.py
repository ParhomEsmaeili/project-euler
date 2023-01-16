import argparse

def parser_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--upper_lim',
                        type=int,
    )
    args = parser.parse_args()
    return args

#Even Fibonacci Sum Program. By induction we prove that every third Fibonacci number is even. If we denote F_{3n} as the Fibonnaci
#number for the (3n)th term in the Fibonacci sequence, we have that for n = 1, this is true since F_3 = F_2 + F_1 = 1 + 1 = 2.

#We assume it is true for F_{3k} (i.e. where n = k), then for F_{3(k+1)} = F_{3k + 2} + F_{3k + 1} = F_{3k + 1} + F_{3k} + F_{3k+1}
#Therefore F_{3(k+1)} = 2F_{3k+1} + F_{3k}, which is therefore even. Since the assumption that it is true for n = k, implies true
#for n = k + 1, and that it is true for n = 1. We therefore have that it is true for all integer n. 

#Secondly, we can use substitution to obtain the expression for F_{3n} as follows: F_{3n} = 3F_{3n - 3} + 2F_{3n - 4}. This implies
#the next even Fibonnaci is the sum of 3 times the prior even and 2 times the fibonacci number before the prior even. We can also
#obtain an expression using substitution for the fibonacci number before an even, F_{3n - 1} as follows: 
#F_{3n - 1} = 2F_{3n - 3} + F_{3n - 4}. 

#Therefore, we can iteratively compute and store F_{3n} and F_{3n - 1} simultaneously, to use for the next pair. 

def even_fibonacci_total(n):
    '''Input: n, the maximum for the even Fibonacci numbers.'''
    
    f_3n_3, f_3n_4 = 2,1
    #f_3n_3 and f_3n_4 denote F_{3n-3} and F_{3n-4} respectively. We initialise these values at 2 and 1 respectively because the first even
    # value is 2, and the prior fibonacci value is 1. We also initialise the total at 2, since the first even fibonacci value is 2. 
    
    fibonacci_total = 2 
    
    while True:
        # F_{3n} is not stored separately, it is just stored under f_3n_3 implicitly to reduce storage requirements.
        f_3n_3, f_3n_4 = 3 * f_3n_3 + 2 * f_3n_4, 2 * f_3n_3 + f_3n_4

        if f_3n_3 > n or f_3n_4 > n:
            break 
        fibonacci_total += f_3n_3
        
    

    return fibonacci_total

def main(args):
    print(even_fibonacci_total(args.upper_lim))

if __name__=="__main__":
    args = parser_arguments()
    main(args)
    