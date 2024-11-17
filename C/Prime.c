#include <stdio.h>
#include <Stdbool.h>


int main(){
	int num;
	printf("Enter a number:\n");
	scanf("%d",&num);
	bool flag = false;
	int i= 2;
	while(i<num){
		if((num%i)==0){
			flag=true;
		}
		i++;
	}
	if(flag){
		printf("\nThe number is not a prime number.");
	}
	else{
		printf("\nThe number is a prime number.");
	}
	

}