def marks(**data):
    with open('marks.txt','a') as f:
        for n,m in data.items():
            f.write(f'{n}:{m}\n')

marks(aman=200,avi=456)
marks(raj=678,ajay=987,ashu=908)
marks()