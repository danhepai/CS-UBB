bits 32

global start        

extern exit, printf, scanf               
import exit msvcrt.dll
import printf msvcrt.dll
import scanf msvcrt.dll

;   Sa se citeasca de la tastatura un octet si un cuvant. Sa se afiseze pe ecran daca bitii octetului citit se regasesc consecutiv printre bitii cuvantului. Exemplu:
;   a = 10 = 0000 1010b
;   b = 256 = 0000 0001 0000 0000b
;   Pe ecran se va afisa NU.
;   a = 0Ah = 0000 1010b
;   b = 6151h = 0110 0001 0101 0001b
;   Pe ecran se va afisa DA (bitii se regasesc pe pozitiile 5-12).

segment data use32 class=data
    octet dw 0
    cuvant dw 0
    mesaj_citire db "Citeste de la tastatura un numar: ", 0
    format db "%d", 0
    temp resw 1
    masca resb 1
    da db "DA", 0
    nu db "NU", 0
    
    

segment code use32 class=code
    start:
        ; mesaj pentru a:
        
        push dword mesaj_citire
        call [printf]
        add esp, 4 * 1
        
        ; citire a
        
        push dword octet
        push dword format
        call [scanf]
        add esp, 4 * 2
        
        
       ; mesaj pentru b:
        
        push dword mesaj_citire
        call [printf]
        add esp, 4 * 1
        
        ; citire b
        
        push dword cuvant
        push dword format
        call [scanf]
        add esp, 4 * 2
       
        
        ; repetitiva
        
        mov ecx, 9
        verifica_bitii:
            mov al, [octet]
            mov bl, [cuvant]
            
            and al, bl
            
            cmp al, [octet]
            je found

            shr word[cuvant], 1
            
            dec ecx
            cmp ecx, 0
            jne verifica_bitii
        
        ; not found
        push dword nu
        call [printf]
        add esp, 4
        
        jmp finish
        
        found:
            push dword da
            call [printf]
            add esp, 4

        finish:
        push    dword 0      
        call    [exit]       
