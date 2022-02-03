#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
int main(){
int n;
int i;
int j;
int k;
int max;
int sth;
max = 0;
j = 1;
scanf("%d",&n);
sth = 0;
int *types = malloc(sizeof(int) * n);
for(int types_i = 0; types_i < n; types_i++){
scanf("%d",&types[types_i]);
}
// your code goes here
i = 0;
while (j <= 5 )
{
k = 0;
i = 0;
while (i < n)
{
if (types[i] == j)
k++;
i++;
}
if (k > max)
{
sth = j;
max = k;
}
j++;
}
printf("%d", sth);
return 0;
}