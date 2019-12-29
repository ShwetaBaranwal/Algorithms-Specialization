3141592653589793238462643383279502884197169399375105820974944592

2718281828459045235360287471352662497757247093699959574966967627

def func(x,y):
    n_digits = len(str(x))
    n_digits = n_digits-1 if n_digits%2!=0 else n_digits
    a = x/(pow(10, (n_digits/2)))
    b = x%(pow(10, (n_digits/2)))
    c = y/(pow(10, (n_digits/2)))
    d = y%(pow(10, (n_digits/2)))
    a_plus_b = a + b
    c_plus_d = c + d
    ac = a*c if ((len(str(a))==1) or (len(str(c))==1)) else func(a, c)
    bd = b*d if ((len(str(b))==1) or (len(str(d))==1)) else func(b, d)
    sum_mul = a_plus_b * c_plus_d if ((len(str(a_plus_b))==1) or (len(str(c_plus_d))==1)) else func(a_plus_b, c_plus_d)
    sub = sum_mul - ac - bd
    res = (pow(10, n_digits) * ac) + (pow(10, (n_digits/2)) * sub) + bd
    # print (x, y, a, b, c, d, res, x*y, n_digits)
    return res
