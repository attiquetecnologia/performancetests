const start = performance.now();

for (let i = 0; i < 1_000_000; i++) {}

const end = performance.now();
const tempoExecucao = end - start;

console.log(`Tempo de execução - contar até 1mi ${tempoExecucao.toFixed(6)} ms`);
// Tempo de execução - contar até 1mi 2.068794 ms
// Tempo de execução - contar até 1mi 5.223873 ms
// Tempo de execução - contar até 1mi 5.719761 ms
// Tempo de execução - contar até 1mi 5.373608 ms