#include "main.h"

/**
 * *_strcat - yeb main
 * @dest: input
 * @src: input
 * Return: void
 */

char *_strcat(char *dest, char *src)
{
	int destlen;
	int srclen;

	destlen = 0;
	while (dest[destlen] != '\0')
	{
		destlen++;
	}
	srclen = 0;
	while (src[srclen] != '\0')
	{
		dest[destlen] = src[srclen];
		destlen++;
		srclen++;
	}
	dest[destlen] = '\0';
	return (dest);
}
