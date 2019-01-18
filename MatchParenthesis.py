def main():
    par = list()
    for i in s:
        if i == '[' or i == '{' or i == '(':
            par.append(i)
        else:
            if len(par) == 0:
                return False
            last = par[-1]
            if (i == ']' and last == '[') or (i == ')' and last == '(') or (i == '}' and last == '{'):
                par.pop()
            else:
                return False
    if len(par) != 0:
        return False
    else:
        return True