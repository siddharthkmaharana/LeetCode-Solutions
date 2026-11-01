<h2><a href="https://leetcode.com/problems/path-existence-queries-in-a-graph-ii">3534. Path Existence Queries in a Graph II</a></h2><h3>Hard</h3><hr><p>You are given an integer <code>n</code> representing the number of nodes in a graph, labeled from 0 to <code>n - 1</code>.</p>

<p>You are also given an integer array <code>nums</code> of length <code>n</code> and an integer <code>maxDiff</code>.</p>

<p>An <strong>undirected </strong>edge exists between nodes <code>i</code> and <code>j</code> if the <strong>absolute</strong> difference between <code>nums[i]</code> and <code>nums[j]</code> is <strong>at most</strong> <code>maxDiff</code> (i.e., <code>|nums[i] - nums[j]| &lt;= maxDiff</code>).</p>

<p>You are also given a 2D integer array <code>queries</code>. For each <code>queries[i] = [u<sub>i</sub>, v<sub>i</sub>]</code>, find the <strong>minimum</strong> distance between nodes <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code><sub>.</sub> If no path exists between the two nodes, return -1 for that query.</p>

<p>Return an array <code>answer</code>, where <code>answer[i]</code> is the result of the <code>i<sup>th</sup></code> query.</p>

<p><strong>Note:</strong> The edges between the nodes are unweighted.</p>