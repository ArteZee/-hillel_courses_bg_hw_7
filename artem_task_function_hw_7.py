def side(a):
    a = 33 ** 2
    pass


def palindrome():
    ...


def is_year_leap (year):
    if year %4==0 and year %100!=0:
        return True
    else:
        return False

print(is_year_leap(2105))

print("Введиет число:")
a= input()
print("Введиnt действие:")
b= input(str())
print("Введиет число:")
c=input()

def arethmetic (a,b,c):
    if b == "+":
       res=int(a)+int(c)
       return res
    elif b == "-":
        res=int(a)-int(c)
        return res
    elif b == "/":
        res= int(a)/int(c)
        return res
    elif b == "*":
        res = int(a)*int(c)
        return res
    elif b =="**":
        res = int(a)**int(c)
        return res
    elif b =="//":
        res = int(a)//int(c)
        return res

print(arethmetic(a,b,c))

list_of_product = ["Картофель", "Морковь", "Лук", "Чеснок", "Петрушка", "Укроп", "Яблоки", "бананы", "Лимон", "Морковь", "Лук", "Чеснок", "Петрушка", "Укроп", "Яблоки", "бананы", "Лимон", "Морковь", "Лук", "Чеснок", "Петрушка", "Укроп", "Яблоки", "бананы", "Лимон", "Морковь", "Лук", "Чеснок", "Петрушка", "Укроп", "Яблоки", "бананы", "Лимон"]

def selected (list_of_product):
    object = {x for x in list_of_product }
    return object

print(selected(list_of_product))