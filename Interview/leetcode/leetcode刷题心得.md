# [点击去B站：Leetcode力扣必备算法知识和练习题|手画图解版](https://b23.tv/bIQs1w)
## 双指针
1. 普通指针：两个指针向一个方向移动
2. 对撞指针：两个指针从两边来。例如[881](https://leetcode-cn.com/problems/boats-to-save-people/)。先调用Arrays.sort(people)对数组进行排序，再对撞。
3. 快慢指针：一个每次走一步，一个每次走两步。例如[141](https://leetcode-cn.com/problems/linked-list-cycle/submissions/)。注意判空时应当先判断head再判断head.next。fast同理

## 二分查找法
- 二分查找一定要有序
题目：
1. [704](https://leetcode-cn.com/problems/binary-search/)
2. [35](https://leetcode-cn.com/problems/search-insert-position/)<br>注意中间的浮标（pos）应当表达成 $pos = head + \frac{tail-head}{2}$, 来避免直接写成 $pos = \frac{head + tail}{2}$ 可能出现超int的情况；<br>可以用`递归`，也可以用`while(head < tail)`循环
3. []()
4. []()