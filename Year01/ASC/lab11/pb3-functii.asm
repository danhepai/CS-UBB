bits 32
segment code use32 class=code public
    global concatenare1
    global concatenare2
    concatenare1:
    mov esi, [esp+4] ;the offset of the source string s1
    mov edi, [esp+12] ;the offset of the destination string s3
    
    mov ecx, [esp + 20] ;len of s1
    
    cld
    
    repeta:
        lodsb
        ; compar al daca ii mai mare ca 48 si mai mic ca 56
        cmp al, 48
        jb my_exit
        cmp al, 56
        ja my_exit
        stosb
        my_exit:
    loop repeta
    
    mov esi, [esp + 8]
    mov ecx, [esp + 16] 
    
    cld 
    
    repeta2:
        lodsb
        ; compar al daca ii mai mare ca 48 si mai mic ca 56
        cmp al, 48
        jb my_exit2
        cmp al, 56
        ja my_exit2
        stosb
        my_exit2:
    loop repeta2
    
    ret 4*5
    
    ;--------------------------------------------------------------------------
    
    concatenare2:
    mov edi, [esp+12] ;the offset of the destination string s3
    mov esi, [esp + 8]
    mov ecx, [esp + 16]
    
    cld 
    
    repeta3:
        lodsb
        ; compar al daca ii mai mare ca 48 si mai mic ca 56
        cmp al, 48
        jb my_exit3
        cmp al, 56
        ja my_exit3
        stosb
        my_exit3:
    loop repeta3
    
    
    mov esi, [esp+4] ;the offset of the source string s1
    mov ecx, [esp + 20] ;len of s1
    
    cld
    
    repeta4:
        lodsb
        ; compar al daca ii mai mare ca 48 si mai mic ca 56
        cmp al, 48
        jb my_exit4
        cmp al, 56
        ja my_exit4
        stosb
        my_exit4:
    loop repeta4
    
    ret 4*5
    
    
            
        
            

    
    