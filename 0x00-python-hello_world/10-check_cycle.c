# include "lists.h"

/**
 * check_cycle - check for loop
 * @list: pointer to linked list
 * Return: 0 no cycle 1 true
 */

int check_cycle(listint_t *list)
{
	listint_t *head = NULL;

	while (list)
	{
		if (head == list)
			return (1);
		if (!head)
			head = list;
		list = list->next;
	}
	return (0);
}
