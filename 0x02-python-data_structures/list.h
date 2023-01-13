#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

def print_list_integer(my_list=[]):
def replace_in_list(my_list, idx, element):
def print_reversed_list_integer(my_list=[]):
def new_in_list(my_list, idx, element):

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_pal(listint_t **head, listint_t *last);
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
