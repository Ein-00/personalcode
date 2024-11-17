#include <stdio.h>
int main(){
	int arr[]={1,2,3,4,5,6};
	int num=6;
	printf("The array before sorting");
	printarray(arr,num);
	printf("The array after sorting");
	bub_sort(arr,num);
	printarray(arr,num);
}
void printarray(int *arr, int n){
	for(int i =0; i<n;i++){
		printf("%d\t",arr[i]);
	}
	printf("\n");
}
void bub_sort(int *arr,int n){
	int issorted;
	for(int i= 0;i<n-1;i++){
		issorted=1;
		for(int j=0;j<n-1-i;j++){
			if(arr[j]>arr[j+1]){
				int temp=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=temp;
				issorted=0;
			}
		}
	}
	if(issorted){
		return;
	}
}
