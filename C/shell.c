
#include <stdio.h>
#include <stdlib.h>
//Declaration of function


void lsh_loop();










//End of declaration
int main(int argc,char **argv){
    //Run commmand loop
    lsh_loop();


    //To perform the shutdown
    return EXIT_SUCCESS;
}
void lsh_loop(void){
    char *line;
    char **args;
    int status;
    do{
        printf("->");
        line=lsh_read_line();
        args = lsh_split_line();
        status = lsh_execute();

        free(line);
        free(args);

    }while(status);


}

// Defining readline

#define LSH_RL_BUFSIZE 1024
char *lsh_read_line(void){
	int buffsize =LSH_RL_BUFSIZE;
	int position = 0;
	char *buufer  = malloc(sizeof(char) * bufsize);
	int c;
	
	if(!buffer){
		fprintf(stderr,"lsh:allocation error\n");
		exit(EXIT_FAILURE);
	}
	while(1){
		//Used to read a character
		c = getchar();
		//incase we hit a EOF we return a null character
		if(c ==EOF||c =='\n'){
			buffer[position]= '\0';
			return buffer;
		}
		else{
			buffer[position] = c;
		}
		position++;
		//if we exceed the buffer then we must reallocate.
		if(position>=bufsize){
			bufsize += LSH_RL_BUFSIZE;
			buffer = realloc(buffer,bufsize);
			if(!buffer){
				fprintf(stderr,"lsh allocation error\n");
				exit(EXIT_FAILURE);}
		}

		}
	
}


char *lsh_read_line(void){
	char *line = NULL;
	ssize_t bufsize = 0;
	//this allocates a buufer for getline
	if(getline(&line,&bufsize,stdin) == -1){
		if(feof(stdin)){
			exit(EXIT_SUCCESS);
			}
		else{
			perror("readline");
			exit(EXIT_FAILURE);
		}
		}
	return line;
	}
#define LSH_TOK_BUFSIZE 64
#define LSH_TOK_DELIM "\t\r\n\a"

char **lsh_split_line(char *line){
	int bufsize = LSH_TOK_BUFSIZE, position = 0;
	char **tokens = malloc(bufsize * sizeof(char *));
	char *token;
	
	
	if(!tokens){
		fprintf(stderr,"lsh: allocation error\n");
		exit(EXIT_FAILURE);
		}
	token = strtok(line, LSH_TOK_DELIM);
	
	while(token != NULL){
		tokens[position] = token;
		position++;
		
		if(position >= bufsize){
			bufsize += LSH_TOK_BUFSIZE;
			tokens = realloc(tokens,bufsize * sizeof(char*))
            if(!tokens){
                fprintf(stderr,"lsh: allocation error\n");
                exit(EXIT_FAILURE);
            }
	    }
        token = strtok(NULL,"lsh: allocation error\n");
    }
    tokens[position] = NULL;
    return tokens;

}
int lsh_launch(char ** args){
  pid_t pid ,wpid;
  int status;
  pid = fork();
  if(pid == 0){
    //Child Process
    if(execvp(args[0],args)== -1 ){
      perror("lsh");
    }
  }
  
}

    








