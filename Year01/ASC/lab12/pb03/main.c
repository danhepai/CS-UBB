#include <stdio.h>
#include <string.h>

void citireSir(char s[]){
    scanf("%s", s);
}

void asmLitereMici(s[], len, litereMici[]);
    
void asmLitereMari(s[], len, litereMari[]);


int main(){
    char s[100], litereMici[100], litereMari[100];
    int len;
    
    printf("Sirul: ");
    citireSir(s);
    
    len = strlen(s);
    
    asmLitereMici(s, len, litereMici);
    asmLitereMari(s, len, litereMari);
    
    printf("Sirurile sunt:\n");
    printf("%s\n", litereMici);
    printf("s%", litereMari);

    
    return 0;
}