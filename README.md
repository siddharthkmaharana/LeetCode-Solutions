# LeetCode Solutions

Automated sync of LeetCode solutions to GitHub and Notion.

LeetCode Profile: [siddharthkmleetcode](https://leetcode.com/u/siddharthkmleetcode)

## Problems

- [0001 - Two Sum](0001-two-sum/solution.py) (Easy)
- [0002 - Add Two Numbers](0002-add-two-numbers/solution.py) (Medium)
- [0007 - Reverse Integer](0007-reverse-integer/solution.py) (Medium)
- [0009 - Palindrome Number](0009-palindrome-number/solution.py) (Easy)
- [0021 - Merge Two Sorted Lists](0021-merge-two-sorted-lists/solution.py) (Easy)
- [0049 - Group Anagrams](0049-group-anagrams/solution.py) (Medium)
- [0195 - Tenth Line](0195-tenth-line/solution.sh) (Easy)
- [0231 - Power of Two](0231-power-of-two/solution.py) (Easy)
- [0326 - Power of Three](0326-power-of-three/solution.py) (Easy)
- [3534 - Path Existence Queries in a Graph II](3534-path-existence-queries-in-a-graph-ii/solution.py) (Hard)

## Sync Architecture

This repository supports two complementary methods for synchronizing LeetCode solutions:

1. **Browser Extension (LeetHub v2 / LeetSync)**:
   - Automatically commits accepted solutions immediately upon submission on LeetCode.
   - State and file hashes are tracked via `stats.json` in the root directory.

2. **Scheduled GitHub Action (`.github/workflows/leetcode-sync.yml`)**:
   - Periodically checks your LeetCode account for newly accepted solutions and commits them directly to GitHub.
   - Requires `LEETCODE_SESSION` and `LEETCODE_CSRF_TOKEN` configured in Repository Secrets.

## Notion Sync

The GitHub Actions workflow (`.github/workflows/notion-sync.yml`) runs `scripts/notion_sync.py` on every push to `main`.
To enable it, configure the following GitHub Repository Secrets:
- `NOTION_TOKEN`: Internal Integration Secret with access to your Notion database.
- `NOTION_DATABASE_ID`: The ID of your target Notion database.

---

<!---LeetCode Topics Start-->
# LeetCode Topics
## Array
|  |
| ------- |
| [0001-two-sum](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0001-two-sum) |
| [0049-group-anagrams](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0049-group-anagrams) |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/3534-path-existence-queries-in-a-graph-ii) |
## Binary Search
|  |
| ------- |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/3534-path-existence-queries-in-a-graph-ii) |
## Bit Manipulation
|  |
| ------- |
| [0231-power-of-two](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0231-power-of-two) |
## Graph
|  |
| ------- |
| [3534-path-existence-queries-in-a-graph-ii](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/3534-path-existence-queries-in-a-graph-ii) |
## Hash Table
|  |
| ------- |
| [0001-two-sum](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0001-two-sum) |
| [0049-group-anagrams](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0049-group-anagrams) |
## Linked List
|  |
| ------- |
| [0002-add-two-numbers](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0002-add-two-numbers) |
| [0021-merge-two-sorted-lists](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0021-merge-two-sorted-lists) |
## Math
|  |
| ------- |
| [0002-add-two-numbers](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0002-add-two-numbers) |
| [0007-reverse-integer](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0007-reverse-integer) |
| [0009-palindrome-number](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0009-palindrome-number) |
| [0231-power-of-two](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0231-power-of-two) |
| [0326-power-of-three](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0326-power-of-three) |
## Recursion
|  |
| ------- |
| [0002-add-two-numbers](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0002-add-two-numbers) |
| [0021-merge-two-sorted-lists](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0021-merge-two-sorted-lists) |
| [0231-power-of-two](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0231-power-of-two) |
| [0326-power-of-three](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0326-power-of-three) |
## Shell
|  |
| ------- |
| [0195-tenth-line](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0195-tenth-line) |
## Sorting
|  |
| ------- |
| [0049-group-anagrams](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0049-group-anagrams) |
## String
|  |
| ------- |
| [0049-group-anagrams](https://github.com/siddharthkmaharana/LeetCode-Solutions/tree/main/0049-group-anagrams) |
<!---LeetCode Topics End-->
