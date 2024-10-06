# Порівняльний аналіз алгоритмів сортування

## Опис завдання

У цьому завданні було порівняно три алгоритми сортування: злиття (Merge Sort), вставки (Insertion Sort) та вбудований Timsort (який використовується у функції `sorted()` в Python). Було протестовано ці алгоритми на різних наборах даних — несортованих, напівсортованих та майже відсортованих масивах з 10, 100 і 1000 елементів.

## Результати тестування

### Ефективність на несортованих наборах:

- **Merge Sort** показує стабільну ефективність навіть на великих масивах.
- **Insertion Sort** стає значно повільнішим з ростом розміру масиву.
- **Timsort** демонструє найкращі результати для будь-якого розміру.

### Ефективність на напівсортованих наборах:

- **Merge Sort** залишається стабільним.
- **Insertion Sort** працює дещо краще, оскільки частина масиву вже відсортована.
- **Timsort** знову показує найкращий час, оскільки добре працює на майже відсортованих масивах.

### Ефективність на майже відсортованих наборах:

- **Merge Sort** все ще стабільний, але Timsort перевершує його за швидкістю.
- **Insertion Sort** працює значно краще на таких наборах, оскільки алгоритм вставок особливо добре працює на майже відсортованих даних.
- **Timsort** продовжує залишатися найшвидшим на таких наборах.

## Висновки

- **Timsort** є найбільш універсальним і швидким для всіх типів даних. Це робить його оптимальним вибором у більшості випадків.
- **Merge Sort** забезпечує стабільність і передбачувану швидкість, особливо на великих масивах.
- **Insertion Sort** підходить лише для дуже малих або вже майже відсортованих масивів, оскільки значно сповільнюється на великих наборах.

Цей аналіз показує, що вибір алгоритму сортування має бути адаптованим до типу та розміру даних для досягнення найкращої ефективності.
