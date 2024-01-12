bits 32
global start        

extern exit, scanf, printf, fopen, fprintf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
                         
segment data use32 class=data
    n resd 1
    formatDecimal db "%d", 0
    formatHexa db "%x", 0
    formatSir db "%s", 0
    num resd 1
    max db 0
    temp resd 1
    citeste db "citeste nr: ", 0
    first_byte resb 1
    second_byte resb 1
    sirbytes resb 20
    len dd 0
    temp2 dd 0
    filename db "output.txt", 0
    descriptor dd -1
    mod_access db "w", 0
    
    
segment code use32 class=code
    start:
        push dword mod_access
        push dword filename
        call [fopen]
        add esp, 8
        mov [descriptor], eax
        
        push dword n
        push dword formatDecimal
        call [scanf]
        add esp, 4*2
        
        mov edi, sirbytes
        
        mov ecx, [n]
        repeta:
            mov [temp], ecx
            
            push dword citeste
            call [printf]
            add esp, 4
            
            push dword num
            push dword formatHexa
            call [scanf]
            add esp, 4*2
            
            mov ebx, num
            
            mov al, [ebx + 0]
            mov ah, [ebx + 2]
            cmp al, ah
            jl mai_mic
            
            movzx eax, al
            push eax
            push dword formatHexa
            push dword descriptor
            call [fprintf]
            add esp, 4*3
            
            mov al, [ebx + 4]
            mov ah, [ebx + 6]
            cmp al, ah
            jl mai_mic
            
            movzx eax, al
            push eax
            push dword formatHexa
            push dword descriptor
            call [fprintf]
            add esp, 4*3
            
            mai_mic:            
            mov ecx, [temp]
        loop repeta
        
        
    
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
