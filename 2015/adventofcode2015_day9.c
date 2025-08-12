#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <stdbool.h>

// Traveling salesman problem

#define nmax 20

void printCities(char **);

int isInArray(char** testArray, char *test){
    for (int i=0; i<nmax; i++){
        if (!testArray[i]) break;
        if (strcmp(testArray[i],test)==0) return i;
    }
    return -1;
}

int findArraySize(char** testArray){
    for (int i=0; i<nmax; i++){
        if (!testArray[i]) return i;
    }
    return -1;
}

void addToCityArray(char **Array, char *toAdd){
    int n=findArraySize(Array);
    Array[n]=malloc((nmax+1)*sizeof(char));
    strcpy(Array[n],toAdd);
}

void addToDistanceArray(int Array[][nmax], int d, int i, int j){
    if (i>=0 && j>=0){
        Array[i][j]=d;
        Array[j][i]=d;
    }
}

void printCities(char **Array){
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
    int distances[nmax][nmax];
    int distance=0;
    int startidx,endidx;
    int ncities;

    for (int i=0;i<nmax;i++) {cities[i]=NULL;}
    for (int i=0;i<nmax;i++) {
        for (int j=0;j<nmax;j++) {
            distances[i][j]=0;
        }
    }


    if ((fp=fopen(input_file, "r"))==NULL){
        printf("Cannot open file\n");
        return 1;
    }

    while (fscanf(fp,"%49s to %49s = %d",start,end,&distance)!=EOF){
        //printf("%s %s %d\n",start,end,distance);
        startidx=isInArray(cities,start);
        //printf("statidx %d\n", startidx);
        if (startidx==-1) addToCityArray(cities,start);
        endidx=isInArray(cities,end);
        // printf("endidx %d\n", endidx);
        if (endidx==-1) addToCityArray(cities,end);

        startidx=isInArray(cities,start);
        endidx=isInArray(cities,end);

        if (startidx!=-1 && endidx!=-1) addToDistanceArray(distances,distance,startidx,endidx);       
    }

    ncities=findArraySize(cities);
    if (ncities!=-1){
        for (int i=0;i<ncities;i++){
            if (!cities[i])   break;
            printf("%d %s\n", i,cities[i]); 
        }


        for (int i=0; i<ncities; i++){
            for (int j=0; j<ncities; j++){
                printf("%d, %d, %d\n", i, j, distances[i][j]);
            }
        }
    }
                    
    fclose(fp);
    return 0;
}