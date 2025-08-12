public class ContarFor {
    public static void main(String[] args){
        long tempoInicial = System.currentTimeMillis();
        
        for (int i=0; i<=1_000_000; i++){}
        
        long tempoFinal = System.currentTimeMillis();
        System.out.printf("%f ms%n", (tempoFinal - tempoInicial) / 1000d);
        // >>> 0,002000 ms
        // >>> 0,006000 ms
        // >>> 0,006000 ms
        // >>> 0,005000 ms
    }
}