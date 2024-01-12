bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

; Se da un sir de dublucuvinte. Sa se obtina sirul format din octetii superiori ai
; cuvitelor superioare din elementele sirului de dublucuvinte care sunt divizibili cu 3.

segment data use32 class=data
    s dd 03000000h, 06000000h, 04000000h
    ls equ ($-s) / 4
    d resd ls
    temp resd 1


segment code use32 class=code
    start:
        mov esi, s ;esi -> index for s
        mov edi, d ;edi -> index for d
        CLD ; direction ->
        mov ecx, ls ;for the loop process
        repeta:
            LODSD ;MOV EAX, DWORD[S+ESI], ESI += 4
            mov [temp], eax ;making a copy of eax
            mov ebx, 3
            
            ;trb sa mut eax in dx:ax
            
            mov edx, 0
            push eax
            pop ax
            pop dx
            
            ; INTEGER OVERFLOW, why?
            div bx ; DX am rest, AX am cat
            
            CMP DX, 0
            JE divizibil
            JNE nedivizibil
            
            divizibil:
                mov eax, [temp]
                STOSD ; [d+edi] = EAX , edi += 4
                
                JMP final
                
            nedivizibil:
                nop
            
            final:
            loop repeta
            
            
        push    dword 0
        call    [exit]       
            