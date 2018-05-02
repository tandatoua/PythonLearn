#!/usr/bin/env python
# -*- conding:utf-8 -*-

# Author:Tandatoua
# FileName:SinglyLinked.py
# Python Version:Python 3.6
#Code Specification:pep8
# Desc:Singly Linked



class SinglyLinkNode(object):

    def __init__(self, data):
        self.data = data
        self.next = None


# Traversing a linked list.
def traver_linked_list(link_head):
    current_node = link_head
    while current_node:
        print(current_node.data)
        current_node = current_node.next

# Searching a linked list
def search_lined_list(link_head, target):
    currend_node = link_head
    while currend_node is not None and currend_node.data != target:
        currend_node = currend_node.next
    return currend_node

if __name__ == "__main__":
    a = SinglyLinkNode(1)
    b = SinglyLinkNode(2)
    c = SinglyLinkNode(3)
    d = SinglyLinkNode(4)
    a.next = b
    b.next = c
    c.next = d
    traver_linked_list(a)
    print(search_lined_list(a,3).data)
