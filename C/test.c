#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <sys/wait.h>
#include <semaphore.h>
#include <pthread.h>
#define MAXCAP 5

int buff[MAXCAP];


sem_t pmutex ,cmutex , empty , full;

int in = 1 , out = 1;
int item  = 0;

void *produce(void *arg){
    sem_wait(&empty);
    item++;
    sem_wait(&pmutex);
    buff[in] = item;
    printf("Producing data into %d.\n", in);
    sleep(1);
    printf("Producing data into %d is done.\n" , in);
    in = in % MAXCAP + 1;
    sem_post(&pmutex);
    sem_post(&full);
    return 0;
}

void *consume(void *arg){
    int citem= 0;
    sem_wait(&full);
    sem_wait(&cmutex);
    citem = buff[out];
    printf("Consuming data from %d.\n", out);
    sleep(1);
    printf("Consuming data form %d is done.\n", out);

    sem_post(&cmutex);
    sem_post(&empty);
    return 0;

}

int main(int argc , const char *argv[]){
    in = 1 , out = 1;
    int i , NumThreads;
    sem_post(&pmutex);
    sem_post(&cmutex);
    sem_init(&full , 0 , 0);
    sem_init(&empty , 0 , MAXCAP);
    pthread_t *producers  , *consumers;
    NumThreads = abs(atoi(argv[1]));
    producers = (pthread_t *)malloc(sizeof(pthread_t) * NumThreads);
    consumers = (pthread_t *)malloc(sizeof(pthread_t) * NumThreads);
    for(i = 0 ; i < NumThreads; i++){
        pthread_create(&consumers[i] , NULL , &consume , NULL);
        pthread_create(&producers[i] , NULL , &produce , NULL);

    }
    for( i = 0 ; i < NumThreads ; i++ ){
        pthread_join(producers[i] , NULL);
        pthread_join(consumers[i] , NULL);
    }
}
