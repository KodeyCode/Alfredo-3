from sys import argv
f = open(argv[1])
exclude = ['import','print','from','for','def','else:','if']
def out(text):
    print(text)
def read(name):
    f = open(name)
    print(f.read())
def append(name,text):
    f = open(name,'a')
    f.write()
def tru(arg,exc):
    if arg:
        exec(exc)
for line in f:
    if line.split('(')[0] in exclude or line.split(' ')[0] in exclude:
        print('Error')
    else:
        exec(line)