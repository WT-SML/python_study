class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1.reverse()
        l2.reverse()
        for i, v in enumerate(l1):
            l1[i] = str(v)
        for i, v in enumerate(l2):
            l2[i] = str(v)
        l1_str = ''.join(l1)
        l2_str = ''.join(l2)
        sum_str = str(int(l1_str)+int(l2_str))
        sum_list = []
        for i in sum_str:
            sum_list.append(int(i))
        sum_list.reverse()
        return sum_list


print(Solution().addTwoNumbers([2, 4, 3],
                               [5, 6, 4]))
