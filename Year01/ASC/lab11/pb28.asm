bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
                         
import scanf msvcrt.dll
import printf msvcrt.dll
import gets msvcrt.dll
extern printf, exit, scanf, gets

extern concatenare1
extern concatenare2

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    s1 resb 40
    len1 resd 1
    s2 resb 40
    s3 resb 40
    new_line db 10, 0
    mesajcitiresir db 'Citeste un sir: ', 0 
    mesajafisaresir db 'Sirul citit este %s ' ,0

    
segment code use32 class=code
    start:
        ;mesaj pt citire sir
        push dword mesajcitiresir
        call [printf]
        add esp,4*1
        
       ;citire efectiva sir        
        push dword s1
        call [scanf]
        add esp, 4*1
        
        mov [len1], eax
        
    
        push dword len1
        push dword s2
        push dword s1
        
        call concatenare1
        
        push dword s2
        call [printf]
        add esp, 4 * 1
        
        ;----------------------------------
        
        push dword new_line
        call[printf]
        add esp, 4
        
        ;----------------------------------
        
        push dword len1
        push dword s3
        push dword s1
        
        call concatenare2
        
        push dword s3
        call [printf]
        add esp, 4 * 1
        
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
