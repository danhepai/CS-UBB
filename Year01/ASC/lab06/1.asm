; TRIED MY BEST, DIDN'T MAKE IT.
; NASM GOT ME FUCKED UP

bits 32

global start

extern exit, printf
import exit msvcrt.dll
import printf msvcrt.dll

;   Se dau doua siruri de octeti s1 si s2. Sa se construiasca sirul de octeti d, care contine
;   pentru fiecare octet din s2 pozitia sa in s1, sau 0 in caz contrar.

segment data use32 class=data
    s1 db 0x0A, 0x0B, 0x0C, 0x0E, 0x0F
    n equ $ - s1
    s2 db 9, 0x0A, 7, 13, 0x0B, 19, 0x0C, 1, 0x0F
    m equ $ - s2
    d resb m
    temp resd 1
    format db "%d", 0
    new_line db 0xA

segment code use32 class=code
    start:
        mov edi, d
        mov esi, s2
        
        mov ecx, m
        CLD 
        repeta:
            lodsb
            mov dl, al      ; DL - el din s2
            mov ebx, esi    ; EBX - S1 POINTER TEMPORARY
            mov [temp], ecx ; TEMP - S1 LEN TEMPORARY
            mov esi, s1     ; ESI - S2 POINTER
            mov ecx, n      ; ECX - S2 LEN
            repeta2:
                lodsb       ; AL - el din s2
                cmp al, dl
                jne not_equal
                
                ; AICI INSEREZ POZITIA PE CARE L-AM GASIT
                
                push dword esi
                push dword format
                call [printf]
                add esp, 8
                
                push dword new_line
                call [printf]
                add esp, 4
                
                push dword esi
                pop edx
                mov al, byte[edx]
                
                stosb
                jmp finish
                
                not_equal:
                cmp ecx, 0
                dec ecx
                jg repeta2
                mov al, 0
                stosb
            finish:
            mov esi, ebx
            mov ecx, [temp]

         loop repeta 

        push dword 0
        call [exit]