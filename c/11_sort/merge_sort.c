#include <stdio.h>
#include <stdbool.h>

void merge_sort(int *array, int n);
void merge_sort_c(int *array, int p, int r);
void merge(int *arr, int p, int q, int r);


void merge_sort(int *array, int n) //ascending
{
	merge_sort_c(array, 0, n-1);
}

void merge_sort_c(int *arr, int p, int r)
{
	int q;

	//Recursive termination condition
	if(p >= r) return;

	//q = (p+r)/2; // p+r maybe out of int range
	q = p + (r-p)/2;

	merge_sort_c(arr, p, q);
	merge_sort_c(arr, q+1, r);

	merge(arr, p, q, r);
}

void merge(int *arr, int p, int q, int r)
{
	int i = p;
	int j = q+1;
	int k = 0;
	int n = 0;
	int tmp[n]; // alloc a temporary array of the same size as arr[p...r]

	n = r-p+1;
	tmp[n] = 0;
	while(i<=q && j<=r){// 'while' is a better thought!
		if(arr[i] <= arr[j]){
			tmp[k++] = arr[i++];
		}else{
			tmp[k++] = arr[j++];
		}
	}
	/*
	for(i = 0; i < p; i++)
	{
		for(j = q; j < r; j++)
		{
			if(arr[i] >= arr[j])
			{
				tmp[k++] = arr[j++];
			}else{
				tmp[k++] = arr[i++];
			}
		}
	}*/

	// determine which subarray has the remaining data
	int start = i;
	int end = q;
	if(j<=r){
		start = j;
		end = r;
	}

	// copy the remaining data to the temporary array tmp
	while(start <= end){
		tmp[k++] = arr[start++];
	}

	// copy the data from the array tmp back to a[p...r]
	for(k=0; k <= r-p; k++){
		//arr[k] = tmp[k];
		arr[p+k] = tmp[k];
	}
		
}

int main(void)
{
	int array[6] = {4,3,5,6,2,1};
//	int array[6] = {1,2,3,6,5,4};
	for(int i = 0; i < sizeof(array)/sizeof(int); ++i)
		printf("%d ",array[i]);
	printf("\n");
	
	merge_sort(array, sizeof(array)/sizeof(int));

	printf("after merge sort\n");

	for(int i = 0; i < sizeof(array)/sizeof(int); ++i)
		printf("%d ", array[i]);
	printf("\n");
}
