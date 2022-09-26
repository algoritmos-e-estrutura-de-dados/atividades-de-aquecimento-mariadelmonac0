a = int(input()) 
b = int(input())
c = int(input())

greatestab = (a + b + abs(a - b))/2
greatestabc = (greatestab + c + abs(greatestab - c))/2

print(f"{int(greatestabc)} eh o maior")