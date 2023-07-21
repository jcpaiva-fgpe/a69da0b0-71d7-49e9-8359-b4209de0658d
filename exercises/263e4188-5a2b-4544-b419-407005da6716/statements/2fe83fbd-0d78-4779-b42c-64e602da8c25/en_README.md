Student List
==============================

![Illustration](05.jpg)

Task
------

Given a list of students with 3 fields (first name, surname and grade obtained in a given curricular unit), your task is to sort the list in the requested order, which can be ascending or descending from one of the 3 fields.

Input
-----

On the first line of the input is a single number indicating the type of order to use. That number can be:

* **1:** Sort by grade in descending order. In case of a tie sort by first name and in case of a new tie sort by surname.
* **2:** Sort by ascending (alphabetical) order of first name. In case of a tie sort by the order in which they came in the input.

In the second line of the input there is a number **N** (1 ≤ N ≤ 20,000) that corresponds to the number of students.

Below is the description of the students, one for each line, in the format "FIRST\_NAME SURNAME NOTE". The first name and surname consist of a sequence of an uppercase letter, followed by lowercase letters, without spaces, and with a maximum of 30 letters. The grade is an integer between 0 and 20 (inclusive).

Output
------

The output must consist of **N** lines, listing the students in the requested order (one per line, in the same format as the input).

Examples
--------

### Input 1

```txt
1
7
Joaquim Oliveira 10
Antonio Campos 17
Jorge Tavares 8
Luis Araujo 12
Carlos Pimenta 11
Carlos Araujo 11
Sonia Soares9
```

### Output 1

```txt
Antonio Campos 17
Luis Araujo 12
Carlos Araujo 11
Carlos Pimenta 11
Joaquim Oliveira 10
Sonia Soares9
Jorge Tavares 8
```

### Input 2

```txt
two
7
Joaquim Oliveira 10
Antonio Campos 17
Jorge Tavares 8
Luis Araujo 12
Carlos Pimenta 11
Carlos Araujo 11
Sonia Soares9
```

### Output 2

```txt
Antonio Campos 17
Carlos Pimenta 11
Carlos Araujo 11
Joaquim Oliveira 10
Jorge Tavares 8
Luis Araujo 12
Sonia Soares9
```