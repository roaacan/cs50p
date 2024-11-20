def f(*args, **kwargs):
    print(kwargs)


def total(galleons=0, pickles=0, knuts=0):
    return (galleons * 17 + pickles) * 29 + knuts


coins = {"galleons": 100, "pickles": 50, "knuts": 10} # Orden no afecta
print(total(**coins))

f(name="Rony", age=12)