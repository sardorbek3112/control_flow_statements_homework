def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a//100==0 and a//10!=0:
        if a%2==0:
            return "two-digit even number"
        else:
            return "two-digit odd number"
    else:
        if a%2==0:
            return "three-digit even number"
        else:
            return "three-digit odd number"