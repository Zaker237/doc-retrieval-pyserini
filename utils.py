
def text_to_dict(text: str) ->tuple:
    return tuple(text.split(" "))

def tsv_to_dict(text: str) ->tuple:
    idx = text.index(" ")
    return (text[:idx], text[idx+1:])

def load_txt_file(path: str) ->list:
    with open(path, "r", encoding="utf-8") as fp:
        data = fp.readlines()

    return list(map(text_to_dict, data))

def load_tsv_file(path: str) ->list:
    with open(path, "r", encoding="utf-8") as fp:
        data = fp.readlines()

    return list(map(tsv_to_dict, data))