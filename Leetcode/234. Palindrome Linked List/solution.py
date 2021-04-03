class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def is_palindrome(self, head):
        # Code to check if it is palindrome LinkedList
        # T(n) = O(n) and S(n) = O(n)
        arr = []

        while head is not None:
            arr.append(head.val)
            head = head.next

        return arr == list(reversed(arr))

    def take_input(self, array):
        # Receive input
        node = ListNode(array[0])
        head = node

        for i in range(1, len(array)):
            node.next = ListNode(array[i])
            node = node.next
            
        return head


if __name__ == "__main__":
    solution = Solution()
    input_array = [1, 2, 2, 1]
    head = solution.take_input(input_array)
    print(solution.is_palindrome(head))
