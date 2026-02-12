#include<stdio.h>

int main(){
    int n, reverse = 0, remainder, sign;

    scanf("%d", &n);

    if(n < 0){ 
        sign = -1; 
        n = -n; 
    }else { 
        sign = 1;
    }

    while(n != 0){
        remainder = n % 10;          
        reverse *= 10 + remainder;  
        n /= 10; 
    }

    reverse = reverse * sign;

    printf("%d", reverse);

    return 0;
}