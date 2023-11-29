#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - insert a new node in a sorted linked list
 *
 * @head : pointer to head of list
 * @number: the element to be add
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *prev, *current;

    current = *head;
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    while (current != NULL && current->n < number)
    {
        prev = current;
        current = current->next;
    }
    prev->next = new;
    new->next = current;
    new->n = number;

    return (new);
}
