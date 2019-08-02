#include <stdio.h>
#include <stdlib.h>

void main()
{
    int i, sumo;
    sumo = 0;
    for(i = 1; i<=200; i++)
    {
        sumo += i;
        if(i == 10)
        {
            printf("(%d+", sumo);
        }
        else if(i == 100)
        {
            printf("%d+", sumo);
        }
        else if(i == 200)
        {
            printf("%d)", sumo);
        }
    }
}
