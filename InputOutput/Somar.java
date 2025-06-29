public class Somar {
    public static void main(String[] args){

        long tempoInicial = System.currentTimeMillis();
        int a = 10;
        int b = 10;
        int soma = a + b;
        System.out.println("A soma entre a:10 e b:10 é " + soma);
        long tempoFinal = System.currentTimeMillis();
        System.out.printf("%f ms%n", (tempoFinal - tempoInicial) / 1000d);
    }
}