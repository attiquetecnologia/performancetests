<?php
$inicio = microtime(true);

$a = 10;
$b = 10;
$soma = $a+$b;
echo "A soma entre a: $a e b: $b é $soma\n";
$fim = microtime(true);
$tempo = $fim - $inicio;
printf("Processado em: %0.16f segundos\n", $tempo/1000000);
?>
