# [点击去B站：Leetcode力扣必备算法知识和练习题|手画图解版](https://b23.tv/bIQs1w)
## 双指针
1. 普通指针：两个指针向一个方向移动
2. 对撞指针：两个指针从两边来。例如[leetcode881](https://leetcode-cn.com/problems/boats-to-save-people/)。先调用Arrays.sort(people)对数组进行排序，再对撞。
3. 快慢指针：一个每次走一步，一个每次走两步。例如[leetcode141](https://leetcode-cn.com/problems/linked-list-cycle/submissions/)。注意判空时应当先判断head再判断head.next。fast同理

## 二分查找法
二分查找一定要有序
