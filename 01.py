#Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный. 

def parse(inp):
    parsed = []
    num = ''
    for i in inp:
        if i.isdigit() or i == '.':
            num += i
        elif i == '-' and (not parsed or parsed and parsed[-1] == '(' and not num):
            num += i
        # elif not parsed and i == '-':
        #     num += i
        # elif i == '-' and parsed and parsed[-1] == '(' and not num:
        #     num += i
        elif num:
            parsed.append(float(num))
            num = ''
        if i == '(':
            parsed.append(i)
        elif i in ')-+*/' and parsed and parsed[-1] != '(':
            parsed.append(i)
    if num:
        parsed.append(float(num))
    return parsed

def polsk(parsed):
    result = []
    stack = []
    for i in parsed:
        if type(i) == float:
            result.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack:
                char = stack.pop()
                if char == '(':
                    break
                result.append(char)
        elif i in '-+*/':
            if not stack or stack[-1] == '(':
                stack.append(i)
            elif i in '-+':
                while stack:
                    if stack[-1] == '(':
                        break
                    result.append(stack.pop())
                stack.append(i)
            elif i in '*/':
                while stack:
                    x = stack.pop()
                    if x in '(-+':
                        stack.append(x)
                        break
                    else:
                        result.append(x)
                stack.append(i)
    while stack:
        result.append(stack.pop())
    return result

def calculation(sorted):
    result = []
    for i in sorted:
        if type(i) == float:
            result.append(i)
        elif i in '-+*/':
            y = result.pop()
            x = result.pop()
            if i == '-':
                result.append(x-y)
            elif i == '+': 
                result.append(x+y)   
            elif i == '*':
                result.append(x*y)
            elif i == '/':
                result.append(x/y)
    return result[0]   
 
#inp = '2*(17/(7-(1+2))*3-(2-(9+1)))'
#inp = '10/((-1+2)*3)'
inp = '-7*(21-(3+4))*4-((6+1)*3)*11/(-7-(0.5+2.5))/2-(6*(2+1))*(10/(8-(2+3))/2-(2+(3-6))+62/(5+(1+1))*4-(7-(3+1)))'
#inp = '-1+2*3+4*(-3+2)'
# par = (parse(inp))
# print(f'ПАРСИНГ {par}')
# pol = polsk(par)
# print(f'ПОЛЬСКИЙ {pol}')

# Проверок на корректность записи выражения и деления на ноль нет
print(f'Самописная: {calculation(polsk(parse(inp)))}')
print(f'Встроенная: {eval(inp)}')