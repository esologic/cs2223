from timeit import timeit

n = 10000


def linear():
    for x in range(n):
        pass


def quadratic():
    for x in range(n):
        for y in range(n):
            pass


def cubic():
    for x in range(n):
        for y in range(n):
            for z in range(n):
                pass


if __name__ == "__main__":

    names = ["Linear", "Quadratic", "Cubic"]
    functions = [linear, quadratic, cubic]

    for name, function in zip(names, functions):
        execution_time = (timeit(function, number=1)*1000000)
        print("It took the " + name + " function " + str(execution_time) + " ms to execute.")
