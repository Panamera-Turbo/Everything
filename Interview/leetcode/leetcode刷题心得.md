# [点击去B站：Leetcode力扣必备算法知识和练习题|手画图解版](https://b23.tv/bIQs1w)
[代码详见 ./ leetcodeTry.java](leetcodeTry.java)
## 双指针
1. 普通指针：两个指针向一个方向移动
2. 对撞指针：两个指针从两边来。例如[881](https://leetcode-cn.com/problems/boats-to-save-people/)。先调用Arrays.sort(people)对数组进行排序，再对撞。
3. 快慢指针：一个每次走一步，一个每次走两步。例如[141](https://leetcode-cn.com/problems/linked-list-cycle/submissions/)。注意判空时应当先判断head再判断head.next。fast同理

## 二分查找法
- 二分查找一定要有序
题目：
1. [704.二分](https://leetcode-cn.com/problems/binary-search/)
2. [35.搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/)<br>注意中间的浮标（pos）应当表达成 $pos = head + \frac{tail-head}{2}$, 来避免直接写成 $pos = \frac{head + tail}{2}$ 可能出现超int的情况；<br>可以用`递归`，也可以用`while(head < tail)`循环
3. [162.寻找峰值](https://leetcode-cn.com/problems/find-peak-element/)<br>关键要抓住：**若nums[m] < nums[m+1], 则峰值在m右侧;若nums[m] > nums[m+1]，则峰值在m+1左侧**
4. [74.二维矩阵搜索](https://leetcode-cn.com/problems/search-a-2d-matrix/)<br>二维矩阵升序排列，直接将二维矩阵二分查找，令`left = 0, right = m * n - 1, xPos = ((left + right) / n), yPos = ((left + right) % n)`作为初始,开始二分

## 小技巧：滑动窗口
- 目的：减少循环中的计算量

举例：<br>给定数组s[n], 计算其中连续三个数之和的最大值
1. 暴力法
2. 滑动窗口法<br>窗口1 = s[0] + s[1] + s[2]<br>窗口2 = 窗口1 - s[0] + s[3]


例题：
1. [209.长度最小的子数组](https://leetcode-cn.com/problems/minimum-size-subarray-sum/) 
    - 对于非定长的数组，灵活分析决定是否能够采用滑动窗口
    - 两种方法：<br>1. 固定window长度，依次遍历，有合适就返回；再改变window长度进行下一次遍历;<br>2. 对一个窗口不断增长直到和超过target，然后逐个减去window的前面数字直导小于target，开始下一次
2. [1456.定长子串中元音的最大数目](https://leetcode-cn.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)<br>典型窗口