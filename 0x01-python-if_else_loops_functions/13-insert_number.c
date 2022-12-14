# include "lists.h"
# include <stdlib.h>

/**
 * insert_node - insert node into a sorted linked lists
 * @head: double pointer to head
 * @num: number to insert
 *
 * Return: pointer to inserted node
 */

listint_t *insert_node(listint_t **head, int num)
{
	listint_t *newnode, *head_c, *tmp = NULL;

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);
	newnode->n = num;
	newnode->next = NULL;
	if (!head || !(*head))
	{
		if (head && !(*head))
		{
			*head = newnode;
			return (newnode);
		}
		free(newnode);
		return (NULL);
	}
	head_c = *head;
	while (head_c)
	{
		if (num <= head_c->n)
		{
			if (tmp == NULL)
			{
				newnode->next = head_c;
				*head = newnode;
				return (newnode);
			}
			tmp->next = newnode;
			newnode->next = head_c;
			return (newnode);
		}
		tmp = head_c;
		head_c = head_c->next;
	}
	tmp->next = newnode;
	return (newnode);
}
