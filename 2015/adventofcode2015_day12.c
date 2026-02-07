#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int tmpTotal;
    int isRed;
    int isObject;
    int isArray;
} stack;

int main(void){
    FILE *fp;
    char ch;
    char prevch='\0';
    char twoprevch='\0';
    int total=0;
    int sign=1;
    char *filename;
    char number[20]="";
    int openbraces=0;
    int stackIdx=-1;
    int isRed=0;
  
    stack stack[10];
   
    filename="input_day12.txt";
    // filename="example_day12.txt";

    if ( (fp=fopen(filename,"r")) == NULL){
        printf("Cannot open input file");
        return(1);
    }

    do {
        ch=getc(fp);
        if ('{'==ch){
            openbraces++;
            stackIdx++;
            stack[stackIdx].tmpTotal=0;
            stack[stackIdx].isRed=0;
            stack[stackIdx].isObject=1;
            stack[stackIdx].isArray=0;
            
        }
        else if ('['==ch){
            stackIdx++;
            stack[stackIdx].tmpTotal=0;
            stack[stackIdx].isRed=0;
            stack[stackIdx].isObject=0;
            stack[stackIdx].isArray=1;            
        }
        
        // printf("stack idx %d\n",stackIdx);
        if ('d'==ch && 'e'==prevch && 'r'==twoprevch){
            stack[stackIdx].isRed=1;
        }

        if isdigit(ch) {
            if (prevch=='-'){
                sign=-1;
            }
            int l = strlen(number);
            number[l]=ch;
            number[l+1]='\0';
            }
        else {
            total+=atoi(number)*sign;
            stack[stackIdx].tmpTotal+=atoi(number)*sign;
            strcpy(number,"");
            sign=1;
        }

        if ('}'==ch || ']'==ch){
            stackIdx--;
            if (!stack[stackIdx+1].isRed || stack[stackIdx+1].isArray){
                stack[stackIdx].tmpTotal+=stack[stackIdx+1].tmpTotal; 
            }           
        }
        
        twoprevch=prevch;
        prevch=ch;
    } while (ch!=EOF);
    // printf("Number of braces %d\n",openbraces);
    fclose(fp);

    printf("Part 1 is %d\n",total); 
    printf("Part 2 is %d\n",stack[0].tmpTotal); // 13901 is too low, 99395 too high
    return(0);
}
