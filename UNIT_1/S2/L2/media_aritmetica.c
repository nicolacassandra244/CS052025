#include <stdio.h>

int main()   {
    int num1;
    int num2;
    int num3;
    int somma;
    int media;

    printf("Inserisci primo numero: ");
    scanf("%d", &num1);
    printf("Inserisci secondo numero: ");
    scanf("%d", &num2);
    printf("Inserisci terzo numero: ");
    scanf("%d", &num3);

    //Somma dei numeri
    somma = num1 + num2 + num3;
    //Calcolo della media facendo somma diviso il numero degli elementi
    media = somma / 3;
    //Stampare risultato
    printf("il risultato è %d", media);
    return 0;
}