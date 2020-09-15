#include <stdio.h>
#include<string.h>

int main() {
	//code
	char str[]="TGAGAGAC";
	char pattern[]="GAG";
	int n=strlen(str);
	int p=strlen(pattern);
	int flag,i,j;
	for(i=0;i<n-p;i++)
	{
	    flag=1;
	    for(j=0;j<p;j++)
	    {
	        if(str[i+j]!=pattern[j])
	        {
	               flag=0;
	               break;
	        }
	    }
	    if(flag==1)
	        printf("occurence at %d \n",i);
	}
	return 0;
}