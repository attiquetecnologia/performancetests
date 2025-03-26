package InputOutput;

public class HelloWorld {
    public static void main(String[] args){

        long tempoInicial = System.currentTimeMillis();
        System.out.println("Hello World");
        long tempoFinal = System.currentTimeMillis();
        System.out.printf("%f ms%n", (tempoFinal - tempoInicial) / 1000d);
    }
}