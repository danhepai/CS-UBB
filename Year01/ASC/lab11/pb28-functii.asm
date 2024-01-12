bits 32
segment code use32 class=code public
    global concatenare1
    global concatenare2
    concatenare1:
    mov esi, [esp+4] ;the offset of the source string s1
    mov edi, [esp+8] ;the offset of the destination string s2
    
    mov ecx, [esp + 12] ;len of s1
    
    cld
    
    repeta:
        lodsb
        ; compar al daca ii mai mare ca 48 si mai mic ca 56
        cmp al, 97
        jb my_exit
        cmp al, 122
        ja my_exit
        stosb
        my_exit:
    loop repeta
    
    ret 4*3
    
    ;--------------------------------------------------------------------------
    
    concatenare2:
    mov esi, [esp+4] ;the offset of the source string s1
    mov edi, [esp+8] ;the offset of the destination string s2
    
    mov ecx, [esp + 12] ;len of s1
    
    cld 
    
    repeta2:
        lodsb
        ; compar al daca ii mai mare ca 48 si mai mic ca 56
        cmp al, 65
        jb my_exit2
        cmp al, 90
        ja my_exit2
        stosb
        my_exit2:
    loop repeta2
    
    ret 4*3
    
    
            
        
            

    
    