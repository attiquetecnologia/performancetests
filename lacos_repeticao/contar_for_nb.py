import time
from numba import njit
import numpy as np

# --- Exemplo 1: Loop Simples com Numba ---
# Esta função é um excelente caso de uso para a Numba,
# pois realiza uma operação puramente numérica em um loop.
@njit
def contar_loop_simples():
    total = 0.0
    for p in range(1_000_000):
        total += p
    return total

print("--- Loop Simples com Numba ---")
# 1. Primeira chamada (inclui o tempo de compilação JIT)
print("Executando a primeira vez (compilação JIT)...")
start_compilacao = time.perf_counter()
contar_loop_simples()
end_compilacao = time.perf_counter()
print(f"Tempo da primeira execução (compilação JIT): {(end_compilacao - start_compilacao) * 1000:.6f} ms")
print("-" * 30)

# 2. Segunda e subsequentes chamadas (código já otimizado)
print("Executando várias vezes (código já compilado)...")
start_otimizado = time.perf_counter()
for _ in range(5):
    contar_loop_simples()
end_otimizado = time.perf_counter()
tempo_otimizado_total = end_otimizado - start_otimizado
print(f"Tempo total para 5 execuções otimizadas: {tempo_otimizado_total * 1000:.6f} ms")
print(f"Tempo médio por execução: {(tempo_otimizado_total / 5) * 1000:.6f} ms")
print("-" * 30)

# --- Exemplo 2: Compressão de Listas com Numba (o que você estava testando) ---
# Numba não é ideal para criar objetos Python nativos como listas.
# O desempenho aqui não será tão impressionante quanto o exemplo 1.
@njit
def contar_lista_numba():
    return [p for p in range(1_000_000)]

print("--- Compressão de Listas com Numba ---")
# 1. Primeira chamada (inclui o tempo de compilação JIT)
print("Executando a primeira vez (compilação JIT)...")
start_compilacao = time.perf_counter()
contar_lista_numba()
end_compilacao = time.perf_counter()
print(f"Tempo da primeira execução (compilação JIT): {(end_compilacao - start_compilacao) * 1000:.6f} ms")
print("-" * 30)

# 2. Segunda e subsequentes chamadas (código já otimizado)
print("Executando várias vezes (código já compilado)...")
start_otimizado = time.perf_counter()
for _ in range(5):
    contar_lista_numba()
end_otimizado = time.perf_counter()
tempo_otimizado_total = end_otimizado - start_otimizado
print(f"Tempo total para 5 execuções otimizadas: {tempo_otimizado_total * 1000:.6f} ms")
print(f"Tempo médio por execução: {(tempo_otimizado_total / 5) * 1000:.6f} ms")
print("-" * 30)
