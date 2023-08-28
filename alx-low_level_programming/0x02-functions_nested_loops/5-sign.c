#include "main.h"

/**
 * print_sign - yeb main
 * @n: yeb
 * Return: 1 0 "-1"
 * 0 and print 0 if n is zero
 * -1 and prints - if n is less than zero
 */

int print_sign(int n)
{
	if (n > 0)
	{
		_putchar('+');
		return (1);
	}
	else if (n == 0)
	{
		_putchar(48);
		return (0);
	}
	else if (n < 0)
	{
		_putchar('-');
	}
	return (-1);

}

