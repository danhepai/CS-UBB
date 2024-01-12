bits 32

global start        

extern exit, fopen, scanf, fprintf, printf, fclose
import exit msvcrt.dll
import fopen msvcrt.dll
import scanf msvcrt.dll
import fprintf msvcrt.dll
import printf msvcrt.dll
import fclose msvcrt.dll

; Se da un nume de fisier (definit in segmentul de date). Sa se creeze un fisier cu numele dat, ; apoi sa se citeasca de la tastatura numere si sa se scrie din valorile citite in fisier
; numerele divizibile cu 7, pana cand se citeste de la tastatura valoarea 0.


segment data use32 class=data
    fisier db "output.txt", 0
    mod_access db "w", 0
    descriptor resd 1
    mesaj_pentru_citire db "Scrie:", 0
    num resd 1
    format db "%d", 0
    
segment code use32 class=code
    start:
        
        push dword mod_access
        push dword fisier
        call [fopen]
        add esp, 4 * 2
        
        mov [descriptor], eax
        
        cmp eax, 0
        je eroare_la_citire
        
        push mesaj_pentru_citire
        call [printf]
        add esp, 4 * 1
        
        repeta:
            push dword num
            push dword format
            call [scanf]
            add esp, 4 * 2
            
            cmp dword[num], 0
            je cititzero
            
            mov bx, 7   
            
            mov eax, [num]
            push eax    ; convert eax -> dx:ax
            pop ax
            pop dx
            
            div bx
            cmp dx, 0   ; dx:ax % bx -> dx
            jne nedivizibil
            ; if here means it is -> write in file
            
            push dword [num]
            push dword format
            push dword [descriptor]
            call [fprintf]
            add esp, 4 * 2
            
            nedivizibil:
        jmp repeta
        
        cititzero:
        
        push dword [descriptor]
        call [fclose]
        add esp, 4 * 1
        
        eroare_la_citire:
        push    dword 0      
        call    [exit]       
