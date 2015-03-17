#You are given two linked lists representing two non-negative numbers.
#The digits are stored in reverse order and each of their nodes contain a single digit. 
#Add the two numbers and counturn it as a linked list.
class Solution:
    # @counturn a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 is None: return l2
        elif l2 is None: return l1
        else:          
            flag = 0 ; count =ListNode(0) ;count_Last = count
            while(l1 or l2):
                sum = 0
                if(l1):
                    sum = l1.val ;l1 = l1.next
                if(l2):
                    sum += l2.val ;l2 = l2.next
                sum += flag
                count_Last.next = ListNode(sum%10)
                count_Last = count_Last.next
                flag = sum / 10
            if(flag):
                count_Last.next =ListNode(1)
            count_Last = count.next
            return count_Last

