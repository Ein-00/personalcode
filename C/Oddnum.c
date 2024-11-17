#include <stdio.h>

int main(){
	int num1,num2;
	printf("Enter 2 numbers:\n");
	scanf("%d%d",&num1,&num2);
	if((num1%2)==0){
		num1++;
	}
	while(num1<num2){
		
		printf("\n%d",num1);
		num1+=2;
	}
}