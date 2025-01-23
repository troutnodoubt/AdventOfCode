#include <stdio.h>

int main(void){
    FILE *fp;
    char ch;
    char prev_ch;
    int ndq=0;
    int nescape=0;

    if ( (fp=fopen("input_day8.txt","r")) == NULL){
        printf("Cannot open input file");
        return(1);
    }

    do {
        ch=getc(fp);
        if (prev_ch=='\\'){
            if ((ch=='\\') || (ch=='\"')){
                nescape++;
            }
            else if (ch=='x'){
                nescape+=3;
            }
       }
       else if ((prev_ch!='\\') && (ch=='\"')){
        ndq++;
       }
       prev_ch=ch;
    } while (ch!=EOF);
    printf("%d %d\n", nescape, ndq);
    printf("Part 1 is %d\n",nescape+ndq); // 1379 is too high. Many lines ending with \\", which will double escape. Need to handle that kind of case.
    return(0);
}