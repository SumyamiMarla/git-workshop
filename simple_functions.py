# Custom python functions

def double_number(a):
    '''
    This function doubles the number given as argument
    params int a: number to be doubled.
    '''
    print(f'value before double_number(): {a}')
    result=a+a
    print(f'value after double_number(): {result}')

def square_number(a):
    '''
    This function squares the number given as argument
    params int a: number to be squared.
    '''
    print(f'value before square_number(): {a}')
    result=a*a
    print(f'value after square_number(): {result}')