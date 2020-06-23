import re
def get_books(name_txt):
    books_list = []
    with open(name_txt, encoding= 'utf-8') as f:
        f.readline()
        data = f.read()
        for line in data.split('\n'):
            line = line.split('|')
            books_list.append([line[0],line[1],line[2],int(line[3]),float(line[4])])
    return books_list


def filter_books(name,list_bok):
    list_gen = []
    for h in range(len(list_bok)):
        inlist = list_bok[h]
        for k in range(len(inlist)):
            name = name.title()
            hg = re.search(fr'({name})',str(inlist[k]))
            if hg:
                list_gen.append(f'{list_bok[h][0]}|{list_bok[h][1]}, {list_bok[h][2]}|{list_bok[h][3]}|{list_bok[h][4]}'.split('|'))
    return list_gen





# filter_books('Python',get_books('books.txt'))