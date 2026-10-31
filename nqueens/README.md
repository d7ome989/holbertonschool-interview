# N Queens | مشكلة الملكات

## English

### Description
This project solves the **N queens puzzle**: placing N non-attacking queens on an N×N chessboard. The program prints every possible solution, one per line.

### How it works
The program uses **backtracking**:
1. Place one queen in each row, starting from row 0.
2. For each row, try every column and check if it is safe (`is_safe`): no queen in the same column or on the same diagonal.
3. If the position is safe, move to the next row.
4. If no column works, go back to the previous row and try another column.
5. When all N rows are filled, print the solution.

Two queens attack each other if they share a column, or if
`abs(row1 - row2) == abs(col1 - col2)` (same diagonal).

### Usage
```
./0-nqueens.py N
```
- `N` must be an integer greater than or equal to 4.
- Wrong number of arguments: prints `Usage: nqueens N`, exit status 1.
- N is not an integer: prints `N must be a number`, exit status 1.
- N is smaller than 4: prints `N must be at least 4`, exit status 1.

### Example
```
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```
Each solution is a list of `[row, column]` pairs.

### Requirements
- Python 3 (3.4.3 on Ubuntu 14.04 LTS)
- Only the `sys` module is imported
- PEP 8 style (`pycodestyle`)
- All files are executable and start with `#!/usr/bin/python3`

---

## العربية

### الوصف
هذا المشروع يحل **مشكلة N ملكات**: نحط N ملكات على رقعة شطرنج حجمها N×N بحيث ما تضرب أي ملكة ملكة ثانية. البرنامج يطبع كل الحلول الممكنة، حل واحد في كل سطر.

### كيف يشتغل
البرنامج يستخدم أسلوب **الرجوع (Backtracking)**:
1. نحط ملكة وحدة في كل صف، نبدأ من الصف 0.
2. في كل صف نجرب كل الأعمدة ونفحص هل الخانة آمنة (`is_safe`): ما فيه ملكة في نفس العمود أو نفس القطر.
3. إذا الخانة آمنة ننتقل للصف اللي بعده.
4. إذا ما لقينا عمود مناسب نرجع للصف اللي قبله ونجرب عمود ثاني.
5. إذا ملينا كل الصفوف الـ N نطبع الحل.

ملكتين تضربون بعض إذا كانوا في نفس العمود، أو إذا
`abs(فرق الصفوف) == abs(فرق الأعمدة)` (نفس القطر).

### طريقة الاستخدام
```
./0-nqueens.py N
```
- `N` لازم يكون رقم صحيح أكبر من أو يساوي 4.
- عدد arguments غلط: يطبع `Usage: nqueens N` ويخرج بـ 1.
- N مو رقم: يطبع `N must be a number` ويخرج بـ 1.
- N أقل من 4: يطبع `N must be at least 4` ويخرج بـ 1.

### مثال
```
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```
كل حل عبارة عن قائمة أزواج `[الصف, العمود]`.

### المتطلبات
- Python 3 (النسخة 3.4.3 على Ubuntu 14.04 LTS)
- نستورد فقط مكتبة `sys`
- أسلوب PEP 8 (`pycodestyle`)
- كل الملفات قابلة للتنفيذ وأول سطر فيها `#!/usr/bin/python3`

---

## Author | المؤلف
Abdulrhman Saleh Alduqil (d7ome989)
