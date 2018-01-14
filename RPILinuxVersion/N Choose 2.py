import itertools
itertools.combinations('abcd',2)
print(list(itertools.combinations('abcd',2)))
print([''.join(x) for x in itertools.combinations('abcd',2)])
