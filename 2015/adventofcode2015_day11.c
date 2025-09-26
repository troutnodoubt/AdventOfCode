#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool threeAscending(char* pw){
    int idx=0;
    bool found=false;
    int nfound=0;

    while (pw[idx]!='\0'){
        if (idx>=2){
            if (pw[idx]-pw[idx-1]==1 && pw[idx-1]-pw[idx-2]==1){
                if (!found) {nfound=1;}
                else {nfound++;}
            }
            else {
                if (nfound==1) {found=true;}
            }
        }
        idx++;
    }
    return nfound==1;
}

bool illegalCharacters(char* pw){
    int idx=0;

    while (pw[idx]!='\0'){
        if ( pw[idx]=='i'||pw[idx]=='l'||pw[idx]=='o'){
            return true;
        }
        idx++;
    }
    return false;
}

bool hasTwoRepeats(char* pw){
    int idx=0;
    char tmp='\0';
    while (pw[idx]!='\0'){
        if (idx>=1){
            if (pw[idx]==pw[idx-1]){
                if (tmp=='\0') {tmp=pw[idx];} // first match found
                else if (pw[idx]!=tmp) {return true;} //second match found
            }
        }
        idx++;
    }
    return false;
}

bool isValid(char *pw){
    return (threeAscending(pw) && !illegalCharacters(pw) && hasTwoRepeats(pw));
}

void incrementPW(char* pw){
    int len=strlen(pw);
    for (int i=len-1; i>=0; i--){
        if (pw[i]!='z'){
            pw[i]+=1;
            break;
        }
        else {
            pw[i]='a';
        }
    }
}

void main(void){
    //char input[10]="vzbxkghb"; // Part 1 solution is vzbxxyzz
    char input [10]="vzbxxyzz"; // Part 2 is part 1 output, solution is vzcaabcc

    if (isValid(input)){
        incrementPW(input);
    }
    while (!isValid(input)){
        incrementPW(input);
        //printf("%s %s\n",input,isValid(input)?"True":"False");
    }

    printf("Solution is %s\n",input);
}
