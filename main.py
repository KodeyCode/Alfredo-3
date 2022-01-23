from sys import argv
f = open(argv[1])
exclude = ['import','print','for','if','else:','elif','from','for','def','class','exec','input','eval',]
funcs = {}
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
def func(name,code):
    funcs.update({name:code})
def call(name):
    if funcs[name].split('(')[0] in exclude or funcs[name].split(' ')[0] in exclude:
        print('Error')
    else:
        exec(funcs[func])\
def use(mod):
    f = open('lib/'+mod)
    for line in f:
        if line.split('(')[0] in exclude or line.split(' ')[0] in exclude:
            print('Error')
        else:
            exec(line)
for line in f:
    if line.split('(')[0] in exclude or line.split(' ')[0] in exclude:
        print('Error')
    else:
        exec(line)
