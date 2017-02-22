#include<iostream>
using namespace std;

// int MIN(unsigned int a, unsigned int b, unsigned int c)
// {
// 	unsigned int min = a;
// 	if(min!=0)
// 	{
// 		if(b<c && b!=0)
// 		{
// 			if(b<min)
// 				min = b;
// 		}
// 		else if(c<min)
// 			min = c;
// 	}
// 	else
// 	{
// 		min = b;
// 		if(c<b)
// 			min = c;
// 	}
// 	return min;
// }

int main()
{
	unsigned int r,g,b,i=0;
	cin>>r>>g>>b;
	while(true)
	{
		int min = std::min(std::min(r,g), b);
		cout<<"min: "<<min<<"\n";
		if(r>0 || g>0)
		{
			if(r>0)
				r -= min;
			if(g>0)
				g -= min;
			b -= min;
			i+=min;
		}
		else
		{
			b /= 2;
			i++;
		}
		cout<<r<<" "<<g<<" "<<b<<" "<<i<<"\n";	
		if(r == 0 && g == 0 && b == 0)
			break;
	}
	cout<<i<<"\n";
	return 0;
}