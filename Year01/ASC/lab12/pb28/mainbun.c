#include <stdio.h>
#include <string.h>

char s[100], litereMiciSir[100], litereMariSir[100];

void citireSir(char *s){
    scanf("%s", s);
}

void litereMici(char *s, int len, char *litereMiciSir);
    
void litereMari(char *s, int len, char *litereMariSir);


int main(){
    int len;
    
    printf("Sirul: ");
    citireSir(s);
    
    len = strlen(s);
    
    litereMari(s, len, litereMariSir);
    litereMici(s, len, litereMiciSir);

    printf("Sirurile sunt:\n");
    printf("%s\n", litereMariSir);
    printf("%s\n", litereMiciSir);
   
    return 0;
}