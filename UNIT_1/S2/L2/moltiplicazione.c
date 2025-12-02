#include <stdio.h>

int main() {
    int a;
    int b;
    int moltiplicazione;

    printf("Inserisci il primo numero: ");
    scanf("%d", &a);
    printf("Inserisci il secondo numero: ");
    scanf("%d", &b);

    moltiplicazione = a * b;

    printf("Il risultato è: %d", moltiplicazione);
    return 0;
}
