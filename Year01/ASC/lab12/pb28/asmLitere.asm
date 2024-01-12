bits 32 

global _litereMici
global _litereMari

segment data public data use32

segment code public code use32

_litereMici:
    ; Codul de intrare
	push ebp
	mov ebp, esp

    mov esi, [esp+8] ;the offset of the source string s
    mov edi, [esp+16] ;the offset of the destination string rez
    
    mov ecx, [esp + 12] ;len of s
    
    cld
    
    repeta:
        lodsb
        ; compar al daca ii mai mare ca 48 si mai mic ca 56
        cmp al, 96
        jb my_exit
        cmp al, 123
        ja my_exit
        stosb
        my_exit:
    loop repeta
    

    ; Codul de iesire
	mov esp, ebp
	pop ebp
    
    ret


_litereMari:
    ; Codul de intrare
	push ebp
	mov ebp, esp
    
    mov esi, [esp+8] ;the offset of the source string s
    mov edi, [esp+16] ;the offset of the destination string rez
    
    mov ecx, [esp + 12] ;len of s
    
    cld
    
    repeta2:
        lodsb
        ; compar al daca ii mai mare ca 48 si mai mic ca 56
        cmp al, 64
        jb my_exit2
        cmp al, 91
        ja my_exit2
        stosb
        my_exit2:
    loop repeta2

    ; Codul de iesire
	mov esp, ebp
	pop ebp
    
    ret    
