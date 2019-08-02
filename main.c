#include <stdio.h>
#include <stdlib.h>

void main()
{
    int i, sumo, ans;
    sumo = 0;
    ans = 0;
    for(i = 1; i<=200; i++)
    {
        sumo += i;
        if(i == 10)
        {
            ans += sumo;
        }
        else if(i == 100)
        {
            ans += sumo;
        }
        else if(i == 200)
        {
            ans += sumo;
        }
    }
    printf("%d", ans);
}
