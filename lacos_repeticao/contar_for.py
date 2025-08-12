# contador até 1mi
import time

start = time.perf_counter()
for p in range(1_000_000):
    pass
end = time.perf_counter()

print(f"Tempo de execução - contar até 1mi {(end-start)* 1000:.6f} ms")
# Tempo de execução - contar até 1mi 70.638609 ms
# pypy: 
# Tempo de execução - contar até 1mi 16.945604 ms
# Tempo de execução - contar até 1mi 10.941131 ms
# pyc - cpython:
# Tempo de execução - contar até 1mi 69.843812 ms
# Tempo de execução - contar até 1mi 90.051050 ms
# Tempo de execução - contar até 1mi 95.942532 ms

# Compressão de Listas
start = time.perf_counter()
contar = [p for p in range(1_000_000)]
end = time.perf_counter()

print(f"Tempo de execução - contar até 1mi {(end-start)* 1000:.6f} ms")
# Tempo de execução - contar até 1mi 31.542276 ms
# pypy: 
# Tempo de execução - contar até 1mi 9.192279 ms
# Tempo de execução - contar até 1mi 9.828184 ms
# pyc - cpython:
# Tempo de execução - contar até 1mi 33.817559 ms
# Tempo de execução - contar até 1mi 39.015471 ms
# Tempo de execução - contar até 1mi 49.092533 ms