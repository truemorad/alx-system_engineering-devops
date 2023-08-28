#include <stdlib.h>
#include <time.h>
/* more headers goes there */
#include <stdio.h>
/* betty style doc for function main goes there */
/**
 * main - yeb main
 *
 * Return: 0
 */

int main(void)
{
	int i;

	for (i = 0 ; i < 10 ; i++)
{
		putchar(i + '0');
		if (i != 9)
		{
		putchar(',');
		putchar(' ');
}
}
	putchar('\n');
	return (0);
}
