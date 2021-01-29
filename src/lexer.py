import string as strlib


#constant
RIGHTBRACKET=']'
LEFTBRACKET='['
RIGHTPARANTHESIS=')'
LEFTPARANTHESIS='('
COLON=':'
COMMA=','
QUOTE='"'
WHITESPACE =['\n','\t',' ','\r']

SEPERATOR= WHITESPACE+[RIGHTBRACKET,LEFTBRACKET,RIGHTPARANTHESIS,LEFTPARANTHESIS,COLON,COMMA]
KPUNTUATION = [RIGHTBRACKET,LEFTBRACKET,RIGHTPARANTHESIS,LEFTPARANTHESIS,COLON,COMMA]
NUMBERS=['0','1','2','3','4','5','6','7','8','9','.']

def errorparse():
    print("error in parsing")
    return 0;

def lexer(string):
    strlen = len(string)
    lexme=[];
    token=""
    i=0;
    while i < strlen:
        if string[i] == QUOTE:
            lexme.append('"')
            i+=1;
            while string[i] !='"':
                token+=string[i]
                i+=1
            lexme.append(token)
            lexme.append('"')
            tokex=''
            i+=1
        elif string[i].isalpha():
            while string[i] not in SEPERATOR:
                token+=string[i]
                i+=1
            lexme.append(token)
            token=""
        elif string[i].isdigit():
            while string[i] in NUMBERS:
                token+=string[i]
                i+=1
            if '.' in token:
                token = float(token)
            else:
                token = int(token)
            lexme.append(token)
            token=""
        elif string[i] in WHITESPACE:
            i+=1
        elif string[i] in strlib.punctuation:
            token = string[i]
            lexme.append(token)
            token=""
            i+=1
        else:
            return errorparse();
    return lexme
        

with open("test.json",'r') as f:
    lines = f.readlines();
lines = "".join(lines)

lexme = lexer(lines);
print(lexme);