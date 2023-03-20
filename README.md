Домашнє завдання #3
Перша частина для потоків
Напишіть програму обробки папки "Хлам", яка сортує файли у вказаній папці за розширеннями з використанням кількох потоків. Пришвидшіть обробку великих каталогів з великою кількістю вкладених папок та файлів за рахунок паралельного виконання обходу всіх папок в окремих потоках. Найбільш витратним за часом буде перенесення файлу та отримання списку файлів у папці (ітерація по вмісту каталогу). Щоб прискорити перенесення файлів, його можна виконувати в окремому потоці чи пулі потоків. Це тим зручніше, що результат цієї операції ви в додатку не обробляєте та можна не збирати жодних результатів. Щоб прискорити обхід вмісту каталогу з кількома рівнями вкладеності, ви можете обробку кожного підкаталогу виконувати в окремому потоці або передавати обробку в пул потоків.

Друга частина для процесів
Напишіть реалізацію функції factorize, яка приймає список чисел та повертає список чисел, на які числа з вхідного списку поділяються без залишку.

Реалізуйте синхронну версію та виміряйте час виконання.

Потім покращіть продуктивність вашої функції, реалізувавши використання кількох ядер процесора для паралельних обчислень і замірьте час виконання знову. Для визначення кількості ядер на машині використовуйте функцію cpu_count() з пакета multiprocessing
