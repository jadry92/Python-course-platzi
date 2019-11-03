def fib(n):
   if n == 1 or n == 2:
       resul = 1
   else:
       resul = fib(n-1) + fib(n-2)
   return resul

print(fib(6))

