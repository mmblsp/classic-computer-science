# classic-computer-science: Simple Problems

fibonacci_recursive - Важно наличие базового случая, иначе использование функции приводит к ошибке RecursionError: maximum recursion deth exceeded. Функция ограничена в работе глубиной рекурсии.
По умолчанию глубина рекурсии в языке Питон ограничена 1000 вызовов. Это ограничение можно поднять при помощи функции  setrecursionlimit из модуля system.

```python
import sys
sys.setrecursionlimit(10000)
```
Функция медленная, так как количество операций растёт в геометрической прогрессии

