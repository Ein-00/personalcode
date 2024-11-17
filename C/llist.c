#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
typedef struct node {
  int info;
  struct node *next;
} node;

node * ins_end(node *start) {
  node * temp = (node*)malloc(sizeof(node));
  printf("Enter a element to insert\n");
  scanf("%d",&temp->info);
  temp->next = NULL;
  if(start == NULL){
    return temp;
  }
  node * c = start;
  while(c->next != NULL){
    c = c->next;
  }
  c->next = temp;
  return start;
}
node * del_end(node * start){
  if(start == NULL){
    printf("Empty List.\n");
    return start;
  }
  node * c = start;
  node * p = NULL;
  while(c->next != NULL){
    p =c ;
    c = c->next;
  }
 
  p->next = NULL;
  free(c);
  return start;
}
node * ins_beg(node * start){
  node * temp = (node*)malloc(sizeof(node));
  temp->next = NULL;
  printf("Enter the number to insert at the beginning.\n");
  scanf("%d",&temp->info);
  temp->next = NULL;
  if(start == NULL){
    return start;
  }
  temp->next = start;
  start = temp;
  return start;
}

node * del_beg(node * start){
  if(start == NULL){
    printf("\nEmpty List.\n");
    return start;
  }
  node * c = start;
  start = start->next;
  free(c);
  return start;
}
node * reverse(node * start){
  node * p = start ,*q ,*r = NULL;
  while(p!= NULL){
    r = q;
    q = p;
    p = p->next;
    q->next = r;
  }
  start = q;
  return start;
}

void display(node * start){
  if(start == NULL){
    printf("Empty List\n");
  }
  node * c = start;
  while(c != NULL){
    printf("%d ",c->info);
    c = c->next;
  }
  printf("\n");
}

int main(){
  node * start = NULL;
  node * rev = NULL;
  while(true){
    printf("1.Ins_End\n2.Display\n3.Del_End\n4.Ins_Beg\n5.Del_Beg\n");
    int ch;
    scanf("%d",&ch);
    if(ch == 1){
      start = ins_end(start);
    }
    else if(ch == 2){
      display(start);
    }
    else if(ch == 3){
      start = del_end(start);
    }
    else if(ch == 4){
      start = ins_beg(start);
    }
    else if(ch == 5){
      start = del_beg(start);
    }
    else if(ch == 6){
      start = reverse(start);
    }
    else{
      break;
    }
  }
}
