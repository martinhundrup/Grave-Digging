#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

struct person{
  int born;
  int death;
  int age;
};

int main(){

  FILE* file = fopen("dates.txt", "r");
  char buffer[100] = {0};
  struct person people[4500] = {0};
  struct person invalids[100] = {0};

  int i = 0; // line number
  int j = 0; // valid person idx
  int k = 0; // invalid person idx
  while (!feof(file)){
    fgets(buffer, 99, file);

    // the buffer is a single person now
    buffer[strlen(buffer) - 2] = '\0';
    char* s = buffer + 1;

    struct person p = {0};

    // s is now the dates without the quotes
    // strtok s until end of the line
    char* s1 = strtok(s, " "); // use space as delim
    int counter = 0;
    while (s1 != NULL){
      int res = atoi(s1);
      if (res > 1000){ // valid year
        counter++;
        if (counter == 1)
          p.born = res;
        else p.death = res;

      }
      s1 = strtok(NULL, " ");
    }
    
    if (counter < 2){ // missing year(s)
      invalids[k++] = p;
    }
    else{      
      p.age = p.death - p.born;
      people[j++] = p;
    }
    i++;
  }
    
  printf("\nvalid people: %d\n", j);
  printf("invalid people: %d\n", k);

  FILE* outfile = fopen("data.txt", "w");
  fprintf(outfile,"born, died, age\n");

  float avg_age = 0;

  for (int x = 0; x < j; x++){ // output valid dates to file
    fprintf(outfile, "%d,%d,%d\n", people[x].born, people[x].death, people[x].age);
    avg_age += people[x].age;
  }
  fprintf(outfile, "average age: %f\n", avg_age / j);
  fprintf(stdout, "average age: %f\n", avg_age / j);  

  

  fclose(outfile);
  fclose(file);
  return 0;
}