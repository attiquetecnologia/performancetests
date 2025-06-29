import time

start = time.perf_counter()
<<<<<<< HEAD
print(f"10 + 10 = {10+10}")
=======

a: int = 10
b: int = 10
print(f"A soma entre a:{a} e b:{b} é {a+b}")

>>>>>>> 25767b28e9e66d52afc2c4930ff9de1b8c3fddfa
end = time.perf_counter()

print(f"Tempo de execução {(end-start)} s")