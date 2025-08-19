System.out.println('--- Bem-vindo à Calculadora de Parcelas! ---');

const PARCELAS_SEM_JUROS_MAX = 6; // Define o máximo de parcelas sem juros

let preco = 120.0; //precço do produto, tenis
const DESCONTO = 0.05;
const JUROS_MES = 0.02;

System.out.println('--- ESCOLHA UMA FORMA DE PAGAMENTO ---\n1 - A Vista\n2 - Parcelado');
let forma_pgto = readlineSync.question("Resposta: ");
System.out.println("Forma de pagamento escolhida:", forma_pgto);
switch(forma_pgto) {
    case "1":
        let desconto = preco * DESCONTO;
        preco = preco - desconto;
        System.out.println("Preço a vista:", preco);
        break;
    case "2":
        let n_parcelas = readlineSync.question("Parcele em até 6x sem juros: ");
        n_parcelas = parseInt(n_parcelas); //converte para inteiro
        if (n_parcelas<=6){
            for (p=1; p<=n_parcelas; p++){
                System.out.println(`Parcela s/juros ${p} -> R$ ${preco/n_parcelas}`);
            }
        } else {
            for (p=1; p<=n_parcelas; p++){
                let juros = preco*n_parcelas*JUROS_MES;
                System.out.println(`Parcela c/juros ${p} -> R$ ${preco/n_parcelas+juros}`);
            }
        }
        break;
    default:
        System.out.println("Escolha uma opção do menu.");
        break;
}
// const totalCompra = parseFloat(totalCompraStr.replace(',', '.')); // Garante que seja float e aceita vírgula