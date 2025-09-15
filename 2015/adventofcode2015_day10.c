#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int newString(char* oldString, char* newString, int length){
    int count=1;
    int lenNextString=0;
    const int asciioffset=48;
    char currentChar=oldString[0];
    char nextChar = '\0';
    printf("lenght %d\n",length);
    if (1 == length){
        newString[0]=length+asciioffset;
        newString[1]=currentChar;
        lenNextString+=2;
    }
    else {    
        for (int i=1; i<length; i++){
            nextChar=oldString[i];
            printf("current char %c nextChar %c\n",currentChar,nextChar);
            if (nextChar != '1' || nextChar != '2' || nextChar != '3' ||
                nextChar != '4' || nextChar != '5' || nextChar != '6' ||
                nextChar != '7' || nextChar != '8' || nextChar != '9')
                {
                    printf("Invalid character\n");
                    break;
                }
            if (nextChar == currentChar){
                count++;
            }
            else {
                //retString[lenNextString]=malloc(sizeof(char));
                //retString[lenNextString+1]=malloc(sizeof(char));

                newString[lenNextString]=count+asciioffset;            
                newString[lenNextString+1]=currentChar;

                currentChar=nextChar;
                lenNextString+=2;
            }
        }
    }
    return lenNextString;
} 

int main(void){
    
    char input[] = {'1'};
    char nextString[] = {'\0'};
    const char nullString[] = {'\0'};
    int length = 1;
    int nextLength = 0;
    int ncycles=2;

    for (int nrepeats=0; nrepeats<ncycles; nrepeats++)
    {
        printf("repeat count %d of %d\n",nrepeats,ncycles);
        nextLength = newString(input, nextString, length);

        for (int i=0; i<length; i++) {printf("%c", input[i]);}
        printf("\n");
        printf("Length of current %d", length);
        printf("\n");
        for (int i=0; i<nextLength; i++) {printf("%c", nextString[i]);}
        printf("\n");
        printf("Length of next %d", nextLength);
        printf("\n");

        length=nextLength;
        memcpy(input, nextString, length);
        memcpy(nextString, nullString, 1);
    }



    
   
    
    return 0;
}