from sys import argv
f = open(argv[1])
exclude = ['import','print','for','if','else:','elif','from','for','def','class','exec','input','eval','open','with']
keys = {
    'use':'use',
    'func':'func',
    'call':'call'
}
funcs = {}
def out(text):
    print(text)
def read(name):
    f = open(name)
    print(f.read())
def append(name,text):
    f = open(name,'a')
    f.write()
def tru(arg,exc,els):
    if arg:
        if exc.split('(')[0] in exclude or exc.split(' ')[0] in exclude:
            print('Error')
        else:
            exec(exc)
    else:
        if els.split('(')[0] in exclude or els.split(' ')[0] in exclude:
            print('Error')
        else:
            exec(els)
def func(name,code):
    funcs.update({name:code})
def call(name):
    if funcs[name].split('(')[0] in exclude or funcs[name].split(' ')[0] in exclude:
        print('Error')
    else:
        exec(funcs[func])
def use(mod):
    f = open('lib/'+mod+'.alf')
    for line in f:
        if line.split('(')[0] in exclude or line.split(' ')[0] in exclude:
            print('Error')
        else:
            exec(line)
for line in f:
    if line.split('(')[0] in exclude or line.split(' ')[0] in exclude:
        print('Error')
    elif line.startswith('//'):
        pass
    elif line.split(' ')[0] in keys:
        exec(keys[line.split(' ')[0]]+'('+line.split(' ')[1]+')')
    else:
        exec(line)
