# contador até 1mi
import time

start = time.perf_counter()
for p in range(1_000_000):
    pass
end = time.perf_counter()

print(f"Tempo de execução - contar até 1mi {(end-start)} s")
# >>> Tempo de execução - contar até 1mi 0.051368702000218036 s
# >>> Tempo de execução - contar até 1mi 0.0739227670001128 s
# >>> Tempo de execução - contar até 1mi 0.08455388199945446 s
# >>> Tempo de execução - contar até 1mi 0.07860575299946504 s

# Compressão de Listas
start = time.perf_counter()
contar = [p for p in range(1_000_000)]
end = time.perf_counter()

print(f"Tempo de execução - contar até 1mi {(end-start)} s")
# >>> Tempo de execução - contar até 1mi 0.030854626999825996 s
# >>> Tempo de execução - contar até 1mi 0.03853460400023323 s
# >>> Tempo de execução - contar até 1mi 0.04224357200018858 s
# >>> Tempo de execução - contar até 1mi 0.03570912500072154 s