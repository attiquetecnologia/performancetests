<?php
$inicio = microtime(true);
<<<<<<< HEAD
$soma = 10+10;
echo "10+10 = $soma";
$fim = microtime(true);
$tempo = $fim - $inicio;
printf("Processado em: %0.16f segundos", $tempo/1000000);
?>
=======

$a = 10;
$b = 10;
$soma = $a+$b;
echo "A soma entre a: $a e b: $b é $soma\n";
$fim = microtime(true);
$tempo = $fim - $inicio;
printf("Processado em: %0.16f segundos\n", $tempo/1000000);
?>
>>>>>>> 25767b28e9e66d52afc2c4930ff9de1b8c3fddfa
