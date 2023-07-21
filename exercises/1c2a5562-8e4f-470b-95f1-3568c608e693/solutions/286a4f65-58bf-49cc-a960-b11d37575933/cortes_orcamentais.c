#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_V 20005
#define MAX_S
#define INF 1000000009

typedef struct STATE {
  int node, cost;
} STATE;

STATE make_state(int n, int c){
  STATE aux;
  aux.node = n;
  aux.cost = c;
  return aux;
}

typedef struct QUEUE_NODE {
  STATE val;
  struct QUEUE_NODE *next;
} QUEUE_NODE;

typedef struct QUEUE {
  QUEUE_NODE *front, *rear;
  int size;
} QUEUE;
  
void init_queue(QUEUE *q){
  q->front = q->rear = NULL;
  q->size = 0;
}

void add_queue(QUEUE *q, STATE x){
  QUEUE_NODE *temp;
  temp = (QUEUE_NODE *) malloc(sizeof(QUEUE_NODE));
  temp->val = x;
  if(!q->size){
    temp->next = NULL;
    q->front = q->rear = temp;
  }
  else{
    q->rear->next = temp;
    q->rear = temp;
  }
  q->size ++;
}

typedef struct PRIORITY_QUEUE {
  // Min_PQ
  int size;
  STATE heap[MAX_S];
} PRIORITY_QUEUE;

void init_pq(PRIORITY_QUEUE *tpq){
  tpq->size = 0;
}

STATE top_pq(PRIORITY_QUEUE *tpq){
  return tpq->heap[1];
}

void add_pq(PRIORITY_QUEUE *tpq, STATE x){
  tpq->size ++;
  tpq->heap[tpq->size] = x;
  int i = tpq->size;
  while(i > 1){
    if(tpq->heap[i].cost < tpq->heap[(i / 2)].cost){
      STATE aux = tpq->heap[i];
      tpq->heap[i] = tpq->heap[(i / 2)];
      tpq->heap[(i / 2)] = aux;
      i /= 2;
    }
    else
      break;
  }
}

void pop_pq(PRIORITY_QUEUE *tpq){
  tpq->heap[1] = tpq->heap[tpq->size];
  tpq->size --;
  int mson, i = 1;
  while(i * 2 <= tpq->size){
    if(i * 2 + 1 <= tpq->size) mson = (tpq->heap[(i * 2)].cost <= tpq->heap[(i * 2 + 1)].cost) ? (i * 2) : (i * 2 + 1);
    else mson = i * 2;
    if(tpq->heap[i].cost > tpq->heap[mson].cost){
      STATE aux = tpq->heap[i];
      tpq->heap[i] = tpq->heap[mson];
      tpq->heap[mson] = aux;
      i = mson;
    }
    else
      break;
  }
}

int temp_min, temp_max, source, dest, V, E, a, b, t, c, ct, vm, best[MAX_V];
QUEUE *adjList[MAX_V];
PRIORITY_QUEUE *pq;

int main(){
  int i;

  scanf("%d %d %d %d %d %d", &temp_min, &temp_max, &source, &dest, &V, &E);

  source --; dest --;

  for(i = 0; i < V; i ++){
    adjList[i] = (QUEUE *) malloc(sizeof(QUEUE));
    init_queue(adjList[i]);
  }

  for(i = 0; i < E; i ++){
    scanf("%d %d %d %d", &a, &b, &t, &c);
    if(t >= temp_min && t <= temp_max){
      a --; b --;
      add_queue(adjList[a], make_state(b, c));
      add_queue(adjList[b], make_state(a, c));
    }
  }
  
  pq = (PRIORITY_QUEUE *) malloc(sizeof(PRIORITY_QUEUE));
  init_pq(pq);
  add_pq(pq, make_state(source, 0));
  for(i = 0; i < V; i ++)
    best[i] = INF;

  while(pq->size){
    STATE act = top_pq(pq);
    pop_pq(pq);
    if(best[act.node] < INF)
      continue;
    best[act.node] = act.cost;
    if(act.node == dest)
      break;
    QUEUE_NODE *walker;
    for(walker = adjList[act.node]->front; walker != NULL; walker = walker->next)
      if(act.cost + walker->val.cost < best[walker->val.node])
	add_pq(pq, make_state(walker->val.node, act.cost + walker->val.cost));
  }

  scanf("%d", &ct);
  while(ct --){
    scanf("%d", &vm);
    if(best[dest] > vm) printf("Nao\n");
    else printf("Sim\n");
  }
  
  return 0;
}
