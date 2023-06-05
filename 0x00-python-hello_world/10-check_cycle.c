#include "lists.h"
#include <stdio.h>

/**
  * check_cycle - Checks if a singly linked list has a cycle in it
  * @list: The singly linked list to check
  *
  * Return: 1 if has a cycle in it or 0 if not
  */
int check_cycle(listint_t *list)
{
	listint_t *rabbit = list, *dog = list;
	int found = 0;

	while ((rabbit && dog) && dog ->next)
	{		
		rabbit = rabbit->next;

		if (dog->next || dog->next->next)	
			dog = dog->next->next;
		else
			break;

		if (rabbit == dog)
		{
			found = 1;
			break;
		}
	}

	return (found);
}i
