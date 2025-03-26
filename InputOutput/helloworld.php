<?php
$inicio = microtime(true);
echo "Hello World";
$fim = microtime(true);
$tempo = $fim - $inicio;
printf("Processado em: %0.16f segundos", $tempo/1000000);
?>