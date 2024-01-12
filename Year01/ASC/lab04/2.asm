bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

;exercise one: a-b-(c-d)+d, where a - byte, b - word, c - doubleword, d - qword, and everything is with sign.
                          
segment data use32 class=data
    a db 1
    b dw 2
    c dd 3
    d dq 4

segment code use32 class=code
    start:
        mov bl, [a]
        movsx bx, bl
        sub bx, [b] ; bx: a-b
        movsx ebx, bx ;ebx: a-b
        mov ecx, 0
        
        mov eax, [c]
        cdq ; edx:eax - c
        sub eax, dword[d+0]
        sbb edx, dword[d+4] ; (c-d), and res -> edx:eax
        sub ebx, eax
        sbb ecx, edx ;in ecx:ebx -> "a-b-(c-d)"
        add ebx, dword[d+0]
        adc ecx, dword[d+4]
         
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
