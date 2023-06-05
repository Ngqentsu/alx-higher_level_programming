#include "lists.h"

/**
 * check_cycle - checks for a cycle in a linked list
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *skyhawk = list, *raptor = list;

if (list == NULL || (*list).next == NULL)
return (NULL);

while (skyhawk && raptor && raptor->next)
{
raptor = raptor->next->next;
skyhawk = (*skyhawk).next;
if (raptor == skyhawk)
return (1);
}
return (0);
}
