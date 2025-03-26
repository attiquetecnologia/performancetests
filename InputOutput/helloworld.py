import time

start = time.perf_counter()
print("Hello World")
end = time.perf_counter()

print(f"Tempo de execução {(end-start)} s")