#include <stdio.h>

void print_array(int arr[],int size){
    for(int i =0;i<size;i++){
        printf("%d ",arr[i]);
    }
    printf("\n");
}
void bubble_sort(int arr[],int size){
    int temp;
    for(int i =0;i<size;i++){
        for(int j=i+1;j<size;j++){
            if(arr[j]<arr[i]){
                temp = arr[i];
                arr[i]= arr[j];
                arr[j] =temp;
            }
        }
    }
    print_array(arr,size);

}
void selection_sort(int arr[],int size){
    int small;
    for(int i =0;i<size;i++){
        small = i;
        for(int j = i+1;j<size;j++){
            if(arr[j]<arr[small]){
                small = j;
            }
        }
        if(small!=i){
            int temp = arr[small];
            arr[small] = arr[i];
            arr[i] = temp;
        }
    }
    print_array(arr,size);
}
void insertion_sort(int arr[],int size){
    int j,temp;
    for(int i =1;i<size;i++){
        temp = arr[i];
        j = i-1;
        while(j>=0&&temp<=arr[j]){
            arr[j+1] = arr[j];
            j--;  
        }
        arr[j+1]= temp;
    }
    print_array(arr,size);

}
int main(){
    printf("Enter the size of the array:\n");
    int size;
    scanf("%d",&size);
    int arr[size];
    for(int i  =0 ;i<size;i++){
        scanf("%d",&arr[i]);
    }
    bubble_sort(arr,size);
    selection_sort(arr,size);
    insertion_sort(arr,size);
}
