bits 32 

global start        


extern exit, printf              
import exit msvcrt.dll   
import printf msvcrt.dll

;   Se dau cuvantul A si octetul B. Sa se obtina dublucuvatul C:
;   bitii 0-3 ai lui C au valoarea 1
;   bitii 4-7 ai lui C coincid cu bitii 0-3 ai lui A
;   bitii 8-13 ai lui C au valoarea 0
;   bitii 14-23 ai lui C coincid cu bitii 4-13 ai lui A
;   bitii 24-29 ai lui C coincid cu bitii 2-7 ai lui B
;   bitii 30-31 au valoarea 1

segment data use32 class=data
    a dw 321
    b db 21
    c dd 0xFFFFFFFF
    format db "%x", 0
    rez dd 0


segment code use32 class=code
    start:
        ; 0 - 3
        mov ebx, 0x0000000F
        or [rez], ebx
        
        ; 4 - 7
        mov ax, [a]
        mov bx, 0x000F
        and ax, bx
        movzx eax, ax
        shl eax, 4
        or [rez], eax
        
        ; 8 - 13
        mov ax, 1100_0000_1111_1111b
        movzx eax, ax
        and [rez], eax
        
        ; 14 - 23
        mov ax, [a]
        mov bx, 0011_1111_1111_0000b
        and ax, bx
        movzx eax, ax
        shl eax, 10
        or [rez], eax
        
        ; 24 - 29
        mov al, [b]
        mov bl, 0111_1100b
        and al, bl
        movzx eax, al
        shl eax, 22
        or [rez], eax
        
        ; 30 - 31
        mov eax, 0xC0000000
        or [rez], eax
        
        ; PRINT TO CHECK
        push dword [rez]
        ;push eax
        push dword format
        call [printf]
        add esp, 4 * 2
        
    
        
        push    dword 0      
        call    [exit]       
