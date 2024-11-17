#include <stdbool.h>
#include <stdio.h>
#define MAX 10

typedef struct queue {
  int arr[MAX];
  int front;
  int rear;

} queue;

void initialize(queue *q) {
  q->front = -1;
  q->rear = -1;
}
void enq(queue *q) {
  if (q->rear == MAX) {
    printf("OverFlow.\n");
    return;
  }
  int ele;
  printf("Enter the element to be enqueued:\n");
  scanf("%d", &ele);

  q->arr[++q->rear] = ele;
}
void deq(queue *q) {
  if (q->front == q->rear) {
    printf("UnderFLow.\n");
    return;
  }
  printf("Popped %d.\n", q->arr[++q->front]);
}
void display(queue *q) {
  if (q->front == q->rear) {
    printf("UnderFlow.\n");
    return;
  }
  for (int i = q->front; i <= q->rear; i++) {
    printf("%d ", q->arr[i]);
  }
}
int main() {
  queue q;
  initialize(&q);
  while (true) {
    printf("\n1.Enq\n2.Deq\n3.Display\n4.Exit.\n");
    int ch;
    scanf("%d", &ch);
    if (ch == 1) {
      enq(&q);
    } else if (ch == 2) {
      deq(&q);
    } else if (ch == 3) {
      display(&q);
    } else {
      break;
    }
  }
}
