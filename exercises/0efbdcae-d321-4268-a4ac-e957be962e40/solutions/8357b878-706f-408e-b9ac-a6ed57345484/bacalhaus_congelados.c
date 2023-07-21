#include <stdio.h>
#include <stdlib.h>

#define MIN(a, b) (a < b ? a : b)
#define MAX(a, b) (a > b ? a : b)

#define INF 1000000007
#define MAX_V 20005

int i, a, b, t, qttVerts, qttEdges, adjMatrix[MAX_V][MAX_V];
int tam, act, next, temp_min, temp_max;

int main(){

  scanf("%d %d", &qttVerts, &qttEdges);
  for(i = 0; i < qttEdges; i ++){
    scanf("%d %d %d %*d", &a, &b, &t);
    adjMatrix[a][b] = adjMatrix[b][a] = t;
  }

  while(1){
    scanf("%d", &tam);
    if(!tam) break;
    temp_min = INF;
    temp_max = -INF;
    scanf("%d", &act);
    for(i = 1; i < tam; i ++){
      scanf("%d", &next);
      temp_min = MIN(temp_min, adjMatrix[act][next]);
      temp_max = MAX(temp_max, adjMatrix[act][next]);
      act = next;
    }
    printf("%d %d\n", temp_min, temp_max);
  }

  return 0;
}
