# include "lists.h"
# include <stddef.h>
#include <stdlib.h>
listint_t *copy_list(listint_t *head);
listint_t *reverse_list(listint_t **head);

/**
 * is_palindrome - check if a list of int is a is_palindrome
 * @head: pointer to head list
 * Return: 1 if palindrome 0 not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *cp_list, *tmp;

	if (head && !(*head))
		return (1);
	cp_list = copy_list((*head));
	tmp = reverse_list(&cp_list);
	while (*(head))
	{
		if ((*head)->n != cp_list->n)
		{
			free_listint(tmp);
			return (0);
		}
		(*head) = (*head)->next;
		cp_list = cp_list->next;
	}
	free_listint(tmp);
	return (1);
}


/**
 * reverse_list - reverse a linked reverse_list
 * @head: double pointer to head
 * Return: pointer to reversed reverse_list
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *p = NULL, *n = NULL;

	while (*head)
	{
		n = (*head)->next;
		(*head)->next = p;
		p = (*head);
		(*head) = n;
	}
	(*head) = p;
	return (*head);
}

/**
 * copy_list - copy linked copy_list
 * @head: head to copy from
 * Return: pointer to new list
 */
listint_t *copy_list(listint_t *head)
{
	listint_t *new_list, *tmp;

	if (!head)
		return (NULL);
	new_list = malloc(sizeof(listint_t));
	if (!new_list)
		return (NULL);
	tmp = new_list;
	while (head)
	{
		tmp->n = head->n;
		if (!(head->next))
			break;
		tmp->next = malloc(sizeof(listint_t));
		tmp = tmp->next;
		if (!tmp)
		{
			free_listint(new_list);
			return (NULL);
		}
		tmp->next = NULL;
		head = head->next;
	}
	return (new_list);
}
