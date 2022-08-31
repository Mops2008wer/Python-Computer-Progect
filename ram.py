raminfo = {
    'ramarm': '1089',
    'ramver': 'DR1_',
    'ramname': 'PyDr_Delta '
    }

def _mov(x, data):
    file = open(("apps/" + x), "w")
    file.write(str(data))
    file.close()

def _read(x):
    file = open(("apps/" + x), "r")
    data = file.read()
    file.close()
    return data

def _mov_metadata(x, _data, n):
    file = open(("apps/" + x), "r")
    data = file.read()
    file.close()
    metadata = data.split("-")
    metadata[int(n)] = _data
    file = open(("apps/" + x), "w")
    file.write("-".join(metadata)) 
    file.close()

def _read_metadata(x, n):
    file = open(("apps/" + x), "r")
    data = file.read()
    file.close()
    metadata = data.split("-")
    return metadata[int(n)]