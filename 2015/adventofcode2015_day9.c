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
    char start[50];
    char end[50];
    int distances[nmax*nmax];
    int distance=0;
    int startidx,endidx;

    for (int i=0;i<nmax;i++) {cities[i]=NULL;}
    for (int i=0;i<(nmax*nmax);i++) {distances[i]=0;}

    if ((fp=fopen(input_file, "r"))==NULL){
        printf("Cannot open file\n");
        return 1;
    }

    while (fscanf(fp,"%49s to %49s = %d",start,end,&distance)!=EOF){
        printf("%s %s %d\n",start,end,distance);
        startidx=isInArray(cities,start,nmax);
        printf("statidx %d\n", startidx);
        if (startidx==-1) printf("add start"),addToCityArray(cities,start,nmax);
        endidx=isInArray(cities,end,  nmax);
        printf("endidx %d\n", endidx);
        if (endidx==-1) printf("add end"),addToCityArray(cities,end,nmax);

        startidx=isInArray(cities,start,nmax);
        endidx=isInArray(cities,end,nmax);

        if (startidx!=-1 && endidx!=-1) addToDistanceArray(distances,distance,startidx,endidx,nmax);

        
        
    }
     
    for (int i=0;i<nmax;i++){
                if (!cities[i])   break;
                printf("%d %s\n", i,cities[i]); 
                    }


    for (int i=0; i<nmax; i++){
        for (int j=0; j<nmax; j++){
            printf("%d, %d, %d\n", i, j, distances[i*nmax+j]);
        }
    }
                    
    fclose(fp);
    return 0;
}