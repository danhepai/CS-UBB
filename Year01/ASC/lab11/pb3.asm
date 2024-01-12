bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
                         
import printf msvcrt.dll
import exit msvcrt.dll
import scanf msvcrt.dll
extern printf, exit, scanf

extern concatenare1
extern concatenare2

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s1 db 'a1b2c3'
    len1 equ $-s1
    s2 db 'd5e6'
    len2 equ $-s2
    s3 times len1+len2+1 db 0

; our code starts here
segment code use32 class=code
    start:
        push dword len1
        push dword len2
        push dword s3
        push dword s2
        push dword s1
        
        call concatenare1
        
        push dword s3
        call [printf]
        add esp, 4 * 1
        
        ;----------------------------------
        
        push dword len1
        push dword len2
        push dword s3
        push dword s2
        push dword s1
        
        call concatenare2
        
        push dword s3
        call [printf]
        add esp, 4 * 1
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
