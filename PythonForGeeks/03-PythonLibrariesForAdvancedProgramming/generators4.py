"""
generators4.py:

    Created on 18-Dec-23
    
    @Author: Jean-François Ndi

    This example illustrates the use of pipelined generators i.e. the use of
    multiple generators use as a pipeline to achieve a goal.

"""
def prime_gen(num):
    """
    This function is a prime number generator.

    :param num: The upper limit of the generated prime number.
    :return: The generated prime number.
    """
    for cand in range(2, num):
        for i in range(2, cand):
            if cand  % i == 0:
                break
            else:
                yield cand


def x2_gen(list2):
    for num in list2:
        yield num * num

print(sum(x2_gen(prime_gen(27))))
