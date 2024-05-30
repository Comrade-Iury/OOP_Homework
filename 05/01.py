PRINT = print


def louder_print(*args, **kwargs):
    loud_font = [str(arg).upper() for arg in args]
    PRINT(*loud_font, **kwargs)


print = louder_print
