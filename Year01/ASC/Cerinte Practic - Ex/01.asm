bits 32

global start        

extern exit, scanf, printf           
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    formatDecimal db "%d", 0
    formatHexa db "%x", 0
    num resd 1
    restl db " rest: ", 0
    restul dw 0
    
segment code use32 class=code
    start:
        mov ebx, 0
        ; NUM 1
        push dword num
        push dword formatDecimal
        call [scanf]
        add esp, 4 * 2
        
        add ebx, [num]
        
        ; NUM 2
        push dword num
        push dword formatDecimal
        call [scanf]
        add esp, 4 * 2
        
        add ebx, [num]
        
        ; NUM 3 
        push dword num
        push dword formatDecimal
        call [scanf]
        add esp, 4 * 2
        
        add ebx, [num]
        
        ; IN EAX E SUMA LOR -> o schimb in DX:AX
        push ebx
        pop ax
        pop dx
        
        ; IN BX PUN 3 -> IMPART DX:AX LA BX
        mov bx, 3
        
        ; IMPART -> CAT IN AX, REST IN DX
        idiv bx
        
        mov [restul], dx
        
        cwde ; CONVERT AX TO EAX
        push eax
        push formatHexa
        call [printf]
        add esp, 4 * 2
        
        push restl
        call [printf]
        add esp, 4
        
        mov ax, [restul]
        cwde
        
        push eax
        push formatHexa
        call [printf]
        add esp, 4 * 2
        
        push    dword 0      
        call    [exit]
