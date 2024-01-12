bits 32

global start

extern exit
import exit msvcrt.dll

;   Se dau 2 siruri de octeti S1 si S2 de aceeasi lungime. Sa se construiasca sirul D
;   astfel incat fiecare element din D sa reprezinte maximul dintre elementele de pe
;   pozitiile corespunzatoare din S1 si S2.

segment data use32 class=data
    s1 db 1,3,6,2,3,7
    len equ $ - s1
    s2 db 6,3,8,1,2,5
    d resb len

segment code use32 class=code
    start:  
        mov esi, 0
        
        mov ecx, len
        repeta:
            mov al, [s1 + esi]
            mov bl, [s2 + esi]
            cmp al, bl
            jae greater_or_eq
            jl less
            
            greater_or_eq:
                mov [d + esi], al
                jmp finish
            
            less:
            mov [d + esi], bl
            
            finish:
                inc esi
        loop repeta
        
        
    
        push dword 0
        call [exit]

    

        