# Zhylkybay Aisen
### Options
Help page when run ```python3 bldd.py -h``` ![][]![[Pasted image 20230312201126.png]]
The directory you want to scan (source) is the mandatory input. In addition you can specify the file in which to write the output of the program, if it is not specified the output will be produced in the console (--output).

### Output
Program output when running ```python3 bldd.py /home``` ![[Pasted image 20230312201618.png]]
Program output when running ```python3 bldd.py /home test.txt```![[Pasted image 20230312201742.png]]

### Problems:
Because of the peculiarities of the `lief` library (which I used to collect ELF data) I always get errors in the console when it is impossible to read them from the file.