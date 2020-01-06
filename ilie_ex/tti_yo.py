
ascii_to_int = {i.to_bytes(1, 'big'): i for i in range(126)}
ascii_to_int2= {str(chr(i)): i for i in range(126)}

def lzw_compress(a):
    z=[]
    if(isinstance(a, str)):
        a=a.encode()
    nr=256
    che=ascii_to_int
    i=0
    s=a[i]
    while i!=a.__len__()-1:
        i=i+1
        c=a[i]
        if s+c in che:
            s=s+c
        else:
            z.append(che[s.to_bytes(1, 'big')])
            che[s+c]=nr
            nr=nr+1
            s=c
    z.append(che[s.to_bytes(1, 'big')])
    return z

def lzw_compress2(a):
    z = []
    if (isinstance(a, str)):
        a = a.encode()
    nr = 256
    che = ascii_to_int2
    i = 0
    s = a[i]
    while i != a.__len__() - 1:
        i = i + 1
        c = a[i]
        if s + c in che:
            s = s + c
        else:
            z.append(che[str(chr(s))])
            che[s + c] = nr
            nr = nr + 1
            s = c
    z.append(che[str(chr(s))])
    return z

def lzw_compress3(a):
    z = []
    if (isinstance(a, str)):
        a = a.encode()
    nr = 256
    che = ascii_to_int2
    i = 0
    s = a[i]
    while i != a.__len__() - 1:
        i = i + 1
        c = a[i]
        if s + c in che:
            s = s + c
        else:
            z.append(che[str(chr(s))])
            che[s + c] = nr
            nr = nr + 1
            s = c
    z.append(che[str(chr(s))])
    return z


def compress(uncompressed):

    dict_size = 128
    dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    if w:
        result.append(dictionary[w])
    return result


def decompress(compressed):
    from io import StringIO

    dict_size = 128
    dictionary = {i: chr(i) for i in range(dict_size)}

    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)

        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result.getvalue()

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

print(text)
z=compress(text)
print(z)
print(decompress(z))