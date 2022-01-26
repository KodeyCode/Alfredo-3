from sys import argv
from importlib import import_module as immod
f = open(argv[1])
exclude = ['import','print','for','if','else:','elif','from','for','def','class','exec','input','eval','open','with','while']
keys = {
    'use':'use',
    'func':'func',
    'call':'call',
    'stack':'stk',
    'link':'link'
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
def func(name,arg,code):
    funcs.update({name+' @ '+arg:code})
def call(name,arg,nuf):
    if funcs[name].split('(')[0] in exclude or funcs[name].split(' ')[0] in exclude:
        print('Syntax Error: In function '+name+'\n    '+funcs[name]+'\nUnidentified command.')
    else:
        k = []
        for key in funcs.keys():
              k.append(key)
        exec(funcs[arg])
        exec(funcs[name.split(' @ ')[0]])
def use(mod):
    f = open('lib/'+mod+'.alf')
    lineNum = 1
    for line in f:
        if line.split('(')[0] in exclude or line.split(' ')[0] in exclude:
            print('Syntax Error at line '+str(lineNum)+' in file '+f.name+'\n    '+line+'\nUnidentified command')
        elif line.startswith('//'):
            pass
        elif line.split(' ')[0] in keys:
            exec(keys[line.split(' ')[0]]+'('+line.split(' ')[1]+')')
        else:
            exec(line)
        lineNum +=1
def stk(stack):
    codes = []
    for item in stack.split(',')
        codes.append(item)
    num = 1
    for i in range(len(codes)):
        exec(codes[num])
        num +=1
def link(file):
    immod(file)
lineNum = 1
for line in f:
    if line.split('(')[0] in exclude or line.split(' ')[0] in exclude:
        print('Syntax Error at line '+str(lineNum)+' in file '+f.name+'\n    '+line+'\nUnidentified command')
    elif line.startswith('//'):
        pass
    elif line.split(' ')[0] in keys:
        exec(keys[line.split(' ')[0]]+'('+line.split(' ')[1]+')')
    else:
        exec(line)
    lineNum +=1
