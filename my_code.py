# my_code.py
import sys

def extra_function():
    pass
 
def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
 
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    # if-else
 
 
# def factorial_recursive
 
 
def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
 
    if n == 0:
        return 1
    else:
        mult = 1
        # range(1, n+1) is the interval [1,n]
        for factor in range(1, n + 1):
            mult *= factor
        # for
        return mult
    # if-else
# def factorial_iterative
 
# print("Start")
 
b_am_i_being_called_from_the_cli = __name__ == "__main__"
 
if b_am_i_being_called_from_the_cli:
    # à confiança a ir buscar o argumento no index 1
    # como se garantidamente a chamada fosse feita assim:
    # python3 my_code.py um-nº-aqui
 
    # we are trusting that the user always provides number
    # maybe that will NOT always happen
 
    # caution!!!
    b_a_number_was_sent = len(sys.argv)>=2
    if b_a_number_was_sent:
        r = received_number_from_the_cli = int(sys.argv[1])
 
        fi = factorial_iterative(
            received_number_from_the_cli
        )
 
        fr = factorial_recursive(
            received_number_from_the_cli
        )
 
        msg = f"Received {r}\nfi={fi}\nfr={fr}\n"
        print(msg)
    else:
        print("Please provide a number")