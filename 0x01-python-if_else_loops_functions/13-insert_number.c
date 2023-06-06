#include <stdlib.h>
#include <stddef.h>
#include "lists.h"

/**
 * *insert_node - inserts a number into a sorted singly-linked list
 * @head: head of the linked list.
 * @number: The number to be inserted.
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new, *tmp = *head;

new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);

(*new).n = number;

if (*head == NULL || number <= (*head)->n)
{
(*new).next = *head;
*head = new;
return (new);
}

while (tmp && tmp->next && tmp->next->n < number)
tmp = (*tmp).next;
new->next = tmp->next;
tmp->next = new;

return (new);
}
