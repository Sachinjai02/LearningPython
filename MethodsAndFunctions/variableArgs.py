def myfunc(n1, n2):
    """
    Returns 5% of the sum of n1 and n2
    :param n1:
    :param n2:
    :return:
    """
    return sum((n1, n2)) * 0.05


def myfunc_varargs(*args):
    print(args)


def myfunc_kwargs(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fav fruit is ' + kwargs['fruit'])
    else:
        print('No fruit found')


def myfunc_allargs(*args, **kwargs):
    print(args)
    print(kwargs)


def convert(stri):
    out = ''
    for idx, l in enumerate(stri):
        print(f'{idx} {l}')
        print(type(l))

        if idx % 2 == 0:
            out = out + l.upper()
            print(out)
        else:
            out = out + l.lower()
            print(out)
    return out


def summer_69(arr):
    sumN = 0
    flag = True
    for n, el in enumerate(arr):
        if el == 6:
            flag = False
        elif el == 9 and flag == False:
            flag = True
        elif flag == True:
            sumN += el
    return sumN


print(summer_69([2, 1, 6, 9, 11]))
print(convert('sachin'))
print(convert('sachin'))
myfunc_varargs(2, 3, 4, 5, 6)
myfunc_kwargs(fruit='Pineapple', veggie='Lettuce')
myfunc_allargs(1, 2, 3, 4, 5, 6, 7, 8, name='Sachin', org='ABC', phNumber='233567787')
