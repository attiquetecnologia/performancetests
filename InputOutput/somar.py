import time

start = time.perf_counter()

a: int = 10
b: int = 10
print(f"A soma entre a:{a} e b:{b} é {a+b}")

end = time.perf_counter()

print(f"Tempo de execução {(end-start)} s")