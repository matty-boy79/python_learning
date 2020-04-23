"""
I DON'T UNDERSTAND THIS!!!!
"""


def tri_recursion(k):
    if k > 0:
        print("k={}".format(k))

        result = k + tri_recursion(k - 1)

        print("result={}".format(result))

    else:
        result = 0

    return result


print("Recursion Example Results")
tri_recursion(3)
