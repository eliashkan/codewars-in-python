def accum(s):
    letters = [];
    for count, value in enumerate(s):
        letters.append(((count + 1)*value).capitalize());
    return '-'.join(letters);

def accum(s):
    return '-'.join([((count + 1)*value).capitalize() for count, value in enumerate(s)]);