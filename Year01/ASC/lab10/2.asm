bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
                          ; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
                          
extern fscanf, printf, fread, fopen
import fscanf msvcrt.dll
import printf msvcrt.dll
import fread msvcrt.dll
import fopen msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    read_file db "readfile.txt", 0
    my_string resb 40
    print_message db "Special chars appeared: %d times", 0
    access_mode_file db "r", 0
    descriptor dd -1
    counter dd 0
    lungime db 0
    

; our code starts here
segment code use32 class=code
    start:
        push dword access_mode_file
        push dword read_file
        call [fopen]
        add esp, 4*2
        
        mov [descriptor], eax
        cmp eax, 0
        je final
               
        push dword my_string
        push dword [descriptor]
        call [fread]
        mov [lungime], eax
        add esp, 4*2
        
        ;parcurg sirul si sa numar caracterele speciale
        
        CLD
        mov ecx, eax
        
        repeta:
            lodsb ; in al am caracterul
            ; caracterele speciale au val 33-47 in ascii
            
            cmp al, 33
            ja mai_mare_ca_33
            jb mai_mic_ca_33
            
            mai_mare_ca_33:
                cmp al, 47
                jb mai_mic_ca_47
                ja mai_mic_ca_33
                
                mai_mic_ca_47:
                    mov edx, [counter]
                    add edx, 1
                    mov [counter], edx
                    
                    
             mai_mic_ca_33:
                nop
        loop repeta
        
        push dword[counter]
        push dword print_message
        call [printf]
        add esp, 4 * 2
        
        final:
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
