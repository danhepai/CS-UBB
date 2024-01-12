bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions

;exercise one, without sign: d - (7 - a * b + c) / a - 6 + x / 2; where: a,c-byte; b-word; d-doubleword; x-qword
segment data use32 class=data
    a db 1
    c db 1
    b dw 1
    d dd 1
    x dq 1

; our code starts here
segment code use32 class=code
    start:
        mov al, [a]
        mov ah, 0
        mul word[b] ;rez il am in dx:ax -> 
        
        push dx
        push ax
        pop eax ;eax = a * b
        
        mov bl, [c]
        mov bh, 0
        add eax, ebx ; eax = a * b + c
        
        mov ecx, 7
        sub ecx, eax
        mov eax, ecx ; eax = (7 - a * b + c)
        
        mov bl, [a]
        mov bh, 0
        div bx ; rez -> ax: (7 - a * b + c) / a
        
        mov bx, 6
        sub ax, bx ; ax -> (7 - a * b + c) / a - 6
        
        mov ebx, [d] ;ebx = d
        movzx eax, ax ;eax = (7 - a * b + c) / a - 6
        sub ebx, eax ; ebx = d - (7 - a * b + c) / a - 6
        
        mov eax, qword[x + 0]
        mov edx, qword[x + 8]
        
        mov ecx, 2
        div ecx ;edx:eax / ecx -> rez in eax: x / 2
        add ebx, eax ;rez final in ebx
        
        
        mov al, [a]
        mov ah, 0
        mul word[b] ;rez il am in dx:ax -> 
        
        
        ; -------------------        
        ;With sign: d - (7 - a * b + c) / a - 6 + x / 2; where: a,c-byte; b-word; d-doubleword; x-qword
        
        mov bl, [c]
        add bl, 7 ; bl = 7 + c
        movsx ebx, bl ; ebx = 7 + c
        
        mov al, [a]
        cbw ; ax = a
        
        imul word[b] ; dx:ax = a * b
        
        push dx
        push ax
        pop eax ;in eax = a * b
        sub ebx, eax
        mov eax, ebx ; eax = (7 - a * b + c)
        
        push eax
        pop dx
        pop ax ; in dx:ax = (7 - a * b + c)
        
        mov bl, [a]
        movsx bx, bl ; in bx = a
        
        idiv bx ; in al = (7 - a * b + c) / a
        sub al, 6 ; in al = (7 - a * b + c) / a - 6
        
        mov bl, al ; bl = (7 - a * b + c) / a - 6
        
        mov eax, dword[x+0]
        mov edx, dword[x+4] ; edx:eax = x
        
        mov ebx, 2
        
        idiv ebx ; in eax = x / 2
        add eax, [d] ; in eax = d + x / 2
        
        movsx ebx, bl
        sub eax, ebx ; eax = d - (7 - a * b + c) / a - 6 + x / 2 cu semn

        ; -------------------

        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
