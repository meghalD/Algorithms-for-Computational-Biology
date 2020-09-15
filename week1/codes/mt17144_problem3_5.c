#include <stdio.h>

int pascal(int r,int c)
{
    if(r==c)
        return 1;
    else if(c==1)
        return 1;
    else
        return (pascal(r-1,c-1)+pascal(r-1,c));
}

int main() {
	//code
	int n,i,j;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
	    for(j=n-1;j>=i;j--)
	    {
	        printf("%c",32);
	    }
	    for(j=1;j<=i;j++)
	    {
	        printf("%d",pascal(i,j));
	        printf("%c",32);
	    }
	    printf("\n");
	}
	return 0;
}