const t0 = performance.now();

let a = 10;
let b = 10;
console.log(`A soma entre a:${a} e b:${b} é ${a+b}`);
const t1 = performance.now();
console.log(`Call to doSomething took ${t1 - t0} milliseconds.`);
