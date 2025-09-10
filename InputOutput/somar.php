<?php
$inicio = microtime(true);
$soma = 10+10;
echo "10+10 = $soma";
$fim = microtime(true);
$tempo = $fim - $inicio;
printf("Processado em: %0.16f segundos", $tempo/1000000);
?>
