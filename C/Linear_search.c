#include <stdio.h>


int main()
{
	int size;
	printf("Enter the size of the array:\n");
	scanf("%d",&size);
	int ar[size];
	printf("\nEnter the elements of the array:\n");
	for(int i=0;i<size;i++){
		scanf("%d",&ar[i]);
	}
	printf("\nEnter the element to be found:\n");
	int num;
	int flag=0;
	scanf("%d",&num);
	for(int i=0;i<size;i++){
		if(ar[i]==num){
			printf("\nThe element has been found in position %d",(i+1));
			flag=1;
			break;
			}
		}
	if(flag==0){
		printf("The element is not present in the array.");
	}
	printf("\nThe End");
	
	
    
}
