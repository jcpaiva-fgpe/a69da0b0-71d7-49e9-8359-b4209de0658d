#include <stdio.h>
#include <stdlib.h>  /* for qsort */
#include <string.h>  /* for strlen */
#include <strings.h> /* for strcasecmp */
 
#define MAX 20000
#define MAX_LEN 35

typedef struct {
  char nome[MAX_LEN];
  char apelido[MAX_LEN];
  int nota;
} Aluno;

int mycmp2(const void *s1, const void *s2){
  int aux;
  Aluno *p1 = (Aluno *)s1;
  Aluno *p2 = (Aluno *)s2;
  if(p1->nota < p2->nota){ return +1;}
  if(p1->nota > p2->nota){ return -1;}
  else{
    aux =  strcmp(p1->nome, p2->nome);
    if(aux!=0){
      return aux;
    }
    else{
      return strcmp(p1->apelido, p2->apelido);
    }
  } 
}


int mycmp(const void *s1, const void *s2){
  Aluno  *p1 = (Aluno *)s1;
  Aluno  *p2 = (Aluno *)s2;

  //if ( p1->tamanho < p2->tamanho) return -1;
  //if ( p1->tamanho > p2->tamanho) return +1;
  return strcmp(p1->nome, p2->nome);

}

int main(){
  int n, i, k, tipo;
  Aluno strings[MAX];

  scanf("%d\n", &tipo);
  scanf("%d\n", &n);
  
  for(i=0;i<n; i++){
    scanf("%s", strings[i].nome);
    scanf("%s", strings[i].apelido);
    scanf("%d", &strings[i].nota);
    //strings[i].tamanho = strlen(strings[i].nome);
  }
  
  if(tipo==1){
    qsort(strings, n, sizeof(Aluno), mycmp2);
  }   
  else if(tipo==2){
    qsort(strings, n, sizeof(Aluno), mycmp);
  }
  
  for(k=0;k<n;k++){
    printf("%s %s %d\n", strings[k].nome, strings[k].apelido, strings[k].nota);
  }
  
  return 0;


}
