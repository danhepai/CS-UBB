bits 32 

global _asmConcatenare

extern _printf

segment data public data use32
    
segment code public code use32

_asmConcatenare:
    ; Codul de intrare
	push ebp
	mov ebp, esp
    
    mov esi, [ebp + 8]       ; s1
    mov ecx, [ebp + 12]      ; len s1
    mov edi, [ebp + 24]      ; rez

    cld
    repeta:
        lodsb
        ; compar al daca ii mai mare ca 48 si mai mic ca 56
        cmp al, '0'
        jb my_exit
        cmp al, '9'
        ja my_exit
        stosb
        my_exit:
    loop repeta
    
    mov esi, [ebp + 16]      ; s2
    mov ecx, [ebp + 20]      ; len s2
    
    
    cld
    repeta2:
        lodsb
        ; compar al daca ii mai mare ca 48 si mai mic ca 56
        cmp al, '0'
        jb my_exit2
        cmp al, '9'
        ja my_exit2
        stosb
        my_exit2:
    loop repeta2
    
    

    ; Codul de iesire
	mov esp, ebp
	pop ebp
    
    ret

        
        
    
        
        