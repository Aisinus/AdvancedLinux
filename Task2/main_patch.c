// 159e -> 5534
// 5532

#include <stdio.h>

int main(){
    int i;
    FILE *f1;

    int offset[2] = {5534, 5535};
    char data[] = {144, 144};

    if((f1 = fopen("hack_app", "r+")) != NULL ){
        for(i = 0; i<2; i++){
            fseek(f1, offset[i], SEEK_SET);
            fprintf(f1, "%c", data[i]);
        }
        printf("finished\n");
    }else{
        printf("file dont exist\n");
    }
    return 0;
}