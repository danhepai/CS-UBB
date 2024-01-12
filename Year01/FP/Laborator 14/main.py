def get_input():
    n = int(input(">>> "))
    if n % 2 == 1:
        print("Invalid input")
        get_input()
    return n


def solution_iterative(n, solutions):
    """
    Iterative solution
    :param n: the number of paranteses
    :param solutions: A list with all solutions for the problem. The elements are strings
    :return:
    """
    stack = [('', 0, 0)]  # The 'stack' list imitates the real stack in case of a recursive algo

    while stack:    # While the stack is not empty, it means that there are still possible solutions to explore
        string, opened, closed = stack.pop()    # Getting the values to check from the stack

        if opened == n // 2 and closed == n // 2:   # If there are equal number of closed and opened parantheses, it
            solutions.append(string)                # means it is solution.
        else:
            if opened < n // 2:                     # If the current state allows for opened parantheses, it adds one
                stack.append((string + '(', opened + 1, closed))
            if closed < opened:                     # If the current state allows for closed parantheses, it adds one
                stack.append((string + ')', opened, closed + 1))


def solution_recursive(n, string, opened, closed, solutions):
    """
    Recursive solution
    :param n: the number of parantheses
    :param string: the current string it checks if it's a solution
    :param opened: num of opened parantheses '('
    :param closed:num of closed parantheses ')'
    :param solutions: A list with all solutions for the problem. The elements are strings
    :return:
    """
    if len(string) == n:    # It means the string is ready to be checked if it is a solution
        if opened == closed:    # If there are equal number of closed and opened parantheses, it means it's a solution
            solutions.append(string)
        return
    if opened < n // 2:  # If the current state allows for opened parantheses, it adds one
        solution_recursive(n, string + '(', opened + 1, closed, solutions)
    if closed < opened:  # If the current state allows for closed parantheses, it adds one
        solution_recursive(n, string + ')', opened, closed + 1, solutions)


# isCosistent daca are acelasi nr de paranteze inchise si deschise
# isSolution daca isCosistent si daca len(solution) == n

def isCosistent(string, n):
    closed = opened = 0
    for char in string:
        if char == '(':
            opened += 1
        else:
            closed += 1
    return n // 2 >= opened >= closed


def isSolution(string, n):
    closed = opened = 0
    for char in string:
        if char == '(':
            opened += 1
        else:
            closed += 1

    return closed == opened and len(string) == n


def BackTracking(string, n, solutions, domain):
    for el in domain:
        string += el
        if isCosistent(string, n):
            if isSolution(string, n):
                solutions.append(string)
            BackTracking(string, n, solutions, domain)
        string = string[:-1]


def main():
    n = get_input()
    solutions = []
    solution_recursive(n, '', 0, 0, solutions)
    print(f"My Recursive: {solutions}")
    solutions = []
    solution_iterative(n, solutions)
    print(f"My Iterative: {solutions}")
    solutions = []
    BackTracking('', n, solutions, ['(', ')'])
    print(f"Ge Recursive: {solutions}")


if __name__ == "__main__":
    main()
