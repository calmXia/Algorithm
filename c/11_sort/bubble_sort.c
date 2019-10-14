
#include <stdio.h>
#include <stdbool.h>

void bubble_sort(int *array, int n) //ascending
{
	int tmp;
	bool swap_flag = false; // data swap or not
	
	if (n <= 1) return;
	
	for(int i = 0; i < n; ++i)
	{
		swap_flag = false;

		//for(int j = 0; j < n; ++j)   //calm: Bug: last one array[n-1] will be swap to 0(array[n])
		//for(int j = 0; j < n-1; ++j) //calm: optimize
		for(int j = 0; j < n-i-1; ++j)
		{
			if(array[j] > array[j+1])
			{
				tmp = array[j+1];
				array[j+1] = array[j];
				array[j] = tmp;

				swap_flag = true;
			}
		}

		if(swap_flag == false)
			break;
	}

	return;
}

int main(void)
{
	int array[6] = {4,3,5,6,2,1};
//	int array[6] = {1,2,3,6,5,4};
	for(int i = 0; i < sizeof(array)/sizeof(int); ++i)
		printf("%d ",array[i]);
	printf("\n");
  
	bubble_sort(array, sizeof(array)/sizeof(int));
	
  printf("after bubble sort\n");
	
  for(int i = 0; i < sizeof(array)/sizeof(int); ++i)
		printf("%d ", array[i]);
	printf("\n");

  return 0;
}
