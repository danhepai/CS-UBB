bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
                          extern fopen, printf, fclose, gets, scanf
                          import fopen msvcrt.dll
                          import printf msvcrt.dll
                          import gets msvcrt.dll
                          import fclose msvcrt.dll
                          import scanf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    fisier db "caracterespeciale.txt", 0
    access_mode db "r", 0
    descriptor dd -1
    formatdecimal db "%d", 0
    text_pentru_print db "numarul caracterelor speciale este %d", 0
    count dd 0
    text_citit resb 20
    lungime_sir dd 0

; our code starts here
segment code use32 class=code
    start:
        push dword access_mode
        push dword fisier
        call [fopen]
        add esp, 4 * 2
        mov [descriptor], eax
        
        ;cmp eax, 0
        ;je final
        
        push dword text_citit
        push dword [descriptor]
        call [scanf]
        add esp, 4 * 2
        mov [lungime_sir], eax ;lungimea sir
        mov ecx, [lungime_sir]
        
        CLD
        mov esi, text_citit 
        repeta:
        
            lodsb 
            cmp al, 33
            ja mai_mare_ca_33
            jb afara_din_interval
        
            mai_mare_ca_33:
                cmp al, 47
                jb mai_mic_ca_47
                ja afara_din_interval
                
                mai_mic_ca_47:
                    mov edx, [count]
                    add edx, 1
                    mov [count], edx
                    
         afara_din_interval:
         loop repeta
         
        push dword[count]
        push dword text_pentru_print
        call [printf]
        add esp, 4 * 2
        
        push dword [descriptor]
        call [fclose]
        add esp, 4
            
    
        ;final:
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
