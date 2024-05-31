def cached(func):
    journal = {}

    def decorated_func(*args, **kwargs):
        nonlocal journal
        allargs = tuple(args) + tuple(kwargs)
        if tuple(allargs) in journal:
            result = journal[allargs]
            #print("сохранённое зачение: ", result)
        else:
            journal[allargs] = func(*args, **kwargs)
            result = journal[allargs]
        return result
    return decorated_func
