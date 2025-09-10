import time

start = time.perf_counter()
print(f"10 + 10 = {10+10}")
end = time.perf_counter()

print(f"Tempo de execução {(end-start)} s")