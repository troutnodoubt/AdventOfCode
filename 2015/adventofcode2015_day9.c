#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void printCities(char **, int);

int isInArray(char** testArray, char *test, int nmax){
    for (int i=0; i<nmax; i++){
        if (!testArray[i]) break;
        if (strcmp(testArray[i],test)==0) return i;
    }
    return -1;
}

int findArraySize(char** testArray, int nmax){
    for (int i=0; i<nmax; i++){
        if (!testArray[i]) return i;
    }
    return -1;
}

void addToCityArray(char **Array, char *toAdd, int nmax){
    int n=findArraySize(Array, nmax);
    Array[n]=malloc((nmax+1)*sizeof(char));
    if (n>0) strcpy(Array[n],toAdd);
}

void addToDistanceArray(int *Array, int d, int i, int j, int nmax){
    if (i>=0 && j>=0){
        Array[nmax*i+j]=d;
        Array[nmax*j+i]=d;
    }
}

void printCities(char **Array, int nmax){
    printf("\n*****\n");
    for (int i=0; i<nmax; i++){
        if (!Array[i]) break;
        printf("%d %s\n",i,Array[i]);        
    }
    printf("\n*****\n\n");
}

int main(void){
    #define nmax 20
    FILE *fp;
    // char *input_file="C:\\Users\\truta\\Documents\\git\\AdventOfCode\\2015\\example_day9.txt";
    char *input_file="example_day9.txt";
    char *cities[nmax];
    char *source[50];
    char *destination[50];
    int distance=0;
    int startidx,endidx;
    
    if ((fp=fopen(input_file, "r"))==NULL){
        printf("Cannot open file\n");
        return 1;
    }

    while (fscanf(fp,"%s to %s = %d",source,destination,&distance)!=EOF){
        printf("%s %s %d\n",source,destination,distance);
        startidx=isInArray(cities,source,nmax);
        printf("statidx %d\n", startidx);
        if (startidx==-1) printf("add start"),addToCityArray(cities,source,nmax);
        endidx=isInArray(cities,destination,  nmax);
        printf("endidx %d\n", endidx);
        if (endidx==-1) printf("add end"),addToCityArray(cities,destination,nmax);
        
        
    }
     
    for (int i=0;i<nmax;i++){
                if (!cities[i])   break;
                printf("%d %s\n", i,cities[i]); 
                    }
                    
    fclose(fp);
    return 0;
}