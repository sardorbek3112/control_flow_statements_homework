def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    i=0
    j=0
    if a>0:
        i+=1
    if b>0:
        i+=1
    if c>0:
        i+=1
    if a<0:
        j+=1
    if b<0:
        j+=1
    if c<0:
        j+=1
    if i>j:
        return "there are a lot of positive numbers"
    return "there are a lot of negative numbers"
    