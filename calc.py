from pprint import pprint


def calculate(cur_line):
    global variables
    try:
        return eval(cur_line, variables)
    except Exception:
        return


def gcd(a, b):
    if not b:
        return a
    else:
        return gcd(b, a % b)


def invalid_message():
    print("Invalid operation.")
    print("Try 'help' to see your options")


variables = dict()
line = ''
while True:
    line = input('>> ').strip()
    # empty line
    if not line:
        continue
    elif line == "exit":
        break
    # help message
    elif line == "help":
        tabs = "___"
        print("Use:")
        print(f"{tabs}'?' to see all created variables")
        print(f"{tabs}'? <name>' to see <name> value if it exists")
        print(f"{tabs}'<name> = <value>' to:")
        print(f"{tabs * 2}create variable as <name> with <value>")
        print(f"{tabs * 2}or set <value> to existing variable <name>")
        print(f"{tabs}'primes of <value>' to decompose it into primes")
        print(f"{tabs}'<value> <operation> <value>' to calculate :)")
        print("so, just try everything, i don`t know, how it works")
        print("the scientific poke method will help you! I hope....")

    # add variable
    elif "=" in line:
        expression = [el.strip(" ") for el in line.split('=')]
        # checking correctness of name
        if expression[0].isdigit():
            print('Don`t name the variables as digits.')
            continue
        # if value is int
        if expression[-1].isdigit():
            variables[expression[0]] = float(expression[-1])
        # if variables in value
        else:
            answer = calculate(expression[-1])
            if answer:
                variables[expression[0]] = answer
            else:
                invalid_message()
    # see variables
    elif line[0] == "?":
        if line == "?":
            if "__builtins__" in variables:
                variables.pop("__builtins__")
            pprint(variables)
        else:
            key = line[1:].split()[-1]
            print(key, "=", variables.get(key))
    elif line[:9] == "primes of":
        n = None
        try:
            n = float(line[9:])
        except ValueError:
            if line[9:].strip() in variables:
                n = variables[line[9:].strip()]
            else:
                invalid_message()
                continue
        if n < 0:
            print("Incorrect value to decompose number (should be >= 0)")
            continue
        primes = []
        for i in range(2, min(n, round(n ** 0.5) + 1)):
            while n % i == 0:
                primes.append(i)
                n //= i
        if n != 1:
            primes.append(n)
        primes.sort()
        print(" * ".join([str(el) for el in primes]))
    elif line[:3] == "gcd":
        f_str, s_str = [el for el in line[3:].split()]
        try:
            a = float(f_str)
        except ValueError:
            if f_str in variables:
                a = variables[f_str]
            else:
                invalid_message()
                continue
        try:
            b = float(s_str)
        except ValueError:
            if s_str in variables:
                b = variables[s_str]
            else:
                invalid_message()
                continue
        print(gcd(a, b))
    # calculate
    else:
        answer = calculate(line)
        if answer:
            print("=", answer)
        else:
            invalid_message()
