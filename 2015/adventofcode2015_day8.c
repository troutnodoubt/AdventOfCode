#include <stdio.h>

int main(void){
    FILE *fp;
    char ch;
    char prev_ch;
    int ndq=0;
    int nescape=0;
    int escaped=0;
    int newliteral=0;
    char *filename;

    filename="input_day8.txt";
    // filename="example_day8.txt";

    if ( (fp=fopen(filename,"r")) == NULL){
        printf("Cannot open input file");
        return(1);
    }

    do {
        ch=getc(fp);
        if ((ch=='\\') || (ch=='\"')) newliteral++;
        if ((!escaped) && (prev_ch=='\\')){
            escaped=1;
            if ((ch=='\\') || (ch=='\"')) nescape++;
            else if (ch=='x') nescape+=3;
        }
        else {
            escaped=0;
            if (ch=='\"') ndq++;
        }
        prev_ch=ch;
    } while (ch!=EOF);

    fclose(fp);

    printf("Part 1 is %d\n",nescape+ndq); 
    printf("Part 2 is %d\n", ndq+newliteral);
    return(0);
}
