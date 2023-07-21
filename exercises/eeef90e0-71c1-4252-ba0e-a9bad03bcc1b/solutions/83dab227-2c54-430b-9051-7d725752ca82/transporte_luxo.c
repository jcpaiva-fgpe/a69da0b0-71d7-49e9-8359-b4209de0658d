#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INF 1000000007
#define MAX_V 20005

typedef struct STATE{
  int node, cost;
} STATE;

typedef struct QUEUE{
  STATE val;
  struct QUEUE *next;
} QUEUE;

STATE aux;
int szQueue;
QUEUE *front, *rear;
int temp_min, temp_max, orig, dest;
int a, b, t, qttVerts, qttEdges;
int nconn[MAX_V], adjList[MAX_V][MAX_V], dist[MAX_V];

void init_queue(){
  szQueue = 0;
  front = rear = NULL;
}

void insert_queue(STATE x){
  QUEUE *temp;
  temp = (QUEUE *) malloc(sizeof(QUEUE));
  temp->val = x;
  if(!szQueue){
    temp->next = NULL;
    front = rear = temp;
  }
  else{
    rear->next = temp;
    rear = temp;
  }
  szQueue ++;
}

STATE front_queue(){
  return front->val;
}

void pop_queue(){
  front = front->next;
  szQueue --;
  if(!szQueue)
    rear = NULL;
}

int main(){
  int i;

  scanf("%d %d %d %d %d %d", &temp_min, &temp_max, &orig, &dest, &qttVerts, &qttEdges);

  orig --; dest --;
  memset(nconn, 0, sizeof(nconn));

  for(i = 0; i < qttEdges; i ++){
    scanf("%d %d %d %*d", &a, &b, &t);
    if(t >= temp_min && t <= temp_max){
      a --; b --;
      adjList[a][nconn[a] ++] = b;
      adjList[b][nconn[b] ++] = a;
    }
  }
 
  for(i = 0; i < qttVerts; i ++)
    dist[i] = INF;
  init_queue();
  aux.node = orig;
  aux.cost = 0;
  insert_queue(aux);

  while(szQueue){
    aux = front_queue();
    pop_queue();
    if(dist[aux.node] != INF)
      continue;
    dist[aux.node] = aux.cost;
    if(aux.node == dest)
      break;
    STATE ns = aux;
    ns.cost ++;
    for(i = 0; i < nconn[aux.node]; i ++){
      ns.node = adjList[aux.node][i];
      insert_queue(ns);
    }
  }

  if(dist[dest] == INF) printf("Nao\n");
  else printf("Sim %d\n", dist[dest]);

  return 0;
}
