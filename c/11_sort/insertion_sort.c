#include <stdio.h>
#include <stdbool.h>

void insertion_sort(int *array, int n) //ascending
{
	int tmp;

	if (n <= 1) return;

	/* Two data part:
	 * 	i : unsorted data part
	 * 	j : sorted data part
	 */
	//for(int i = 1; i < n-1; ++i) //calm: Bug: the last element(array[n-1]) will not to be sorted
	for(int i = 1; i < n; ++i)
	{
		int value = array[i];
		int j = i-1;
			
		for(; j >= 0; --j) //find position to insert data "value"
		{
			if(array[j] > value)
			{
				array[j+1] = array[j]; // move data
			}else{
				break;
			}
		}

		array[j+1] = value; //insert data
	}

	return;
}

/*
EX: 2 3 1 5 4
i == 2
	1)(j == 1) j = i -1 
	  2 3 3 5 4

	2)(j == 0) --j
	  2 2 3 5 4 

	2)(j == -1) --j
	  1 2 3 5 4

EX: 1 3 2 5 4
i == 2
	1)(j == 1) j = i -1 
	  1 3 3 5 4

	2)(j == 0) --j
	  1 2 3 5 4 
*/
int main(void)
{
//	int array[6] = {4,3,5,6,2,1};
	int array[6] = {1,2,3,6,5,4};
	for(int i = 0; i < sizeof(array)/sizeof(int); ++i)
		printf("%d ",array[i]);
	printf("\n");
	
	insertion_sort(array, sizeof(array)/sizeof(int));

	printf("after insertion sort\n");

	for(int i = 0; i < sizeof(array)/sizeof(int); ++i)
		printf("%d ", array[i]);
	printf("\n");
}
