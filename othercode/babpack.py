# Babylonian Root Finding Package
#
#created by Ima Somma Hacka 23 Feb 2007
#
#revised by Heeza Betah Codah 15 Mar 2007
#
def next_iteration(x, a):
    xnew = 0.5 * (x + a/x)
    return xnew
def findaroot(a, err=10**-10, debug=False):
    xold = a
    error = float("inf")
    while error > err:
        x=next_iteration(xold, a)
        error = abs(x-xold)
        xold = x
        if debug: print(x, error)
    return x