bits 32

global start        


extern exit, printf
import exit msvcrt.dll 
import printf msvcrt.dll   

; (a*a/b+b*b)/(2+b)+e-x; a-byte; b-word; e-doubleword; x-qword 
segment data use32 class=data
    a db 2
    b dw 4
    e dd 12
    x dq 16
    temp resw 1
    format db "%d", 0


segment code use32 class=code
    start:
        mov al, [a]
        imul al             ; -> AX = a * a*a
        
        cwd                 ; -> AX -> DX:AX
        mov bx, [b]
        idiv bx             ; -> AX: a*a/b
        mov [temp], ax      ; word temp -> AX
        
        mov ax, [b]
        imul ax             ; -> DX:AX b*b
        
        add ax, [temp]
        adc dx, 0           ; DX:AX -> (a*a/b+b*b)
        
        mov bx, [b]         ; BX -> 2 + b
        add bx, 2
        
        idiv bx             ; AX -> (a*a/b+b*b)/(2+b)
        
        cwde
        add eax, [e]
        mov edx, 0
        
        mov ecx, [x+4]      ; CAREFUL ABT LITTLE ENDIAN. GOT FUCKED UP FIRST TIME
        mov ebx, [x]
        
        sub eax, ebx
        sbb edx, ecx
        
        push eax
        push dword format
        call [printf]
        add esp, 4 * 2
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
