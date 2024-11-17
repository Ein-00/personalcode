#include <stdio.h>
void linear_search(int arr[],int size){
    int ele;
    printf("Enter the element to be found:\n");
    scanf("%d",&ele);
    for(int i = 0 ;i<size;i++){
        if(arr[i]==ele){
            printf("The element was found at position %d.\n",i+1);
            return ;
        }
    }
    printf("Element not present in array.\n");
    return ;
}
void binary_search(int arr[],int size){
    int ele;
    scanf("%d",&ele);
    int low =0;
    int high = size-1;
    int mid = high/2;
    while(low<=high){
        mid = low+high/2;
        if(arr[mid]==ele){
            printf("Element found at position %d.",mid+1);
            return ;
        }
        else if(arr[mid]<ele){
            low = mid+1;

        }
        else{
            high  = mid-1;
        }
    }
}



int main(){
	printf("Enter the size of the array:\n");
    int size;
    scanf("%d",&size);
    int arr[size];
    printf("Enter the elements:\n");
    for(int i = 0 ;i<size;i++){
        scanf("%d",&arr[i]);
    }
    linear_search(arr,size);
    binary_search(arr,size);
    

}
