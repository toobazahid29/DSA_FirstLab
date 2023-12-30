class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
class LinkedList:
    def __init__(self):
       self.head = None  
 # Add a new node at the beginning
    def insert_at_head(self, new_node):
        new_node.next = self.head  # Connect the new node to the current head
        self.head = new_node  # Make the new node the head

   # Delete a node with a specific data
    def delete_node(self, data):
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.data == data:  # Node found
                if previous_node:
                    previous_node.next = current_node.next  # Skip over the node
                else:
                    self.head = current_node.next  # Update head if deleting the first node
                return
            previous_node = current_node
            current_node = current_node.next

    # Print the linked list data
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")  # Indicate the end of the list

# Example usage
first_node = Node("Ahmad")
linked_list = LinkedList()
linked_list.insert_at_head(first_node)

second_node = Node("Amaan")
linked_list.insert_at_head(second_node)

third_node = Node("Sami")
linked_list.insert_at_head(third_node)

linked_list.print_list()  # Output: sami -> Amaan -> Ahmad -> None

# Delete "Amaan"
linked_list.delete_node("Amaan")

linked_list.print_list()  # Output: sami -> Ahmad -> None
