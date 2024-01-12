bits 32

global start

extern exit
import exit msvcrt.dll

;problem to solve:
; Se dau doua cuvinte A si B. Sa se obtina dublucuvantul C:
; bitii 0-4 ai lui C au valoarea 1
; bitii 5-11 ai lui C coincid cu bitii 0-6 ai lui A
; bitii 16-31 ai lui C au valoarea 0000000001100101b
; bitii 12-15 ai lui C coincid cu bitii 8-11 ai lui B


segment data use32 class=data
    a dw 0FFFFh
    b dw 0FFFFh
    c dd 0

segment code use32 class=code
    start:

    mov ax, [a] ; ax = a(15)...a(0)
    SHL ax, 5 ; ax = a(11)...a(0)0000
    and ax, 0000111111100000b ; ax =00000a(6)a(5)..a(0)0000
    movzx eax, ax ; eax = 00000000000000000000a(6)a(5)..a(0)00000

    or dword[c], eax ; in c biti 5-11 coincid cu bitii 0-6 a lui a

    or dword[c], 0000001Fh ; in c biti 5-11 coincid cu bitii 0-6 a lui A, iar primii 5 biti is 1

    mov bx, [b]
    or bx, 0F00h ; in bx am biti 8-11 lui b
    movzx ebx, bx ; in ebx am biti 8-11 lui b
    SHL ebx, 4 ; in ebx pe pozitiile 12-15 am biti 8-11 a lui b, in ret 0

    or dword[c], ebx ; bitii 0-11 si 16-31 isi pastreaza valoarea,
                     ; iar bitii 12-15 iau valoarea bitilor 8-11 a lui b

    mov bx, 0065h ; in bx se afla valoarea 0065h
    movzx ebx, bx ; in ebx se afla valoarea 00000065h

    SHL ebx, 16 ; in ebx se afla valoarea 00650000h

    or dword[c], ebx ; in C am pastrat toti bitii inafara de bitii 16-31 care au luat valoarea 0065h

    ; in final C arata asa:
    ; 0000.0000.0110.0101.b(11)b(10)b(9)b(8).a(6)a(5)a(4)a(3).a(2)a(1)a(0)1.1111

    ;in caz ca b = FFFFh si a = FFFFh =>
    ; c = 0065FFFF1h

    mov eax, [c]

    push dword 0
    call [exit]