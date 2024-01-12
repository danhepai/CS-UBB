#include <stdio.h>
#include <string.h>

char s1[100], s2[100], rez[200];

void citireSir(char *s){
    scanf("%s", s);
}

void asmConcatenare(char *s1, int l1, char *s2, int l2, char *rez);

int main(){
    int l1, l2;
    
    printf("Sirul 1: ");
    citireSir(s1);
    printf("Sirul 2: ");
    citireSir(s2);
    
    l1 = strlen(s1);
    l2 = strlen(s2);
    
    asmConcatenare(s1, l1, s2, l2, rez);
    printf("Rez:");
    printf("%s", rez);
    
    
    return 0;
}