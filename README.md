# Порівняння ефективності жадібного алгоритму та алгоритму динамічного програмування

### Жадібний алгоритм (find_coins_greedy)
- **Часова складність:** O(N), де N — кількість номіналів монет.
- **Продуктивність при великих сумах:** Жадібний алгоритм працює швидко навіть для великих сум, якщо набір монет дозволяє обирати найбільші номінали. Він оптимальний у випадках, коли найбільші номінали монет можуть швидко наближати решту до потрібної суми.

### Алгоритм динамічного програмування (find_min_coins)
- **Часова складність:** O(N * M), де N — кількість номіналів монет, M — сума, яку потрібно видати.
- **Продуктивність при великих сумах:** Алгоритм динамічного програмування забезпечує мінімальну кількість монет для будь-якої суми, але вимагає більше часу для виконання, особливо при великих значеннях суми. Він корисний, якщо набір монет не дозволяє жадібний підхід.

### Висновки
- Жадібний алгоритм є швидким і ефективним, коли набір монет дозволяє обирати найбільші номінали, що добре працює для великих сум.
- Алгоритм динамічного програмування гарантує мінімальну кількість монет, але за рахунок більшої складності, що може бути важливим для повного набору номіналів або нестандартного набору монет.
