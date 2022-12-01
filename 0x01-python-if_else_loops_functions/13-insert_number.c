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
	listint_t *newnode, *head_c = *head, *tmp;

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);
	newnode->n = num;
	if (!head)
		return (*head = (newnode->next = NULL));
	while (head_c)
	{
		if (num >= head_c->n && (head_c->next)->n > num)
		{
			tmp = head_c->next;
			head_c->next = newnode;
			newnode->next = tmp;
			return (newnode);
		}
		head_c = head_c->next;
	}
	return (NULL);
}

