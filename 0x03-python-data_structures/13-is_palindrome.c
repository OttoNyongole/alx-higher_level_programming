#include "lists.h"
/**
 * is_palindrome - check if the linked list is palindrome
 * @head: a pointer to the linked list
 * Return:success 1 if it is palindrome fail 0 if its not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *cursor = NULL, *start = NULL, *end = NULL;
	if (*head == NULL)
		return (1);
	start = *head;
	while (sart != end)
	{
		cursor = start;
		while (cursor->next && cursor->next != end)
			cutsor = cutsor->next;
		end = cursor;
		if (start->n != end->n)
			return (0);
		if (start == end)
			break;
		start = start->next;
	}
	return (1);
}
