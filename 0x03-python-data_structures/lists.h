#ifndef LISTS_H
#define LISTS_H
/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;
int is_palindrome(listint_t **head);
listint_t *add_nodeint_end(listint_t **head, const int n);
int check_pal(listint_t **head, listint_t *last);
void free_listint(listint_t *head);
#endif
