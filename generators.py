import random


def random_integer(x, y):
    """Generate random integer (from x to y), return it as integer"""
    return round(random.uniform(x, y))


def random_float(x, y):
    """Generate random integer (from x to y), return it as integer"""
    return random.uniform(x, y)


def sri(x, y):
    """Generate random integer (from x to y), return it as string"""
    return str(random_integer(x, y))


def random_string(times, s='qwertyuiopasdfghjklzxcvbnm'):
    """Generate random string of given length (s is for providing custom alphabet)"""
    temp = ''
    for i in range(times):
        temp += random.choice(s)
    return temp


def random_sign():
    return random_integer(0, 1) * 2 - 1


def rs():
    """Generate random string of random length"""
    return random_string(random_integer(1, 100))


def rss():
    """Generate random string of random length with spaces"""
    return random_string(random_integer(1, 100), s='qwertyuiopasdfghjklzxcvbnm ')


def a1():
    a = random_integer(1, 10000)
    b = random_integer(1, 10000)
    return '{0}\n{1}'.format(a, b)


def m1():
    hms1 = random_integer(0, 86398)
    hours_1 = hms1 // 3600
    minutes_1 = hms1 // 60 % 60
    seconds_1 = hms1 % 60
    hms2 = random_integer(hms1 + 1, 86399)
    hours_2 = hms2 // 3600
    minutes_2 = hms2 // 60 % 60
    seconds_2 = hms2 % 60
    return '{0}\n{1}\n{2}\n{3}\n{4}\n{5}'.format(hours_1, minutes_1, seconds_1, hours_2, minutes_2, seconds_2)


def n1():
    a = random_integer(0, 10000)
    b = random_integer(0, 10)
    n = random_integer(1, 10000)
    return '{0}\n{1}\n{2}'.format(a, b, n)


def o1():
    v = random_integer(-1000, 1000)
    t = random_integer(-1000, 1000)
    return '{0}\n{1}'.format(v, t)


def q1():
    return random_string(4, '0123456789')


def r1():
    n = random_integer(1, 2400)
    m = random_integer(1, 100000)
    return '{0}\n{1}'.format(n, m)


def s1():
    h = random_integer(3, 1000)
    a = random_integer(2, h-1)
    b = random_integer(1, a-1)
    return '{0}\n{1}\n{2}'.format(h, a, b)


def t1():
    a = random_integer(1, 1000)
    b = random_integer(1, 1000)
    return '{0}\n{1}'.format(a, b)


def a2():
    a = random_integer(1, 8)
    b = random_integer(1, 8)
    c = random_integer(1, 8)
    d = random_integer(1, 8)
    return '{0}\n{1}\n{2}\n{3}'.format(a, b, c, d)


def b2():
    a = random_integer(1, 100)
    b = random_integer(1, 100)
    c = random_integer(1, 100)
    d = random_integer(1, 100)
    e = random_integer(1, 100)
    return '{0}\n{1}\n{2}\n{3}\n{4}'.format(a, b, c, d, e)


def c2():
    _a1 = random_integer(1, 100)
    _b1 = random_integer(1, 100)
    _c1 = random_integer(1, 100)
    _a2 = random_integer(1, 100)
    _b2 = random_integer(1, 100)
    _c2 = random_integer(1, 100)
    return '{0}\n{1}\n{2}\n{3}\n{4}\n{5}'.format(_a1, _b1, _c1, _a2, _b2, _c2)


def e2():
    a = random_integer(-100, 100)
    b = random_integer(-100, 100)
    c = random_integer(-100, 100)
    d = random_integer(-100, 100)
    if a == 0 and b == 0 and c == 0 and d == 0:
        a = random_integer(1, 100) * random_sign()
        b = random_integer(1, 100) * random_sign()
        c = random_integer(1, 100) * random_sign()
        d = random_integer(1, 100) * random_sign()
    return '{0}\n{1}\n{2}\n{3}'.format(a, b, c, d)


def f2():
    _l1 = random_integer(0, 99)
    _r1 = random_integer(_l1 + 1, 100)
    _l2 = random_integer(0, 99)
    _r2 = random_integer(_l2 + 1, 100)
    _l3 = random_integer(0, 99)
    _r3 = random_integer(_l3 + 1, 100)
    return '{0}\n{1}\n{2}\n{3}\n{4}\n{5}'.format(_l1, _r1, _l2, _r2, _l3, _r3)


def i2():
    epochs = random_integer(0, 1000)
    s = sri(1, 100)
    for e in range(epochs):
        s += '\n' + sri(1, 100)
    s += '\n0'
    return s


def l2():
    epochs = random_integer(1, 1000)
    s = sri(1, 100)
    for e in range(epochs):
        s += '\n' + sri(1, 100)
    s += '\n0'
    return s


def m2():
    return str(random_float(0, 100))

def q2():
    return str(round(random_float(0, 100),2))


def o2():
    a = random_integer(1, 100)
    b = random_integer(1, 100)
    c = random_integer(1, 100)
    while not (a < b + c and b < a + c and c < a + b):
        a = random_integer(1, 100)
        b = random_integer(1, 100)
        c = random_integer(1, 100)
    return '{0}\n{1}\n{2}'.format(a, b, c)


def p2():
    p = random_integer(0, 100)
    x = random_integer(0, 100000)
    y = random_integer(0, 99)
    k = random_integer(1, 100)
    return '{0}\n{1}\n{2}\n{3}'.format(p, x, y, k)


def r2():
    n = random_integer(0, 20)
    x = random_float(-100, 100)
    s = '{0}\n{1}\n'.format(n, x)
    for i in range(n + 1):
        s += str(random_float(-100, 100)) + '\n'
    return s


def t2():
    a = random_float(0.0001, 100) * random_sign()
    b = random_float(-100, 100)
    c = random_float(-100, 100)
    return '{0}\n{1}\n{2}'.format(a, b, c)


def b3():
    n = random_integer(0, 50)
    s = ''
    for i in range(n):
        s += rs() + ' '
    s += rs()
    return s


def c3():
    return rs() + ' ' + rs()


def e3():
    return rss() + 'h' + rss() + 'h' + rss()


def h3():
    return random_string(random_integer(1, 1000), s='qwertyuiopasdfghjklzxcvbnm111234567890 ')


def i3():
    return random_string(random_integer(1, 1000), s='qwertyuiopasdfghjklzxcvbnm1234567890./ @@@')


def o3():
    a = random_integer(1000, 9998)
    b = random_integer(a + 1, 9999)
    return '{0}\n{1}'.format(a, b)


def r3():
    n = random_integer(1, 100)
    f = random_integer(1, n)
    _list = list(range(1, n+1))
    _list.__delitem__(f)
    s = str(n) +'\n'
    for i in _list:
        s += str(i) + '\n'
    return s


def a4():
    a = random_integer(-10000, 10000)
    b = random_integer(-10000, 10000)
    c = random_integer(-10000, 10000)
    d = random_integer(-10000, 10000)
    return '{0}\n{1}\n{2}\n{3}'.format(a, b, c, d)


def b4():
    x1 = random_float(-1000, 1000)
    y1 = random_float(-1000, 1000)
    x2 = random_float(-1000, 1000)
    y2 = random_float(-1000, 1000)
    return '{0}\n{1}\n{2}\n{3}'.format(x1, y1, x2, y2)


def c4():
    x1 = random_integer(-1000, 1000)
    y1 = random_integer(-1000, 1000)
    x2 = random_integer(-1000, 1000)
    y2 = random_integer(-1000, 1000)
    x3 = random_integer(-1000, 1000)
    y3 = random_integer(-1000, 1000)
    return '{0}\n{1}\n{2}\n{3}\n{4}\n{5}'.format(x1, y1, x2, y2, x3, y3)


def d4():
    x = random_integer(0, 1)
    y = random_integer(0, 1)
    return '{0}\n{1}'.format(x, y)


def e4():
    x = random_float(-100, 100)
    y = random_float(-100, 100)
    return '{0}\n{1}'.format(x, y)


def g4():
    x = random_float(-100, 100)
    y = random_float(-100, 100)
    x_c = random_float(-100, 100)
    y_c = random_float(-100, 100)
    r = random_float(0, 100)
    return '{0}\n{1}\n{2}\n{3}\n{4}'.format(x, y, x_c, y_c, r)


def k4():
    a = random_float(0, 1000)
    p = random_integer(0, 100)
    a_s = '%.6f' % a
    return a_s + '\n' + str(p)


def l4():
    a = random_float(0, 1000)
    p = random_integer(-100, 100)
    return '{0}\n{1}'.format(a, p)


def m4():
    a = random_integer(0, 200)
    b = random_integer(0, 200)
    return '{0}\n{1}'.format(a, b)


def r4():
    a = random_integer(0, 30)
    b = random_integer(0, a)
    return '{0}\n{1}'.format(a, b)


def s4():
    s = ''
    for i in range(random_integer(1, 1000)):
        s += str(random_integer(1, 1000) * random_sign()) + '\n'
    s += '0'
    return s


def u4():
    s = ''
    for i in range(random_integer(1, 1000)):
        s += str(random_integer(1, 1000)) + '\n'
    s += '0'
    return s


def a5():
    s = ''
    for i in range(random_integer(1, 10000)):
        s += str(random_integer(-1000, 1000)) + ' '
    s += str(random_integer(-1000, 1000))
    return s


def c5():
    higher = random_integer(150, 200)
    lower = random_integer(140, higher)
    p = random_integer(lower, higher)
    _last = higher
    s = ''
    for i in range(random_integer(1, 60)):
        _last = random_integer(lower, _last)
        s += str(_last) + ' '
    _last = random_integer(lower, _last)
    s += str(_last) + '\n' + str(p)
    return s


def d5():
    higher = random_integer(500, 1000)
    lower = random_integer(0, 500)
    _last = higher
    s = ''
    for i in range(random_integer(1, 1000)):
        _last = random_integer(lower, _last)
        s += str(_last) + ' '
    _last = random_integer(lower, _last)
    s += str(_last)
    return s


def e5():
    s = ''
    for i in range(random_integer(1, 1000)):
        s += sri(-1000, 1000) + ' '
    s += sri(-1000, 1000)
    return s


def g5():
    n = random_integer(1, 1000)
    m = random_integer(1, 100)
    s = str(n) + ' ' + str(m) + '\n'
    for i in range(m):
        left = random_integer(1, n)
        right = random_integer(left, n)
        s += str(left) + ' ' + str(right) + '\n'
    left = random_integer(1, n)
    right = random_integer(left, n)
    s += str(left) + ' ' + str(right)
    return s


def h5():
    x = list(range(1, 9))
    y = x[:]
    random.shuffle(x)
    random.shuffle(y)
    s = ''
    for i in range(7, -1, -1):
        s += str(x[i]) + ' ' + str(y[i]) + '\n' * (not not i)
    return s


def i5():
    s = ''
    for i in range(random_integer(1, 10000)):
        if random_float(0, 1) < 0.2:
            s += str(random_integer(-1000, 1000)) + ' '
        else:
            s += '0 '
    if random_float(0, 1) < 0.2:
        s += str(random_integer(-1000, 1000))
    else:
        s += '0'
    return s


def j5():
    _l = random.choices(range(random_integer(1, 100)), k=random_integer(1, 1000))
    s = str(_l)[1:-1].replace(',', '')
    return s


def k5():
    n = random_integer(1, 1000)
    _l = random.choices(range(random_integer(1, 100)), k=random_integer(1, 1000))
    s = str(n) + '\n'
    s += str(_l)[1:-1].replace(',', '') + '\n'
    s += sri(1, 100)
    return s


def l5():
    s = ''
    for i in range(random_integer(1, 100000)):
        s += str(random_integer(-1000, 1000)) + ' '
    s += str(random_integer(-1000, 1000))
    return s


def m5():
    s = ''
    for i in range(random_integer(1, 99999)):
        s += str(random_integer(0, 100)) + ' '
    s += str(random_integer(0, 100))
    return s


def n5():
    S = random_integer(1, 10000)
    N = random_integer(1, 100)
    s = str(S) + ' ' + str(N) + '\n'
    for i in range(N-1):
        s += sri(1, 1000) + '\n'
    s += sri(1, 1000)
    return s


def o5():
    s = ''
    for i in range(random_integer(1, 10000)):
        s += rs() + ' ' + rs() + ' ' + sri(9, 11) + ' ' + sri(0, 100) + '\n'
    s += rs() + ' ' + rs() + ' ' + sri(9, 11) + ' ' + sri(0, 100)
    return s


def p5():
    s = ''
    for i in range(random_integer(1, 10000)):
        s += rs() + ' ' + rs() + ' ' + sri(1, 99) + ' ' + sri(0, 100) + '\n'
    s += rs() + ' ' + rs() + ' ' + sri(1, 99) + ' ' + sri(0, 100)
    return s


def q5():
    _l = []
    for i in range(random_integer(1, 25)):
        _s = random_string(random_integer(1, 25))
        if _s not in _l:
            _l.append(_s)
    _v = random.choices(_l, k=random_integer(1, 1000))
    s = 'PARTIES:\n'
    s += str(_l)[1:-1].replace("'", '').replace(', ', '\n') + '\n'
    s += 'VOTES:\n'
    s += str(_v)[1:-1].replace("'", '').replace(', ', '\n')
    return s


def r5():
    s = ''
    _l = list(range(1, 1000))
    s += str(random.choices(_l, k=random_integer(1, 10000)))[1:-1].replace(',', '') + '\n'
    s += str(random.choices(_l, k=random_integer(1, 10000)))[1:-1].replace(',', '')
    return s


def t5():
    s = sri(1, 300) + '\n'
    for i in range(random_integer(1, 10000)):
        s += rs() + ' ' + rs() + ' ' + sri(0, 100) + ' ' + sri(0, 100) + ' ' + sri(0, 100) + '\n'
    s += rs() + ' ' + rs() + ' ' + sri(0, 100) + ' ' + sri(0, 100) + ' ' + sri(0, 100)
    return s


def a6():
    s = ''
    flag = True
    for i in range(random_integer(1, 10000)):
        x = random_integer(-100, 100)
        s += str(x) + ' '
        if abs(x) % 2 == 1:
            flag = False
    if flag:
        s += str(random_integer(-50, 50) * 2 + 1)
    else:
        s += str(random_integer(-100, 100))
    return s


def b6():
    n = random_integer(1, 100000)
    s = str(n) + '\n'
    for i in range(n):
        if random_float(0, 1) < 0.05:
            s += '0\n'
        else:
            s += sri(0, 1000) + '\n'
    return s


def c6():
    s = ''
    for i in range(random_integer(1, 1000)):
        if i < 100:
            s += sri(1, 100) + ' '
        else:
            s += sri(1, 10) + ' '
    s += sri(1, 100)
    return s


def d6():
    s = ''
    n = random_integer(1, 100)
    for i in range(n):
        s += sri(0, 1) + ' '
    s += sri(0, 1) + '\n'

    for i in range(n):
        s += sri(0, 1) + ' '
    s += sri(0, 1)
    return s


def e6():
    _l = random.choices(range(random_integer(-1000, 0), random_integer(1, 1000)), k=random_integer(1, 10000))
    s = str(_l)[1:-1].replace(',', '')
    return s


def h6():
    n = random_integer(2, 1000)
    k = random_integer(1, 1000)
    s = str(n) + '\n'
    for i in range(n-1):
        _l = random.choices([0, 1], k=k)
        s += str(_l)[1:-1].replace(',', '') + '\n'

    _l = random.choices([0, 1], k=k)
    s += str(_l)[1:-1].replace(',', '')
    return s


def j6():
    _l = random.choices(range(random_integer(0, 100000)), k=random_integer(1, 100000))
    s = str(_l)[1:-1].replace(',', '')
    return s


def k6():
    s = ''
    for i in range(random_integer(1, 1000)):
        s += rss() + '\n'
    s += rss()
    return s


def b7():
    _l = random.choices(range(random_integer(0, 5000)), k=random_integer(1, 5000))
    s = str(_l)[1:-1].replace(',', '') + '\n'
    _l = random.choices(range(random_integer(0, 5000)), k=random_integer(1, 5000))
    s += str(_l)[1:-1].replace(',', '')
    return s


def e7():
    n = random_integer(1, 10000)
    m = random_integer(1, 10000)
    s = str(n) + ' ' + str(m) + '\n'
    _l = list(set(random.choices(range(random_integer(0, 10000)), k=n)))
    s += str(_l)[1:-1].replace(', ', '\n') + '\n'
    _l = list(set(random.choices(range(random_integer(0, 10000)), k=m)))
    s += str(_l)[1:-1].replace(', ', '\n')
    return s


def g7():
    n = random_integer(1, 10000)
    m = random_integer(1, n)
    s = ''
    for i in range(random_integer(1, 1000)):
        _l = list(range(1, n+1))
        random.shuffle(_l)
        __l = _l[0:random_integer(1, len(_l))]
        s += str(__l)[1:-1].replace(',', '') + '\n'
        if m in __l:
            s += 'YES\n'
        else:
            s += 'NO\n'
    s += 'HELP'
    return s


def h7():
    n = random_integer(1, 10000)
    s = ''
    for i in range(random_integer(1, 1000)):
        _l = list(range(1, n + 1))
        random.shuffle(_l)
        __l = _l[0:random_integer(1, len(_l))]
        s += str(__l)[1:-1].replace(',', '') + '\n'
    s += 'HELP'
    return s


def i7():
    langs = ['Afar', 'Abkhaz', 'Avestan', 'Afrikaans', 'Akan', 'Amharic', 'Aragonese', 'Arabic', 'Assamese', 'Avar', 'Aymara', 'Azerbaijani', 'Bashkir', 'Belarusian', 'Bulgarian', 'Bihari', 'Bislama', 'Bambara', 'Bengali', 'Tibetan', 'Breton', 'Catalan', 'Chechen', 'Chamorro', 'Corsican', 'Cree', 'Czech', 'Old Church Slavonic', 'Chuvash', 'Welsh', 'Danish', 'German', 'Dhivehi', 'Dzongkha', 'Ewe', 'Greek', 'English', 'Esperanto', 'Spanish', 'Estonian', 'Basque', 'Persian', 'Fula', 'Finnish', 'Fijian', 'Faroese', 'French', 'West Frisian', 'Irish', 'Scottish Gaelic', 'Galician', 'Guaraní', 'Gujarati', 'Manx', 'Hausa', 'Hebrew', 'Hindi', 'Hiri Motu', 'Haitian Creole', 'Hungarian', 'Armenian', 'Herero', 'Interlingua', 'Indonesian', 'Interlingue', 'Igbo', 'Sichuan Yi', 'Inupiaq', 'Ido', 'Icelandic', 'Italian', 'Inuktitut', 'Japanese', 'Javanese', 'Georgian', 'Kongo', 'Kikuyu', 'Kwanyama', 'Kazakh', 'Greenlandic', 'Khmer', 'Kannada', 'Korean', 'Kanuri', 'Kashmiri', 'Cornish', 'Kyrgyz', 'Latin', 'Luxembourgish', 'Luganda', 'Limburgish', 'Lingala', 'Lao', 'Lithuanian', 'Luba-Katanga', 'Latvian', 'Malagasy', 'Marshallese', 'Maori', 'Macedonian', 'Malayalam', 'Mongolian', 'Marathi', 'Malay', 'Maltese', 'Burmese', 'Nauruan', 'Norwegian Bokmål', 'Northern Ndebele', 'Nepali', 'Ndonga', 'Dutch', 'Norwegian Nynorsk', 'Norwegian', 'Southern Ndebele', 'Navajo', 'Chichewa', 'Occitan', 'Ojibwe', 'Oromo', 'Oriya', 'Ossetian', 'Punjabi', 'Pali', 'Polish', 'Pashto', 'Portuguese', 'Quechua', 'Romansch', 'Romanian', 'Russian', 'Rwanda-Rundi', 'Sanskrit', 'Sardinian', 'Sindhi', 'Northern Sami', 'Sango', 'Serbo-Croatian', 'Sinhalese', 'Slovak', 'Slovene', 'Samoan', 'Shona', 'Somali', 'Albanian', 'Swazi', 'Sotho', 'Sundanese', 'Swedish', 'Swahili', 'Tamil', 'Telugu', 'Tajik', 'Thai', 'Tigrinya', 'Turkmen', 'Tagalog', 'Tswana', 'Tongan', 'Turkish', 'Tsonga', 'Tatar', 'Tahitian', 'Uyghur', 'Ukrainian', 'Urdu', 'Uzbek', 'Venda', 'Vietnamese', 'Volapük', 'Walloon', 'Wolof', 'Xhosa', 'Yiddish', 'Yoruba', 'Zhuang', 'Chinese', 'Zulu']
    n = random_integer(1, 1000)
    s = str(n) + '\n'
    for i in range(n):
        _l = list(set(random.choices(langs, k=random_integer(1, 40))))
        s += str(len(_l)) + '\n'
        s += str(_l)[1:-1].replace(', ', '\n').replace("'", '') + '\n'
    return s[:-1]


def j7():
    a = random_integer(1, 100)
    b = random_integer(1, 100)
    c = random_integer(1, 100)
    d = random_integer(1, 100)
    return '{0} {1} {2} {3}'.format(a, b, c, d)


def k7():
    n = random_integer(1, 1000000)
    k = random_integer(1, 100)
    s = str(n) + ' ' + str(k) + '\n'
    for i in range(k):
        s += sri(1, n) + ' ' + sri(1, n) + '\n'
    return s[:-1]


def l7():
    def num():
        _tel = ''
        for _i in range(6):
            _tel += sri(0, 9) + ('-' * random_integer(0, 1))
        return _tel + sri(0, 9)

    def code():
        _r = random_float(0, 1)
        _code = ''
        if _r < 1 / 2:
            _code = '('
            for _i in range(2):
                _code += sri(0, 9) + ('-' * random_integer(0, 1))
            _code += sri(0, 9) + ')'
        else:
            _code = '-' * random_integer(0, 1)
            for _i in range(2):
                _code += sri(0, 9) + ('-' * random_integer(0, 1))
            _code += sri(0, 9) + '-' * random_integer(0, 1)
        return _code

    s = ''
    for i in range(4):
        r = random_float(0, 1)
        tel = ''
        if r < 1/3:
            tel += '+7' + code() + num()
        elif r < 2/3:
            tel += '8' + code() + num()
        else:
            tel += num()
        s += tel +'\n'
    return s[:-1]


def m7():
    n = random_integer(1, 100)
    countries = []
    cities = []
    s = str(n) + '\n'
    for i in range(n):
        c = rs()
        while c in countries:
            c = rs()
        countries.append(c)
        s += c + ' '
        for j in range(random_integer(1, 100)):
            cit = rs()
            while cit in cities:
                cit = rs()
            s += cit + ' '
        s = s[:-1] + '\n'

    m = random_integer(1, 500)
    for i in range(m):
        s += random.choice(cities) + '\n'
    return s[:-1]


def n7():
    words = []
    for i in range(random_integer(1, 10000)):
        words.append(random_string(random_integer(1, 25), s='qwertyuiopasdfghjklzxcvbnm0123456789@?";:[{]} '+"\n"))
    _l = random.choices(words, k=random_integer(1, 10000))
    s = str(_l)[1:-1].replace(',', '').replace("'", '').replace('\\n', '\n')
    return s


def o7():
    n = random_integer(1, 1000)
    words = []
    s = str(n) + '\n'
    for i in range(n):
        x, y = rs(), rs()
        while x in words:
            x = rs()
        words.append(x)
        while y in words:
            y = rs()
        words.append(y)
        s += x + ' ' + y + '\n'
    s += random.choice(words)
    return s


def p7():
    n = random_integer(1, 100)
    names = []
    s = ''
    for i in range(n):
        c = rs()
        while c in names:
            c = rs()
        names.append(c)

    for i in range(random_integer(1, 1000)):
        s += random.choice(names) + ' ' + sri(1, 1000) + '\n'
    return s[:-1]


def s7():
    n = random_integer(1, 20)
    names = []
    s = ''
    for i in range(n):
        c = random_string(random_integer(1, 15)) + ' ' + random_string(random_integer(1, 15))
        while c in names:
            c = random_string(random_integer(1, 15)) + ' ' + random_string(random_integer(1, 15))
        names.append(c)

    for i in range(random_integer(1, 10000)):
        s += random.choice(names) + '\n'
    return s[:-1]


def t7():
    names = []
    products = []
    s = ''
    for i in range(random_integer(1, 500)):
        c = rs()
        while c in names:
            c = rs()
        names.append(c)

    for i in range(random_integer(1, 500)):
        c = rs()
        while c in products:
            c = rs()
        products.append(c)

    for i in range(random_integer(1, 10000)):
        s += random.choice(names) + ' ' + random.choice(products) + ' ' + sri(1, 1000) + '\n'
    return s[:-1]


def u7():
    names = []
    s = ''
    for i in range(random_integer(1, 500)):
        c = rs()
        while c in names:
            c = rs()
        names.append(c)

    for i in range(random_integer(1, 10000)):
        r = random_integer(0, 4)
        if r == 0:
            s += 'DEPOSIT ' + random.choice(names) + ' ' + sri(1, 1000) + '\n'
        if r == 1:
            s += 'WITHDRAW ' + random.choice(names) + ' ' + sri(1, 1000) + '\n'
        if r == 2:
            s += 'BALANCE ' + random.choice(names) + '\n'
        if r == 3:
            _n1 = random.choice(names)
            _n2 = random.choice(names)
            while _n1 == _n2:
                _n2 = random.choice(names)
            s += 'TRANSFER ' + _n1 + ' ' + _n2 + ' ' + sri(1, 1000) + '\n'
        if r == 4:
            s += 'INCOME ' + sri(1, 150) + '\n'
    return s[:-1]


messages = [
    'Алиса все падала, падала, падала... Казалось этому падению никогда не будет конца.',
    'Алиса, надо сказать, частенько давала себе очень разумные советы, но довольно редко следовала им.',
    'Впрочем, ведь раз некому ответить, то не все ли равно, о чем спрашивать?',
    'Нет ничего на свете, из чего нельзя было бы сделать вывод. Надо только знать, как взяться за дело.',
    'Знаешь, одна из самых серьезных потерь в битве - это потеря головы.',
    'Лучше буду молчать - подумала Алиса, Лучше молчи - подумали все.',
    'Хорошенькая вышла шутка, правда? Жаль, что не ты ее придумала!',
    'Если верить в себя, то невозможное оказывается осуществимо.',
    'Ты зря состязаешься со временем! От времени не убежишь!',
    'Нужно бежать со всех ног, чтобы только оставаться на месте, а чтобы куда-то попасть, надо бежать как минимум вдвое быстрее!'
]
# messages = ['РИВЕСТ, ШАМИР И АДЛЕМАН.']
alph = ' АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ.,-?!абвгдеёжзийклмнопрстуфхцч'


def a8():
    message = random.choice(messages).upper()
    key = random.randint(1, len(alph) - 1)
    res = ''.join([alph[(alph.index(c)+key) % len(alph)] for c in message])
    return res

def b8():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
    p, q = primes[random.randint(3, len(primes) - 1)], primes[random.randint(3, len(primes) - 1)]
    while p == q or p * q < 39 * 64 + 39 or p * q > 65 * 64:
        p = primes[random.randint(3, len(primes) - 1)]
        q = primes[random.randint(3, len(primes) - 1)]
    n = p * q
    euler = (p - 1) * (q - 1)
    e = 17
    for d in range(2, euler):
        if d * e % euler == 1:
            break

    message = random.choice(messages).upper()
    message = message + ' ' * (len(message) % 2)

    def tokenize(chars):
        a = alph.index(chars[0])
        b = alph.index(chars[1])
        return a * 64 ** 1 + b * 64 ** 0

    def encode(m):
        m_ = 1
        for i in range(e):
            m_ *= m
            m_ %= n
        return m_

    def detokenize(m):
        a = m // 64
        b = m % 64
        return alph[a] + alph[b]

    tokenized_message = [tokenize(c) for c in zip(message[::2], message[1::2])]
    encoded_message = [encode(m) for m in tokenized_message]
    detokenized_message = ''.join([detokenize(m) for m in encoded_message])
    return str(n)+' '+str(e)+'\n'+detokenized_message


def c8():
    n = random.randint(100, 1000)
    c = random.choices(range(0, 100), k=n)
    s = c[0]
    c = sorted(c)
    return str(s)+'\n'+str(c)[1:-1].replace(',', '')


import numpy as np

def f(c, x):
  return c[0]*x*x*x + c[1]*x*x + c[2]*x + c[3]

def d8():
    if random.randint(0, 1) == 0:
        a, b, c_1, d = (np.random.random(4) - 0.5) * 20
        c = b ** 2 / (3 * a) + abs(c_1)
        x = (np.random.random() - 0.5) * 20
        h = f([a, b, c, d], x)
        return str(a)+' '+str(b)+' '+str(c)+' '+str(d)+'\n'+str(h)
    else:
        c, d = (np.random.random(2) - 0.5) * 20
        c = abs(c)
        x = (np.random.random() - 0.5) * 20
        h = f([0, 0, c, d], x)
        return '0 0 '+str(c)+' '+str(d)+'\n'+str(h)


def e8():
    def display(r):
        s = ''
        for i in range(10):
            for j in range(10):
                s += str(r[i][j]) + ' '
            s += '\n'
        return s
    x1, y1 = 9, 9
    x2, y2 = 0, 0
    r = [[2 for i in range(9)] + [3] for i in range(9)] + [[2 for i in range(9)] + [0]]
    for i in range(1000):
        dc = random.randint(0, 1)
        if dc == 0:
            x, y = x1, y1
        else:
            x, y = x2, y2
        dz = random.randint(0, 1)
        if dz == 0:
            dx = random.randint(0, 1) * 2 - 1
            if dx == -1:
                r[x][y] = 1
                r[(x - 1) % 10][y] = 0
                x = (x - 1) % 10
            else:
                r[x][y] = 3
                r[(x + 1) % 10][y] = 0
                x = (x + 1) % 10
        else:
            dy = random.randint(0, 1) * 2 - 1
            if dy == -1:
                r[x][y] = 4
                r[x][(y - 1) % 10] = 0
                y = (y - 1) % 10
            else:
                r[x][y] = 2
                r[x][(y + 1) % 10] = 0
                y = (y + 1) % 10
        if dc == 0:
            x1, y1 = x, y
        else:
            x2, y2 = x, y
    s = display(r)
    s += str(x) + ' ' + str(y) + '\n'
    s += str(random.randint(0, 9)) + ' ' + str(random.randint(0, 9))
    return s


print(a8())
