#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* newString(char* old){
    int count=1;
    int newLength=0;
    const int ascissoffset=48;
    int index=0;
    char current;
    char prev;
    char* tmp=malloc(2);
    char* new=malloc(1);
    new[0]='\0';
    while (old[index]!='\0'){
        index++;
        if (index>0){
            current=old[index];
            prev=old[index-1];
            if (current==prev){
                count++;
            }
            else {
                newLength+=2;
                new=realloc(new,newLength+1);
                tmp[0]=count+ascissoffset;
                tmp[1]='\0';
                strcat(new,tmp);
                tmp[0]=old[index-1];
                tmp[1]='\0';
                strcat(new,tmp);
                count=1;
            }
        }
    }
    return new;
}

void main(void){

    char* nums="1113122113"; // 132113 3113 1113 13 - Conway Sequence
    const int nrepeats=40; // Part 1
    // const int nrepeats=50; // Part 2 - works but takes about an hour

    for (int i=0; i<nrepeats; i++){
        nums=newString(nums);
        printf("%d of %d\n",i,nrepeats);
    }

    printf("\n");
    printf("Solution is %d\n", strlen(nums));
}
