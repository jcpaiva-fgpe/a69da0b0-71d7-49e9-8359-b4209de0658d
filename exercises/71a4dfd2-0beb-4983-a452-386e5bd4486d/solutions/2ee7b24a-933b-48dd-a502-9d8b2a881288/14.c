#include <stdio.h>

#define MAX 5001


// Juntar dois arrays ordenados
// Assumir que os arrays sao v[start..middle] e v[middle+1..end]
void merge(int v[], int start, int middle, int end) {
	int i, p1, p2, aux[MAX];

	p1 = start;     // "Apontador" do array da metade esquerda
	p2 = middle + 1;  // "Apontador" do array da metade direita
	i = start;    // "Apontador" do array aux[] a conter juncao
	while (p1 <= middle && p2 <= end) {            // Enquanto de para comparar
		if (v[p1] <= v[p2]) aux[i++] = v[p1++];  // Escolher o menor e adicionar
		else                aux[i++] = v[p2++];
	}
	while (p1 <= middle) aux[i++] = v[p1++];     // Adicionar o que resta
	while (p2 <= end)    aux[i++] = v[p2++];

	for (i = start; i <= end; i++) v[i] = aux[i];  // Copiar array aux[] para v[]
}

// Ordenar array v[] com mergesort entre posicoes start e end
void mergesort(int v[], int start, int end) {
	int middle;
	if (start<end) {                 // Parar quando tamanho do array < 2
		middle = (start + end) / 2;        // Calcular ponto medio
		mergesort(v, start, middle);   // Ordenar metade esquerda
		mergesort(v, middle + 1, end);   // Ordenar metade direita
		merge(v, start, middle, end);  // Combinar duas metades ordenadas
	}
}

int main()
{

	int S, C;
	scanf("%d", &S);
	scanf("%d", &C);

	int i, j;
	int peso[MAX];
	int somas[C + 1];

	for (i = 0; i<S; i++) scanf("%d", &peso[i]);
	for (i = 0; i <= C; i++)  somas[i] = 0;

	mergesort(peso, 0, S - 1);

	somas[0] = 1;

	for (i = 0; i<S; i++)
		for (j = C; j >= peso[i]; j--)
			if (somas[j - peso[i]] == 1)
				somas[j] = 1;

	for (i = C; i >= 0; i--)
		if (somas[i] == 1)
		{
			printf("%d\n", i);
			return 0;
		}



	return 0;
}

//feito com andre meira