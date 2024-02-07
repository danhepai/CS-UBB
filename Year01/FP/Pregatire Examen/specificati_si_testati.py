def f2(n):
    """
    Calculeaza suma lui Gauss pentru (n-1) / Calculeaza suma numerelor naturale mai mici decat n
    daca n este natural diferit de 0. In caz contrar, arunca exceptie de tip ValueError
    param: int
    return: int / ValueError
    """
    if n <= 0:
        raise ValueError()
    l = [x for x in range(n - 1, -1, -1)]
    for i in range(n - 1):
        l[i + 1] += l[i]
    return l[-1]


def test_f2():
    assert f2(6) == 15
    assert f2(1) == 0
    try:
        x = f2(-1)
        assert False
    except ValueError:
        assert True


def f(n):
    """
    Calculeaza si returneaza al n-lea numar Fibonacci daca n este pozitiv. In caz contrar ridica exceptie ValueError
    Un numar fibonacci se formeaza prin adunarea a celor doi termeni anteriori. Primii 2 termeni sunt 1, 1.
    :param n: int
    :return: int / ValueError
    """
    if n < 0:
        raise ValueError()
    if n <= 1:
        return n
    l = [0] * (n + 1)
    l[1] = 1
    for i in range(2, n + 1):
        l[i] = l[i - 1] + l[i - 2]
    return l[n]


def test_f():
    assert f(5) == 5
    assert f(6) == 8
    try:
        x = f(-1)
        assert False
    except ValueError:
        assert True


def f3(n):
    """
    Returneaza True daca numarul natural nenul n are in componenta minim o cifra para.
    Daca n este negativ sau 0, ridica exceptie de tip ValueError
    :param n: int
    :return: bool / ValueError
    """
    if n <= 0:
        raise ValueError()
    while n > 0:
        c = n % 10
        n = n // 10
        if c % 2 == 0:
            return True
    return False


def test_f3():
    assert f3(12) == True
    assert f3(11) == False

    try:
        f3(-1)
        assert False
    except ValueError:
        assert True


def f4(n):
    """
    Calculeaza si returneaza suma cifrelor lui n, daca n este numar natural nenul. In caz contrat ridica exceptie de tip
    ValueError
    :param n: int / float
    :return: int
    """
    if n <= 0:
        raise ValueError()
    l = []
    while n > 0:
        c = n % 10
        n = n // 10
        l.append(c)
    for i in range(len(l) - 1):
        l[i + 1] += l[i]
    return l[-1]


def test_f4():
    assert f4(112233) == 12
    assert f4(12) == 3
    try:
        x = f4(0)
        assert False
    except ValueError:
        assert True

    try:
        x = f4(-1)
        assert False
    except ValueError:
        assert True


def f5(l):
    """
    Returneaza adevarat daca lista 'l' este ordanata strict crescator sau false in caz contrat.
    In caz ca parametrul nu este o lista sau daca lista este vida se ridica eroare de tip ValueError.
    :param l: list
    :return: bool
    """
    if l == None or l == []:
        raise ValueError()
    aux = l[0] - 1
    for e in l:
        if aux - e >= 0:
            return False
        aux = e
    return True


def test_f5():


test_f3()
test_f()
test_f2()
test_f4()
