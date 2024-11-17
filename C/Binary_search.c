#include <stdio.h>


int main(){
	int size;
	int  num;
	printf("Enter the size of the array:\n");
	scanf("%d",&size);
	int ar[size];
	printf("\nEnter the elements of the array:\n");
	for(int i=0;i<size;i++){
		scanf("%d",&ar[i]);
	}
	printf("\nEnter the element to be found:\n");
	scanf("%d",&num);
	
	
	int low=0;
	int high=size-1;
	int mid=size/2;
	while(low<high){
		if(num==ar[mid]){
			printf("The elements has been found in position %d",(mid+1));
			break;
			}
		else if(num>ar[mid]){
			low=mid+1;
			mid=(low+high)/2;
			}
		else{
			high=mid-1;
			mid=(low+high)/2;
			}		
		}
	
	}
