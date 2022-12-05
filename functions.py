
#takes a string like x^2+x+1
#returns 2 lists [x^2,x,1] and [+1,+1] that creates parts of the function and stores the coefficients associatd with them

def funcsplit(func):
    parts = []
    coefs = []
    part = ''
    coef = ''
    for ele,i in enumerate(func):
        if i != '(' and len(part) < 1:
            coef += i
        elif i == '(' or len(part) > 0:
            part += i
        if ele < len(func) - 1:
            if i == ')' and func[ele+1] != ')':
                part = part[1:-1]
                parts.append(part)
                if coef == '':
                    coefs.append('+1')
                else:
                    coefs.append(coef)
                part = ''
                coef = ''
        elif i == ')':
                part = part[1:-1]
                parts.append(part)
                if coef == '':
                    coefs.append('+1')
                else:
                    coefs.append(coef)
                part = ''
                coef = ''
    return parts, coefs

#takes a coefficient and a function
#right now it is only useful power and constant funciton, but will be more applicable in the regular conversion
#returns a new coefficient which is the product of the original coeficient and the coeficient of the function 

def coefcombine(coef,func):
    funccoef = ''
    sign = ''
    if coef[0] not in ('+','-'):
        coef = '+' + coef
    if len(coef) < 2:
        coef += '1'
    if func[0:1] != '-':
        sign = coef[0]
    elif coef[0] == '+':
        sign = '-'
    else:
        sign = '+'

    for i in func:
        if i in ['1','2','3','4','5','6','7','8','9']:
            funccoef += i
        elif i == '-':
            pass
        else:
            break
    if len(funccoef) > 0:
        newcoef = sign + str(int(coef[1:])*int(funccoef))
    else:
        newcoef = sign + coef[1:]
    return newcoef

#takes a function in the form n(func)+n(func)... coefficents in front and the base function in the parenthesises
#does not include product, quotient or chain rule (so no func*func, func/func or func(func))
#returns a new function that is the derivative of the original function

def simpleconversion(func):
    newparts = []
    newfunc = ''
    newcoefs = []
    split = funcsplit(func)
    parts = split[0]
    coefs = split[1]
    for part in parts:
        if part[0] == 'x':
            newparts.append(power(part))
        elif part[0] == 'e':
            newparts.append(exp(part))
        elif part[0] == 'l':
            newparts.append(log(part))
        elif part[0] not in ['1','2','3','4','5','6','7','8','9']:
            newparts.append(trig(part))
        else:
            newparts.append(constant(part))
    for i, part in enumerate(newparts):
        newcoef = coefcombine(coefs[i],part)
        newpart = ''
        ln = False
        count = 0
        if len(part) > 1 and part[0:2] == '1/':
            ln = True
        for char in part:
            if char in ['-','+','1','2','3','4','5','6','7','8','9'] and ln == False:
              count += 1
            else:
                break
        newpart = part[count:]
        newparts[i] = newpart
        if newcoef[-1] == '1' and len(newcoef) == 2:
            newcoefs.append(newcoef[0])
        else:
            newcoefs.append(newcoef)
    for i, part in enumerate(newparts):
        if newcoefs[i] + part not in ('+0','-0'):
            newfunc += newcoefs[i] + part
    if newfunc[0] == '+':
        newfunc = newfunc[1:]
    return newfunc


#this will be the fully functional conversion function

def conversion(func):
    pass

#takes a constant and aplies the constant rule
#finished

def constant(part):
    part = "0"
    return part

#takes a input in the form of x^n
#returns nx^n-1

def power(part):
    if len(part) == 1:
        part = "1"
    else:
        var = part[0]
        pow = part[2:]
        if int(pow) - 1 == 1:
            part = pow + var
        else:
            part = pow + var + "^" + str(int(pow)-1)
    return part

#takes in the 6 trig functions in form of sin(x), cos(x)... will add inverse trig functions or make a seperate function in future
#returns respective derivative of function observed in the dict 'trigfunc'

def trig(part):
    start = part.index('(')
    end = len(part) - 1
    inside = part[start+1:end]
    trigfunc = {'sin':'cos({})'.format(inside),'cos':'-sin({})'.format(inside),'tan':'sec^2({})'.format(inside),'sec':'tan({})sec({})'.format(inside,inside),'csc':'-cot({})csc({})'.format(inside,inside),'cot':'csc^2({})'.format(inside)}
    if part[0:3] in trigfunc:
        return trigfunc[part[0:3]]

#takes e^x will add a^x in future
# returns e^x   

def exp(part):
    return part

#takes ln(x) will add loga() in future
#returns x^-1 (1/x was causing issues due to combinecoef function, may fix that in the future if it is at all reasonable)
def log(part):
    inner = part[3:-1]
    return inner + '^-1'

#these are going to be a nightmare
def product(part):
    pass

def quotient(part):
    pass

def chain(part):
    pass


#testing:
#print(coefcombine('2','56x^2'))
#print(funcsplit('(x^2)+2(x)'))
#print(simpleconversion('2(x^56)-4(sin(x))+3(e^x)+5(ln(x))+(1)'))