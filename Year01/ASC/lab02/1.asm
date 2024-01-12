bits 32 ;

global start        

extern exit, printf               
import exit msvcrt.dll    
import printf msvcrt.dll

; Exercise: (e + g) * 2 / (a * c) + (h – f) + b * 3, where a,b,c,d-byte, e,f,g,h-word
; print EAX
segment data use32 class=data
    a db 3
    b db 9
    c db 5
    e dw 10
    f dw 15
    g dw 20
    h dw 10
    temp resw 1
    format db "%d", 0


segment code use32 class=code
    start:
        ; e + g -> AX
        mov ax, [e]
        add ax, [g] 
        
        ; (e + g) * 2 -> DX:AX
        mov bx, 2
        imul bx
        
        ; (e + g) * 2 -> CX:BX
        mov cx, dx
        mov bx, ax
        
        ; (a * c) -> AX
        mov al, [a]
        mov ah, [c]
        imul ah
        
        ; temp -> (a*c)
        mov [temp], ax 
        
        ; (e + g) * 2 / (a * c) -> temp
        mov dx, cx
        mov ax, bx
        idiv word [temp]
        mov [temp], ax
        
        ;(h – f) + b * 3
        mov bx, [h]
        sub bx, [f] ; h - f -> BX
        
        mov ah, -7
        mov al, [b]
        imul ah ; b * 3 -> AX
        
        add bx, ax ; BX -> (h – f) + b * 3
        
        ;(e + g) * 2 / (a * c) TEMP  +    (h – f) + b * 3 BX
        
        mov ax, [temp]
        add ax, bx
        
        cwde
        ; REZ FINAL IN EAX
        
        push eax
        push dword format
        call [printf]
        add esp, 4 * 2
        
        

        push    dword 0      
        call    [exit]     
