#include <stdio.h>


int main(){
	int num;
	printf("Enter a number:");
	scanf("%d",&num);
	int fact=1;
	while(num>1){
		fact*=num;
		num--;
	}
	
	printf("The factorial is :%d",fact);
	
}

