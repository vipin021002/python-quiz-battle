# --- English Classic Pools ---
easy_questions = [
    {
        'question': 'What is the output of print(2 + 3)?',
        'options': ['5', '6', '23', 'Error'],
        'answer': '5'
    },
    {
        'question': 'Which symbol is used to comment a single line in Python?',
        'options': ['#', '//', '--', '/*'],
        'answer': '#'
    },
    {
        'question': 'What is the correct file extension for Python files?',
        'options': ['.py', '.python', '.pt', '.pyt'],
        'answer': '.py'
    },
    {
        'question': 'Which function is used to get input from the user?',
        'options': ['input()', 'scan()', 'get()', 'read()'],
        'answer': 'input()'
    },
    {
        'question': 'What is the output of print(10 // 3)?',
        'options': ['3.33', '3', '4', '3.0'],
        'answer': '3'
    },
    {
        'question': 'Which of these is a valid variable name in Python?',
        'options': ['2var', 'var_2', 'var-2', 'var 2'],
        'answer': 'var_2'
    },
    {
        'question': 'How do you start a function in Python?',
        'options': ['def', 'function', 'fun', 'define'],
        'answer': 'def'
    },
    {
        'question': 'What is the output of print(type([]))?',
        'options': ["<class 'list'>", "<class 'dict'>", "<class 'tuple'>", "<class 'set'>"],
        'answer': "<class 'list'>"
    },
    {
        'question': 'Which of the following is not a Python data type?',
        'options': ['list', 'set', 'array', 'tuple'],
        'answer': 'array'
    },
    {
        'question': 'What does the len() function do?',
        'options': ['Returns the length of an object', 'Returns the type of an object', 'Returns the value of an object', 'Returns the id of an object'],
        'answer': 'Returns the length of an object'
    },
    {
        'question': 'What is the output of print(5 + 7)?',
        'options': ['12', '57', '2', '13'],
        'answer': '12'
    },
    {
        'question': 'Which function is used to display output in Python?',
        'options': ['print()', 'output()', 'echo()', 'display()'],
        'answer': 'print()'
    },
    {
        'question': 'What is the output of print("Python"[0])?',
        'options': ['P', 'y', 'n', 'o'],
        'answer': 'P'
    },
    {
        'question': 'Which of these is a Python keyword?',
        'options': ['for', 'loop', 'repeat', 'iterate'],
        'answer': 'for'
    },
    {
        'question': 'What is the output of print(2 ** 3)?',
        'options': ['8', '6', '9', '5'],
        'answer': '8'
    },
    {
        'question': 'Which operator is used for addition?',
        'options': ['+', '-', '*', '/'],
        'answer': '+'
    },
    {
        'question': 'What is the output of print(10 % 3)?',
        'options': ['1', '3', '0', '10'],
        'answer': '1'
    },
    {
        'question': 'Which of these is a valid list?',
        'options': ['[1, 2, 3]', '(1, 2, 3)', '{1, 2, 3}', 'list(1,2,3)'],
        'answer': '[1, 2, 3]'
    },
    {
        'question': 'What is the output of print("a" * 3)?',
        'options': ['aaa', 'a3', 'Error', '3a'],
        'answer': 'aaa'
    },
    {
        'question': 'Which function returns the length of a list?',
        'options': ['len()', 'count()', 'size()', 'length()'],
        'answer': 'len()'
    },
    {
        'question': 'What is the output of print(4 // 2)?',
        'options': ['2', '2.0', '0', '1'],
        'answer': '2'
    },
    {
        'question': 'Which of these is a comment in Python?',
        'options': ['# comment', '// comment', '-- comment', '/* comment */'],
        'answer': '# comment'
    },
    {
        'question': 'What is the output of print(7 - 2)?',
        'options': ['5', '9', '2', '7'],
        'answer': '5'
    },
    {
        'question': 'Which function converts a string to an integer?',
        'options': ['int()', 'str()', 'float()', 'chr()'],
        'answer': 'int()'
    }
]

intermediate_questions = [
    {
        'question': 'What is the output of print([i for i in range(3)])?',
        'options': ['[0, 1, 2]', '[1, 2, 3]', '[0, 1, 2, 3]', '[1, 2]'],
        'answer': '[0, 1, 2]'
    },
    {
        'question': 'Which method is used to add an item to a list?',
        'options': ['add()', 'append()', 'insert()', 'push()'],
        'answer': 'append()'
    },
    {
        'question': 'What is the output of print(type({}))?',
        'options': ["<class 'dict'>", "<class 'set'>", "<class 'list'>", "<class 'tuple'>"],
        'answer': "<class 'dict'>"
    },
    {
        'question': 'How do you start a for loop in Python?',
        'options': ['for i in range(5):', 'for(i=0;i<5;i++)', 'foreach i in range(5)', 'loop i in range(5)'],
        'answer': 'for i in range(5):'
    },
    {
        'question': 'Which operator is used for exponentiation?',
        'options': ['^', '**', 'exp()', '^^'],
        'answer': '**'
    },
    {
        'question': 'What is the output of print("Hello"[1])?',
        'options': ['H', 'e', 'l', 'o'],
        'answer': 'e'
    },
    {
        'question': 'How do you import the math module?',
        'options': ['import math', 'include math', 'using math', 'require math'],
        'answer': 'import math'
    },
    {
        'question': 'Which method removes the last item from a list?',
        'options': ['remove()', 'pop()', 'delete()', 'discard()'],
        'answer': 'pop()'
    },
    {
        'question': 'What is the output of print(5 != 3)?',
        'options': ['True', 'False', 'None', 'Error'],
        'answer': 'True'
    },
    {
        'question': 'Which of the following is a tuple?',
        'options': ['(1, 2, 3)', '[1, 2, 3]', '{1, 2, 3}', 'tuple[1, 2, 3]'],
        'answer': '(1, 2, 3)'
    },
    {
        'question': 'What is the output of print([i*2 for i in range(3)])?',
        'options': ['[0, 2, 4]', '[2, 4, 6]', '[1, 2, 3]', '[0, 1, 2]'],
        'answer': '[0, 2, 4]'
    },
    {
        'question': 'Which method returns the index of an item in a list?',
        'options': ['index()', 'find()', 'locate()', 'position()'],
        'answer': 'index()'
    },
    {
        'question': 'What is the output of print("abc".upper())?',
        'options': ['ABC', 'abc', 'Abc', 'aBc'],
        'answer': 'ABC'
    },
    {
        'question': 'Which of these is a dictionary?',
        'options': ['{"a": 1, "b": 2}', '[1, 2, 3]', '(1, 2, 3)', '{1, 2, 3}'],
        'answer': '{"a": 1, "b": 2}'
    },
    {
        'question': 'What is the output of print(3 in [1, 2, 3])?',
        'options': ['True', 'False', 'None', 'Error'],
        'answer': 'True'
    },
    {
        'question': 'Which method adds an item at a specific index in a list?',
        'options': ['insert()', 'append()', 'add()', 'extend()'],
        'answer': 'insert()'
    },
    {
        'question': 'What is the output of print("hello".capitalize())?',
        'options': ['Hello', 'hello', 'HELLO', 'hELLO'],
        'answer': 'Hello'
    },
    {
        'question': 'Which function returns the absolute value?',
        'options': ['abs()', 'fabs()', 'absolute()', 'absval()'],
        'answer': 'abs()'
    },
    {
        'question': 'What is the output of print(list("abc"))?',
        'options': ['["a", "b", "c"]', '[a, b, c]', 'abc', '[abc]'],
        'answer': '["a", "b", "c"]'
    },
    {
        'question': 'Which method sorts a list in place?',
        'options': ['sort()', 'sorted()', 'order()', 'arrange()'],
        'answer': 'sort()'
    },
    {
        'question': 'What is the output of print(2 not in [1, 3, 5])?',
        'options': ['True', 'False', 'None', 'Error'],
        'answer': 'True'
    },
    {
        'question': 'Which function returns the minimum value?',
        'options': ['min()', 'max()', 'smallest()', 'minimum()'],
        'answer': 'min()'
    },
    {
        'question': 'What is the output of print("abc".replace("a", "z"))?',
        'options': ['zbc', 'azc', 'abz', 'abc'],
        'answer': 'zbc'
    },
    {
        'question': 'Which method removes all items from a list?',
        'options': ['clear()', 'remove()', 'del()', 'pop()'],
        'answer': 'clear()'
    }
]

expert_questions = [
    {
        'question': 'What is the output of print({i: i*i for i in range(2, 5)})?',
        'options': ['{2: 4, 3: 9, 4: 16}', '{1: 1, 2: 4, 3: 9, 4: 16}', '{2: 2, 3: 3, 4: 4}', '{4: 16, 3: 9, 2: 4}'],
        'answer': '{2: 4, 3: 9, 4: 16}'
    },
    {
        'question': 'Which of the following is a valid way to open a file for reading in Python?',
        'options': ["open('file.txt', 'r')", "open('file.txt', 'read')", "open('file.txt', 'w')", "open('file.txt', 'rw')"],
        'answer': "open('file.txt', 'r')"
    },
    {
        'question': 'What is the output of print(list(map(lambda x: x*2, [1, 2, 3])))?',
        'options': ['[2, 4, 6]', '[1, 2, 3, 4, 5, 6]', '[1, 4, 9]', '[2, 3, 4]'],
        'answer': '[2, 4, 6]'
    },
    {
        'question': 'What is the output of print("".join(sorted(set("banana"))))?',
        'options': ['abn', 'abnn', 'abna', 'ab'],
        'answer': 'abn'
    },
    {
        'question': 'Which built-in function returns the memory address of an object?',
        'options': ['id()', 'mem()', 'address()', 'loc()'],
        'answer': 'id()'
    },
    {
        'question': 'What is the output of print([x for x in range(5) if x % 2 == 0])?',
        'options': ['[0, 2, 4]', '[1, 3, 5]', '[2, 4, 6]', '[0, 1, 2, 3, 4]'],
        'answer': '[0, 2, 4]'
    },
    {
        'question': 'Which of the following is not a valid set operation?',
        'options': ['union()', 'intersect()', 'difference()', 'symmetric_difference()'],
        'answer': 'intersect()'
    },
    {
        'question': 'What is the output of print((lambda x: x**2)(3))?',
        'options': ['9', '6', '3', 'None'],
        'answer': '9'
    },
    {
        'question': 'Which method is used to read all lines of a file into a list?',
        'options': ['readlines()', 'read()', 'readall()', 'lines()'],
        'answer': 'readlines()'
    },
    {
        'question': 'What is the output of print([i for i in range(10) if i%3==0])?',
        'options': ['[0, 3, 6, 9]', '[3, 6, 9]', '[0, 3, 6]', '[1, 4, 7, 10]'],
        'answer': '[0, 3, 6, 9]'
    },
    {
        'question': 'What is the output of print({i: i+1 for i in range(3)})?',
        'options': ['{0: 1, 1: 2, 2: 3}', '{1: 2, 2: 3, 3: 4}', '{0: 0, 1: 1, 2: 2}', '{1: 1, 2: 2, 3: 3}'],
        'answer': '{0: 1, 1: 2, 2: 3}'
    },
    {
        'question': 'Which of these is a valid lambda function?',
        'options': ['lambda x: x+1', 'def x: x+1', 'function(x) x+1', 'lambda(x): x+1'],
        'answer': 'lambda x: x+1'
    },
    {
        'question': 'What is the output of print([i for i in range(6) if i%3==0])?',
        'options': ['[0, 3]', '[0, 3, 6]', '[3, 6]', '[0, 3, 6, 9]'],
        'answer': '[0, 3]'
    },
    {
        'question': 'Which function returns a sorted list from an iterable?',
        'options': ['sorted()', 'sort()', 'order()', 'arrange()'],
        'answer': 'sorted()'
    },
    {
        'question': 'What is the output of print("".join(sorted("cab")))?',
        'options': ['abc', 'bac', 'cab', 'bca'],
        'answer': 'abc'
    },
    {
        'question': 'Which method returns a shallow copy of a list?',
        'options': ['copy()', 'clone()', 'duplicate()', 'replicate()'],
        'answer': 'copy()'
    },
    {
        'question': 'What is the output of print([x for x in range(10) if x%4==0])?',
        'options': ['[0, 4, 8]', '[4, 8]', '[0, 4, 8, 12]', '[0, 2, 4, 6, 8]'],
        'answer': '[0, 4, 8]'
    },
    {
        'question': 'Which function returns the sum of all items in a list?',
        'options': ['sum()', 'add()', 'total()', 'summation()'],
        'answer': 'sum()'
    },
    {
        'question': 'What is the output of print("python"[::-1])?',
        'options': ['nohtyp', 'python', 'nothpy', 'htypno'],
        'answer': 'nohtyp'
    },
    {
        'question': 'Which method returns the number of occurrences of a value?',
        'options': ['count()', 'find()', 'index()', 'search()'],
        'answer': 'count()'
    },
    {
        'question': 'What is the output of print([i**2 for i in range(3, 6)])?',
        'options': ['[9, 16, 25]', '[3, 4, 5]', '[6, 9, 12]', '[1, 4, 9]'],
        'answer': '[9, 16, 25]'
    },
    {
        'question': 'Which function returns the largest integer less than or equal to a number?',
        'options': ['floor()', 'ceil()', 'int()', 'round()'],
        'answer': 'floor()'
    },
    {
        'question': 'What is the output of print({i: i**3 for i in range(2, 5)})?',
        'options': ['{2: 8, 3: 27, 4: 64}', '{2: 4, 3: 9, 4: 16}', '{1: 1, 2: 8, 3: 27}', '{3: 27, 4: 64, 5: 125}'],
        'answer': '{2: 8, 3: 27, 4: 64}'
    },
    {
        'question': 'Which method returns the index of the first occurrence of a value?',
        'options': ['index()', 'find()', 'search()', 'locate()'],
        'answer': 'index()'
    }
]

code_combat_questions = [
    {
        'question': 'What is the output of this code?\n\nx = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)',
        'options': ['[1, 2, 3, 4]', '[1, 2, 3]', '[1, 2, 3, 4, 4]', 'Error'],
        'answer': '[1, 2, 3, 4]'
    },
    {
        'question': 'What will be the output?\n\ndef func(a, b=[]):\n    b.append(a)\n    return b\n\nprint(func(1))\nprint(func(2))',
        'options': ['[1]\n[2]', '[1]\n[1, 2]', '[1, 2]\n[1, 2]', 'Error'],
        'answer': '[1]\n[1, 2]'
    },
    {
        'question': 'Predict the output:\n\nmy_list = [1, 2, 3, 4, 5]\nprint(my_list[1:3])',
        'options': ['[2, 3]', '[1, 2]', '[2, 3, 4]', '[1, 2, 3]'],
        'answer': '[2, 3]'
    },
    {
        'question': 'What is the value of `x`?\n\nx = (lambda a, b: a * b)(3, 4)',
        'options': ['12', '7', 'Error', 'None'],
        'answer': '12'
    },
    {
        'question': 'What is printed by this code?\n\nfor i in range(2):\n    print(i)\n    for j in range(3):\n        print(j)',
        'options': ['0\\n0\\n1\\n2\\n1\\n0\\n1\\n2', '0\\n1\\n2\\n0\\n1\\n2', '0\\n1\\n0\\n1\\n2\\n0\\n1\\n2', '0\\n0\\n1\\n1\\n2\\n2'],
        'answer': '0\\n0\\n1\\n2\\n1\\n0\\n1\\n2'
    },
    {
        'question': 'What is the output of:\n\nset1 = {1, 2, 3}\nset2 = {3, 4, 5}\nprint(set1.union(set2))',
        'options': ['{1, 2, 3, 4, 5}', '{1, 2, 3, 3, 4, 5}', '{1, 2, 4, 5}', '{3}'],
        'answer': '{1, 2, 3, 4, 5}'
    },
    {
        'question': 'What does this code output?\n\ndef my_func(*args):\n    return sum(args)\n\nprint(my_func(1, 2, 3, 4))',
        'options': ['10', 'Error', '1', 'None'],
        'answer': '10'
    },
    {
        'question': 'Predict the output:\n\nmy_dict = {\'a\': 1, \'b\': 2}\nprint(my_dict.get(\'c\', 3))',
        'options': ['3', 'None', 'Error', '1'],
        'answer': '3'
    },
    {
        'question': 'What is the output of this list comprehension?\n\n[x**2 for x in range(5) if x % 2 == 1]',
        'options': ['[1, 9]', '[1, 4, 9, 16]', '[1, 9, 25]', '[0, 1, 4, 9, 16]'],
        'answer': '[1, 9]'
    },
    {
        'question': 'What is the result of:\n\ntry:\n    print("try")\nexcept:\n    print("except")\nfinally:\n    print("finally")',
        'options': ['try\\nfinally', 'try', 'try\\nexcept\\nfinally', 'finally'],
        'answer': 'try\\nfinally'
    }
]

code_combat_easy = [
    {
        'question': 'What is the output of this code?\n\nx = [1, 2, 3]\nprint(len(x))',
        'options': ['3', '2', '4', 'Error'],
        'answer': '3'
    },
    {
        'question': 'Predict the output:\n\nprint("Hello" + " " + "World")',
        'options': ['Hello World', 'HelloWorld', 'Hello World', 'Error'],
        'answer': 'Hello World'
    },
    {
        'question': 'What is the value of `x`?\n\nx = 10 % 3',
        'options': ['1', '3', '0', '10'],
        'answer': '1'
    },
    {
        'question': 'What is the output of print("abc"[1])?',
        'options': ['b', 'a', 'c', 'Error'],
        'answer': 'b'
    },
    {
        'question': 'What is the output of print(2*2+2)?',
        'options': ['6', '8', '4', '2'],
        'answer': '6'
    },
    {
        'question': 'What is the output of print([i for i in range(2)])?',
        'options': ['[0, 1]', '[1, 2]', '[0, 1, 2]', '[1, 2, 3]'],
        'answer': '[0, 1]'
    },
    {
        'question': 'What is the output of print("a".upper())?',
        'options': ['A', 'a', 'Error', 'None'],
        'answer': 'A'
    },
    {
        'question': 'What is the output of print(3**2)?',
        'options': ['9', '6', '8', '12'],
        'answer': '9'
    },
    {
        'question': 'What is the output of print("hello".capitalize())?',
        'options': ['Hello', 'hello', 'HELLO', 'hELLO'],
        'answer': 'Hello'
    },
    {
        'question': 'What is the output of print(len("python"))?',
        'options': ['6', '5', '7', 'Error'],
        'answer': '6'
    },
    {
        'question': 'What is the output of print(10//3)?',
        'options': ['3', '3.33', '4', '3.0'],
        'answer': '3'
    },
    {
        'question': 'What is the output of print("a"*4)?',
        'options': ['aaaa', 'a4', '4a', 'Error'],
        'answer': 'aaaa'
    },
    {
        'question': 'What is the output of print([1,2,3][2])?',
        'options': ['3', '2', '1', 'Error'],
        'answer': '3'
    }
]

code_combat_intermediate = [
    {
        'question': 'What is the output of this code?\n\nx = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)',
        'options': ['[1, 2, 3, 4]', '[1, 2, 3]', '[1, 2, 3, 4, 4]', 'Error'],
        'answer': '[1, 2, 3, 4]'
    },
    {
        'question': 'Predict the output:\n\nmy_list = [1, 2, 3, 4, 5]\nprint(my_list[1:3])',
        'options': ['[2, 3]', '[1, 2]', '[2, 3, 4]', '[1, 2, 3]'],
        'answer': '[2, 3]'
    },
    {
        'question': 'What is the output of:\n\nset1 = {1, 2, 3}\nset2 = {3, 4, 5}\nprint(set1.intersection(set2))',
        'options': ['{3}', '{1, 2, 3, 4, 5}', '{1, 2, 4, 5}', '{}'],
        'answer': '{3}'
    },
    {
        'question': 'Predict the output:\n\nmy_dict = {\'a\': 1, \'b\': 2}\nprint(my_dict.get(\'c\', 3))',
        'options': ['3', 'None', 'Error', '1'],
        'answer': '3'
    },
    {
        'question': 'What is the output of print([i**2 for i in range(3)])?',
        'options': ['[0, 1, 4]', '[1, 4, 9]', '[0, 1, 2]', '[1, 2, 3]'],
        'answer': '[0, 1, 4]'
    },
    {
        'question': 'What is the output of print("abc".replace("a", "z"))?',
        'options': ['zbc', 'azc', 'abz', 'abc'],
        'answer': 'zbc'
    },
    {
        'question': 'What is the output of print({i: i*2 for i in range(2, 5)})?',
        'options': ['{2: 4, 3: 6, 4: 8}', '{2: 2, 3: 3, 4: 4}', '{2: 4, 3: 9, 4: 16}', '{4: 8, 3: 6, 2: 4}'],
        'answer': '{2: 4, 3: 6, 4: 8}'
    },
    {
        'question': 'What is the output of print("python"[::-1])?',
        'options': ['nohtyp', 'python', 'nothpy', 'htypno'],
        'answer': 'nohtyp'
    },
    {
        'question': 'What is the output of print([x for x in range(10) if x%3==0])?',
        'options': ['[0, 3, 6, 9]', '[3, 6, 9]', '[0, 3, 6]', '[1, 4, 7, 10]'],
        'answer': '[0, 3, 6, 9]'
    },
    {
        'question': 'What is the output of print("abc".count("a"))?',
        'options': ['1', '2', '0', '3'],
        'answer': '1'
    },
    {
        'question': 'What is the output of print([i for i in range(5) if i%2==0])?',
        'options': ['[0, 2, 4]', '[1, 3, 5]', '[2, 4, 6]', '[0, 1, 2, 3, 4]'],
        'answer': '[0, 2, 4]'
    },
    {
        'question': 'What is the output of print("python".find("t"))?',
        'options': ['2', '1', '0', '-1'],
        'answer': '2'
    },
    {
        'question': 'What is the output of print([i for i in range(6) if i%3==0])?',
        'options': ['[0, 3]', '[0, 3, 6]', '[3, 6]', '[0, 3, 6, 9]'],
        'answer': '[0, 3]'
    },
    {
        'question': 'What is the output of print("abc".isalpha())?',
        'options': ['True', 'False', 'None', 'Error'],
        'answer': 'True'
    }
]

code_combat_expert = [
    {
        'question': 'What is the output of print({i: i*i for i in range(2, 6)})?',
        'options': ['{2: 4, 3: 9, 4: 16, 5: 25}', '{2: 2, 3: 3, 4: 4, 5: 5}', '{2: 4, 3: 9, 4: 16}', '{4: 16, 3: 9, 2: 4, 5: 25}'],
        'answer': '{2: 4, 3: 9, 4: 16, 5: 25}'
    },
    {
        'question': 'What is the output of print("".join(sorted(set("banana"))))?',
        'options': ['abn', 'abnn', 'ab', 'abna'],
        'answer': 'abn'
    },
    {
        'question': 'What is the output of print([x for x in range(10) if x%4==0])?',
        'options': ['[0, 4, 8]', '[4, 8]', '[0, 4, 8, 12]', '[0, 2, 4, 6, 8]'],
        'answer': '[0, 4, 8]'
    },
    {
        'question': 'What is the output of print("python".replace("o", "a"))?',
        'options': ['pythan', 'python', 'pythona', 'pythn'],
        'answer': 'pythan'
    },
    {
        'question': 'What is the output of print([i**2 for i in range(3, 6)])?',
        'options': ['[9, 16, 25]', '[3, 4, 5]', '[6, 9, 12]', '[1, 4, 9]'],
        'answer': '[9, 16, 25]'
    },
    {
        'question': 'What is the output of print("python".count("y"))?',
        'options': ['1', '2', '0', '3'],
        'answer': '1'
    },
    {
        'question': 'What is the output of print([i for i in range(10) if i%5==0])?',
        'options': ['[0, 5]', '[5, 10]', '[0, 5, 10]', '[0, 2, 4, 6, 8]'],
        'answer': '[0, 5]'
    },
    {
        'question': 'What is the output of print("python"[1:4])?',
        'options': ['yth', 'pyt', 'tho', 'hon'],
        'answer': 'yth'
    },
    {
        'question': 'What is the output of print([i**3 for i in range(2, 5)])?',
        'options': ['[8, 27, 64]', '[2, 3, 4]', '[6, 9, 12]', '[1, 8, 27]'],
        'answer': '[8, 27, 64]'
    },
    {
        'question': 'What is the output of print("abc".find("d"))?',
        'options': ['-1', '0', '1', '2'],
        'answer': '-1'
    }
]

rapid_fire_easy_hindi = [
    {
        'question': 'Python में फ़ंक्शन को परिभाषित करने के लिए कौन सा कीवर्ड उपयोग होता है?',
        'options': ['def', 'func', 'function', 'define'],
        'answer': 'def'
    },
    {
        'question': '3 * 2 का परिणाम क्या है?',
        'options': ['6', '5', '9', '32'],
        'answer': '6'
    },
    {
        'question': 'कौन सा डेटा टाइप अपरिवर्तनीय (immutable) है?',
        'options': ['ट्यूपल', 'सूची', 'डिक्शनरी', 'सेट'],
        'answer': 'ट्यूपल'
    },
    {
        'question': 'What does `//` operator do?',
        'options': ['Floor Division', 'Division', 'Exponent', 'Modulo'],
        'answer': 'Floor Division'
    },
    {
        'question': 'How do you create a variable `x` with value 5?',
        'options': ['x = 5', 'x == 5', 'let x = 5', 'var x = 5'],
        'answer': 'x = 5'
    },
    {
        'question': 'What is the output of print(1+1)?',
        'options': ['2', '11', '1', '0'],
        'answer': '2'
    },
    {
        'question': 'Which function is used to get user input?',
        'options': ['input()', 'scan()', 'get()', 'read()'],
        'answer': 'input()'
    },
    {
        'question': 'What is the output of print("A"*2)?',
        'options': ['AA', 'A2', '2A', 'Error'],
        'answer': 'AA'
    },
    {
        'question': 'Which operator is used for subtraction?',
        'options': ['-', '+', '*', '/'],
        'answer': '-'
    },
    {
        'question': 'What is the output of print(6//2)?',
        'options': ['3', '2', '1', '0'],
        'answer': '3'
    },
    {
        'question': 'Which of these is a string?',
        'options': ['"hello"', '123', '[1,2,3]', 'True'],
        'answer': '"hello"'
    },
    {
        'question': 'What is the output of print(2*3)?',
        'options': ['6', '5', '23', '8'],
        'answer': '6'
    },
    {
        'question': 'Which function returns the type of an object?',
        'options': ['type()', 'typeof()', 'kind()', 'class()'],
        'answer': 'type()'
    },
    {
        'question': 'What is the output of print(9-4)?',
        'options': ['5', '13', '4', '9'],
        'answer': '5'
    },
    {
        'question': 'Which of these is a boolean value?',
        'options': ['True', '1', '"True"', 'None'],
        'answer': 'True'
    }
]

rapid_fire_intermediate_hindi = [
    {
        'question': 'print([i+1 for i in range(3)]) का आउटपुट क्या होगा?',
        'options': ['[1, 2, 3]', '[0, 1, 2]', '[2, 3, 4]', '[1, 3, 5]'],
        'answer': '[1, 2, 3]'
    },
    {
        'question': 'सूची का अंतिम आइटम प्राप्त करने के लिए कौन सी विधि उपयोग होती है?',
        'options': ['pop()', 'remove()', 'last()', 'end()'],
        'answer': 'pop()'
    },
    {
        'question': 'print("abc".lower()) का आउटपुट क्या होगा?',
        'options': ['abc', 'ABC', 'Abc', 'aBc'],
        'answer': 'abc'
    },
    {
        'question': 'Which of these is a tuple?',
        'options': ['(1, 2, 3)', '[1, 2, 3]', '{1, 2, 3}', 'tuple(1,2,3)'],
        'answer': '(1, 2, 3)'
    },
    {
        'question': 'What is the output of print(2 in [1, 2, 3])?',
        'options': ['True', 'False', 'None', 'Error'],
        'answer': 'True'
    },
    {
        'question': 'Which method adds an item to the end of a list?',
        'options': ['append()', 'add()', 'insert()', 'extend()'],
        'answer': 'append()'
    },
    {
        'question': 'What is the output of print("hello".title())?',
        'options': ['Hello', 'hello', 'HELLO', 'hELLO'],
        'answer': 'Hello'
    },
    {
        'question': 'Which function returns the maximum value?',
        'options': ['max()', 'min()', 'largest()', 'maximum()'],
        'answer': 'max()'
    },
    {
        'question': 'What is the output of print(list("xyz"))?',
        'options': ['["x", "y", "z"]', '[x, y, z]', 'xyz', '[xyz]'],
        'answer': '["x", "y", "z"]'
    },
    {
        'question': 'Which method reverses a list in place?',
        'options': ['reverse()', 'reversed()', 'flip()', 'invert()'],
        'answer': 'reverse()'
    }
]

rapid_fire_expert_hindi = [
    {
        'question': 'print({i: i*2 for i in range(2, 5)}) का आउटपुट क्या होगा?',
        'options': ['{2: 4, 3: 6, 4: 8}', '{2: 2, 3: 3, 4: 4}', '{2: 4, 3: 9, 4: 16}', '{4: 8, 3: 6, 2: 4}'],
        'answer': '{2: 4, 3: 6, 4: 8}'
    },
    {
        'question': 'इनमें से कौन सा वैध जनरेटर एक्सप्रेशन है?',
        'options': ['(x*x for x in range(3))', '[x*x for x in range(3)]', '{x*x for x in range(3)}', 'generator(x*x for x in range(3))'],
        'answer': '(x*x for x in range(3))'
    },
    {
        'question': 'print([i for i in range(7) if i%2==1]) का आउटपुट क्या होगा?',
        'options': ['[1, 3, 5]', '[0, 2, 4, 6]', '[2, 4, 6]', '[1, 2, 3, 4, 5]'],
        'answer': '[1, 3, 5]'
    },
    {
        'question': 'Which function returns the ceiling of a number?',
        'options': ['ceil()', 'floor()', 'int()', 'round()'],
        'answer': 'ceil()'
    },
    {
        'question': 'What is the output of print("python".count("o"))?',
        'options': ['1', '2', '0', '3'],
        'answer': '1'
    },
    {
        'question': 'Which method returns a deep copy of a list?',
        'options': ['copy.deepcopy()', 'copy()', 'clone()', 'replicate()'],
        'answer': 'copy.deepcopy()'
    },
    {
        'question': 'What is the output of print([x for x in range(10) if x%5==0])?',
        'options': ['[0, 5]', '[5, 10]', '[0, 5, 10]', '[0, 2, 4, 6, 8]'],
        'answer': '[0, 5]'
    },
    {
        'question': 'What is the output of print("python"[1:4])?',
        'options': ['yth', 'pyt', 'tho', 'hon'],
        'answer': 'yth'
    },
    {
        'question': 'Which method returns the number of items in a dictionary?',
        'options': ['len()', 'count()', 'size()', 'length()'],
        'answer': 'len()'
    }
]

code_combat_easy_hindi = [
    {
        'question': 'इस कोड का आउटपुट क्या होगा?\nx = [1, 2, 3]\nprint(len(x))',
        'options': ['3', '2', '4', 'त्रुटि'],
        'answer': '3'
    },
    {
        'question': 'आउटपुट का अनुमान लगाएँ:\nprint("Hello" + " " + "World")',
        'options': ['Hello World', 'HelloWorld', 'Hello World', 'त्रुटि'],
        'answer': 'Hello World'
    },
    {
        'question': '`x` का मान क्या होगा?\nx = 10 % 3',
        'options': ['1', '3', '0', '10'],
        'answer': '1'
    },
    {
        'question': 'What is the output of print("abc"[1])?',
        'options': ['b', 'a', 'c', 'Error'],
        'answer': 'b'
    },
    {
        'question': 'What is the output of print(2*2+2)?',
        'options': ['6', '8', '4', '2'],
        'answer': '6'
    },
    {
        'question': 'What is the output of print([i for i in range(2)])?',
        'options': ['[0, 1]', '[1, 2]', '[0, 1, 2]', '[1, 2, 3]'],
        'answer': '[0, 1]'
    },
    {
        'question': 'What is the output of print("a".upper())?',
        'options': ['A', 'a', 'Error', 'None'],
        'answer': 'A'
    },
    {
        'question': 'What is the output of print(3**2)?',
        'options': ['9', '6', '8', '12'],
        'answer': '9'
    },
    {
        'question': 'What is the output of print("hello".capitalize())?',
        'options': ['Hello', 'hello', 'HELLO', 'hELLO'],
        'answer': 'Hello'
    },
    {
        'question': 'What is the output of print(len("python"))?',
        'options': ['6', '5', '7', 'Error'],
        'answer': '6'
    },
    {
        'question': 'What is the output of print(10//3)?',
        'options': ['3', '3.33', '4', '3.0'],
        'answer': '3'
    },
    {
        'question': 'What is the output of print("a"*4)?',
        'options': ['aaaa', 'a4', '4a', 'Error'],
        'answer': 'aaaa'
    },
    {
        'question': 'What is the output of print([1,2,3][2])?',
        'options': ['3', '2', '1', 'Error'],
        'answer': '3'
    }
]

code_combat_intermediate_hindi = [
    {
        'question': 'इस कोड का आउटपुट क्या होगा?\nx = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)',
        'options': ['[1, 2, 3, 4]', '[1, 2, 3]', '[1, 2, 3, 4, 4]', 'त्रुटि'],
        'answer': '[1, 2, 3, 4]'
    },
    {
        'question': 'आउटपुट का अनुमान लगाएँ:\nmy_list = [1, 2, 3, 4, 5]\nprint(my_list[1:3])',
        'options': ['[2, 3]', '[1, 2]', '[2, 3, 4]', '[1, 2, 3]'],
        'answer': '[2, 3]'
    },
    {
        'question': 'इस कोड का आउटपुट क्या होगा?\nset1 = {1, 2, 3}\nset2 = {3, 4, 5}\nprint(set1.intersection(set2))',
        'options': ['{3}', '{1, 2, 3, 4, 5}', '{1, 2, 4, 5}', '{}'],
        'answer': '{3}'
    },
    {
        'question': 'Predict the output:\n\nmy_dict = {\'a\': 1, \'b\': 2}\nprint(my_dict.get(\'c\', 3))',
        'options': ['3', 'None', 'Error', '1'],
        'answer': '3'
    },
    {
        'question': 'What is the output of print([i**2 for i in range(3)])?',
        'options': ['[0, 1, 4]', '[1, 4, 9]', '[0, 1, 2]', '[1, 2, 3]'],
        'answer': '[0, 1, 4]'
    },
    {
        'question': 'What is the output of print("abc".replace("a", "z"))?',
        'options': ['zbc', 'azc', 'abz', 'abc'],
        'answer': 'zbc'
    },
    {
        'question': 'What is the output of print({i: i*2 for i in range(2, 5)})?',
        'options': ['{2: 4, 3: 6, 4: 8}', '{2: 2, 3: 3, 4: 4}', '{2: 4, 3: 9, 4: 16}', '{4: 8, 3: 6, 2: 4}'],
        'answer': '{2: 4, 3: 6, 4: 8}'
    },
    {
        'question': 'What is the output of print("python"[::-1])?',
        'options': ['nohtyp', 'python', 'nothpy', 'htypno'],
        'answer': 'nohtyp'
    },
    {
        'question': 'What is the output of print([x for x in range(10) if x%3==0])?',
        'options': ['[0, 3, 6, 9]', '[3, 6, 9]', '[0, 3, 6]', '[1, 4, 7, 10]'],
        'answer': '[0, 3, 6, 9]'
    },
    {
        'question': 'What is the output of print("abc".count("a"))?',
        'options': ['1', '2', '0', '3'],
        'answer': '1'
    },
    {
        'question': 'What is the output of print([i for i in range(5) if i%2==0])?',
        'options': ['[0, 2, 4]', '[1, 3, 5]', '[2, 4, 6]', '[0, 1, 2, 3, 4]'],
        'answer': '[0, 2, 4]'
    },
    {
        'question': 'What is the output of print("python".find("t"))?',
        'options': ['2', '1', '0', '-1'],
        'answer': '2'
    },
    {
        'question': 'What is the output of print([i for i in range(6) if i%3==0])?',
        'options': ['[0, 3]', '[0, 3, 6]', '[3, 6]', '[0, 3, 6, 9]'],
        'answer': '[0, 3]'
    },
    {
        'question': 'What is the output of print("abc".isalpha())?',
        'options': ['True', 'False', 'None', 'Error'],
        'answer': 'True'
    }
]

code_combat_expert_hindi = [
    {
        'question': 'print({i: i*i for i in range(2, 6)}) का आउटपुट क्या होगा?',
        'options': ['{2: 4, 3: 9, 4: 16, 5: 25}', '{2: 2, 3: 3, 4: 4, 5: 5}', '{2: 4, 3: 9, 4: 16}', '{4: 16, 3: 9, 2: 4, 5: 25}'],
        'answer': '{2: 4, 3: 9, 4: 16, 5: 25}'
    },
    {
        'question': 'print("".join(sorted(set("banana")))) का आउटपुट क्या होगा?',
        'options': ['abn', 'abnn', 'ab', 'abna'],
        'answer': 'abn'
    },
    {
        'question': 'print([x for x in range(10) if x%4==0]) का आउटपुट क्या होगा?',
        'options': ['[0, 4, 8]', '[4, 8]', '[0, 4, 8, 12]', '[0, 2, 4, 6, 8]'],
        'answer': '[0, 4, 8]'
    },
    {
        'question': 'What is the output of print("python".replace("o", "a"))?',
        'options': ['pythan', 'python', 'pythona', 'pythn'],
        'answer': 'pythan'
    },
    {
        'question': 'What is the output of print([i**2 for i in range(3, 6)])?',
        'options': ['[9, 16, 25]', '[3, 4, 5]', '[6, 9, 12]', '[1, 4, 9]'],
        'answer': '[9, 16, 25]'
    },
    {
        'question': 'What is the output of print("python".count("y"))?',
        'options': ['1', '2', '0', '3'],
        'answer': '1'
    },
    {
        'question': 'What is the output of print([i for i in range(10) if i%5==0])?',
        'options': ['[0, 5]', '[5, 10]', '[0, 5, 10]', '[0, 2, 4, 6, 8]'],
        'answer': '[0, 5]'
    },
    {
        'question': 'What is the output of print("python"[1:4])?',
        'options': ['yth', 'pyt', 'tho', 'hon'],
        'answer': 'yth'
    },
    {
        'question': 'What is the output of print([i**3 for i in range(2, 5)])?',
        'options': ['[8, 27, 64]', '[2, 3, 4]', '[6, 9, 12]', '[1, 8, 27]'],
        'answer': '[8, 27, 64]'
    },
    {
        'question': 'What is the output of print("abc".find("d"))?',
        'options': ['-1', '0', '1', '2'],
        'answer': '-1'
    }
]

# --- Hindi Classic Pools ---
easy_questions_hindi = [
    {
        'question': 'print(2 + 3) का आउटपुट क्या होगा?',
        'options': ['5', '6', '23', 'त्रुटि'],
        'answer': '5'
    },
    {
        'question': 'Python में एकल पंक्ति की टिप्पणी के लिए कौन सा चिन्ह उपयोग होता है?',
        'options': ['#', '//', '--', '/*'],
        'answer': '#'
    },
    {
        'question': 'Python फ़ाइलों के लिए सही एक्सटेंशन क्या है?',
        'options': ['.py', '.python', '.pt', '.pyt'],
        'answer': '.py'
    },
    {
        'question': 'Which function is used to get input from the user?',
        'options': ['input()', 'scan()', 'get()', 'read()'],
        'answer': 'input()'
    },
    {
        'question': 'What is the output of print(10 // 3)?',
        'options': ['3.33', '3', '4', '3.0'],
        'answer': '3'
    },
    {
        'question': 'Which of these is a valid variable name in Python?',
        'options': ['2var', 'var_2', 'var-2', 'var 2'],
        'answer': 'var_2'
    },
    {
        'question': 'How do you start a function in Python?',
        'options': ['def', 'function', 'fun', 'define'],
        'answer': 'def'
    },
    {
        'question': 'What is the output of print(type([]))?',
        'options': ["<class 'list'>", "<class 'dict'>", "<class 'tuple'>", "<class 'set'>"],
        'answer': "<class 'list'>"
    },
    {
        'question': 'Which of the following is not a Python data type?',
        'options': ['list', 'set', 'array', 'tuple'],
        'answer': 'array'
    },
    {
        'question': 'What does the len() function do?',
        'options': ['Returns the length of an object', 'Returns the type of an object', 'Returns the value of an object', 'Returns the id of an object'],
        'answer': 'Returns the length of an object'
    },
    {
        'question': 'What is the output of print(5 + 7)?',
        'options': ['12', '57', '2', '13'],
        'answer': '12'
    },
    {
        'question': 'Which function is used to display output in Python?',
        'options': ['print()', 'output()', 'echo()', 'display()'],
        'answer': 'print()'
    },
    {
        'question': 'What is the output of print("Python"[0])?',
        'options': ['P', 'y', 'n', 'o'],
        'answer': 'P'
    },
    {
        'question': 'Which of these is a Python keyword?',
        'options': ['for', 'loop', 'repeat', 'iterate'],
        'answer': 'for'
    },
    {
        'question': 'What is the output of print(2 ** 3)?',
        'options': ['8', '6', '9', '5'],
        'answer': '8'
    },
    {
        'question': 'Which operator is used for addition?',
        'options': ['+', '-', '*', '/'],
        'answer': '+'
    },
    {
        'question': 'What is the output of print(10 % 3)?',
        'options': ['1', '3', '0', '10'],
        'answer': '1'
    },
    {
        'question': 'Which of these is a valid list?',
        'options': ['[1, 2, 3]', '(1, 2, 3)', '{1, 2, 3}', 'list(1,2,3)'],
        'answer': '[1, 2, 3]'
    },
    {
        'question': 'What is the output of print("a" * 3)?',
        'options': ['aaa', 'a3', 'Error', '3a'],
        'answer': 'aaa'
    },
    {
        'question': 'Which function returns the length of a list?',
        'options': ['len()', 'count()', 'size()', 'length()'],
        'answer': 'len()'
    },
    {
        'question': 'What is the output of print(4 // 2)?',
        'options': ['2', '2.0', '0', '1'],
        'answer': '2'
    },
    {
        'question': 'Which of these is a comment in Python?',
        'options': ['# comment', '// comment', '-- comment', '/* comment */'],
        'answer': '# comment'
    },
    {
        'question': 'What is the output of print(7 - 2)?',
        'options': ['5', '9', '2', '7'],
        'answer': '5'
    },
    {
        'question': 'Which function converts a string to an integer?',
        'options': ['int()', 'str()', 'float()', 'chr()'],
        'answer': 'int()'
    }
]

intermediate_questions_hindi = [
    {
        'question': 'print([i for i in range(3)]) का आउटपुट क्या होगा?',
        'options': ['[0, 1, 2]', '[1, 2, 3]', '[0, 1, 2, 3]', '[1, 2]'],
        'answer': '[0, 1, 2]'
    },
    {
        'question': 'सूची में एक आइटम जोड़ने के लिए कौन सी विधि उपयोग होती है?',
        'options': ['add()', 'append()', 'insert()', 'push()'],
        'answer': 'append()'
    },
    {
        'question': 'print(type({})) का आउटपुट क्या होगा?',
        'options': ["<class 'dict'>", "<class 'set'>", "<class 'list'>", "<class 'tuple'>"],
        'answer': "<class 'dict'>"
    },
    {
        'question': 'Python में for लूप कैसे शुरू करते हैं?',
        'options': ['for i in range(5):', 'for(i=0;i<5;i++)', 'foreach i in range(5)', 'loop i in range(5)'],
        'answer': 'for i in range(5):'
    },
    {
        'question': 'घात (exponentiation) के लिए कौन सा ऑपरेटर उपयोग होता है?',
        'options': ['^', '**', 'exp()', '^^'],
        'answer': '**'
    },
    {
        'question': 'print("Hello"[1]) का आउटपुट क्या होगा?',
        'options': ['H', 'e', 'l', 'o'],
        'answer': 'e'
    },
    {
        'question': 'math मॉड्यूल को कैसे इम्पोर्ट करते हैं?',
        'options': ['import math', 'include math', 'using math', 'require math'],
        'answer': 'import math'
    },
    {
        'question': 'सूची से अंतिम आइटम हटाने के लिए कौन सी विधि है?',
        'options': ['remove()', 'pop()', 'delete()', 'discard()'],
        'answer': 'pop()'
    },
    {
        'question': 'print(5 != 3) का आउटपुट क्या होगा?',
        'options': ['True', 'False', 'None', 'Error'],
        'answer': 'True'
    },
    {
        'question': 'निम्नलिखित में से कौन सा ट्यूपल (tuple) है?',
        'options': ['(1, 2, 3)', '[1, 2, 3]', '{1, 2, 3}', 'tuple[1, 2, 3]'],
        'answer': '(1, 2, 3)'
    },
    {
        'question': 'print([i*2 for i in range(3)]) का आउटपुट क्या होगा?',
        'options': ['[0, 2, 4]', '[2, 4, 6]', '[1, 2, 3]', '[0, 1, 2]'],
        'answer': '[0, 2, 4]'
    },
    {
        'question': 'सूची में किसी आइटम का इंडेक्स प्राप्त करने के लिए कौन सी विधि है?',
        'options': ['index()', 'find()', 'locate()', 'position()'],
        'answer': 'index()'
    },
    {
        'question': 'print("abc".upper()) का आउटपुट क्या होगा?',
        'options': ['ABC', 'abc', 'Abc', 'aBc'],
        'answer': 'ABC'
    },
    {
        'question': 'निम्नलिखित में से कौन सा डिक्शनरी (dictionary) है?',
        'options': ['{"a": 1, "b": 2}', '[1, 2, 3]', '(1, 2, 3)', '{1, 2, 3}'],
        'answer': '{"a": 1, "b": 2}'
    },
    {
        'question': 'print(3 in [1, 2, 3]) का आउटपुट क्या होगा?',
        'options': ['True', 'False', 'None', 'Error'],
        'answer': 'True'
    },
    {
        'question': 'print([i**3 for i in range(2, 5)]) का आउटपुट क्या होगा?',
        'options': ['[8, 27, 64]', '[2, 3, 4]', '[6, 9, 12]', '[1, 8, 27]'],
        'answer': '[8, 27, 64]'
    },
    {
        'question': 'print("abc".find("d")) का आउटपुट क्या होगा?',
        'options': ['-1', '0', '1', '2'],
        'answer': '-1'
    }
]

expert_questions_hindi = [
    {
        'question': 'print({i: i*i for i in range(2, 5)}) का आउटपुट क्या होगा?',
        'options': ['{2: 4, 3: 9, 4: 16}', '{1: 1, 2: 4, 3: 9, 4: 16}', '{2: 2, 3: 3, 4: 4}', '{4: 16, 3: 9, 2: 4}'],
        'answer': '{2: 4, 3: 9, 4: 16}'
    },
    {
        'question': 'Python में फ़ाइल पढ़ने के लिए कौन सा तरीका सही है?',
        'options': ["open('file.txt', 'r')", "open('file.txt', 'read')", "open('file.txt', 'w')", "open('file.txt', 'rw')"],
        'answer': "open('file.txt', 'r')"
    },
    {
        'question': 'print(list(map(lambda x: x*2, [1, 2, 3]))) का आउटपुट क्या होगा?',
        'options': ['[2, 4, 6]', '[1, 2, 3, 4, 5, 6]', '[1, 4, 9]', '[2, 3, 4]'],
        'answer': '[2, 4, 6]'
    },
    {
        'question': 'print("".join(sorted(set("banana")))) का आउटपुट क्या होगा?',
        'options': ['abn', 'abnn', 'abna', 'ab'],
        'answer': 'abn'
    },
    {
        'question': 'कौन सा बिल्ट-इन फ़ंक्शन किसी ऑब्जेक्ट का मेमोरी एड्रेस देता है?',
        'options': ['id()', 'mem()', 'address()', 'loc()'],
        'answer': 'id()'
    },
    {
        'question': 'print([x for x in range(5) if x % 2 == 0]) का आउटपुट क्या होगा?',
        'options': ['[0, 2, 4]', '[1, 3, 5]', '[2, 4, 6]', '[0, 1, 2, 3, 4]'],
        'answer': '[0, 2, 4]'
    },
    {
        'question': 'निम्नलिखित में से कौन सा वैध सेट ऑपरेशन नहीं है?',
        'options': ['union()', 'intersect()', 'difference()', 'symmetric_difference()'],
        'answer': 'intersect()'
    },
    {
        'question': 'print((lambda x: x**2)(3)) का आउटपुट क्या होगा?',
        'options': ['9', '6', '3', 'None'],
        'answer': '9'
    },
    {
        'question': 'फ़ाइल की सभी पंक्तियाँ सूची में पढ़ने के लिए कौन सी विधि है?',
        'options': ['readlines()', 'read()', 'readall()', 'lines()'],
        'answer': 'readlines()'
    },
    {
        'question': 'print([i for i in range(10) if i%3==0]) का आउटपुट क्या होगा?',
        'options': ['[0, 3, 6, 9]', '[3, 6, 9]', '[0, 3, 6]', '[1, 4, 7, 10]'],
        'answer': '[0, 3, 6, 9]'
    },
    {
        'question': 'print({i: i+1 for i in range(3)}) का आउटपुट क्या होगा?',
        'options': ['{0: 1, 1: 2, 2: 3}', '{1: 2, 2: 3, 3: 4}', '{0: 0, 1: 1, 2: 2}', '{1: 1, 2: 2, 3: 3}'],
        'answer': '{0: 1, 1: 2, 2: 3}'
    },
    {
        'question': 'निम्नलिखित में से कौन सा वैध lambda फ़ंक्शन है?',
        'options': ['lambda x: x+1', 'def x: x+1', 'function(x) x+1', 'lambda(x): x+1'],
        'answer': 'lambda x: x+1'
    },
    {
        'question': 'print([i for i in range(6) if i%3==0]) का आउटपुट क्या होगा?',
        'options': ['[0, 3]', '[0, 3, 6]', '[3, 6]', '[0, 3, 6, 9]'],
        'answer': '[0, 3]'
    },
    {
        'question': 'कौन सा फ़ंक्शन iterable से sorted सूची लौटाता है?',
        'options': ['sorted()', 'sort()', 'order()', 'arrange()'],
        'answer': 'sorted()'
    },
    {
        'question': 'print("".join(sorted("cab"))) का आउटपुट क्या होगा?',
        'options': ['abc', 'bac', 'cab', 'bca'],
        'answer': 'abc'
    },
    {
        'question': 'सूची की शैलो कॉपी प्राप्त करने के लिए कौन सी विधि है?',
        'options': ['copy()', 'clone()', 'duplicate()', 'replicate()'],
        'answer': 'copy()'
    },
    {
        'question': 'print([x for x in range(10) if x%4==0]) का आउटपुट क्या होगा?',
        'options': ['[0, 4, 8]', '[4, 8]', '[0, 4, 8, 12]', '[0, 2, 4, 6, 8]'],
        'answer': '[0, 4, 8]'
    },
    {
        'question': 'सूची के सभी आइटम का योग प्राप्त करने के लिए कौन सा फ़ंक्शन है?',
        'options': ['sum()', 'add()', 'total()', 'summation()'],
        'answer': 'sum()'
    },
    {
        'question': 'print("python"[::-1]) का आउटपुट क्या होगा?',
        'options': ['nohtyp', 'python', 'nothpy', 'htypno'],
        'answer': 'nohtyp'
    },
    {
        'question': 'सूची में किसी मान के occurrences प्राप्त करने के लिए कौन सी विधि है?',
        'options': ['count()', 'find()', 'index()', 'search()'],
        'answer': 'count()'
    },
    {
        'question': 'print([i**2 for i in range(3, 6)]) का आउटपुट क्या होगा?',
        'options': ['[9, 16, 25]', '[3, 4, 5]', '[6, 9, 12]', '[1, 4, 9]'],
        'answer': '[9, 16, 25]'
    },
    {
        'question': 'कौन सा फ़ंक्शन किसी संख्या से कम या बराबर सबसे बड़ा पूर्णांक लौटाता है?',
        'options': ['floor()', 'ceil()', 'int()', 'round()'],
        'answer': 'floor()'
    },
    {
        'question': 'print({i: i**3 for i in range(2, 5)}) का आउटपुट क्या होगा?',
        'options': ['{2: 8, 3: 27, 4: 64}', '{2: 4, 3: 9, 4: 16}', '{1: 1, 2: 8, 3: 27}', '{3: 27, 4: 64, 5: 125}'],
        'answer': '{2: 8, 3: 27, 4: 64}'
    },
    {
        'question': 'सूची में किसी मान की पहली occurrence का इंडेक्स प्राप्त करने के लिए कौन सी विधि है?',
        'options': ['index()', 'find()', 'search()', 'locate()'],
        'answer': 'index()'
    }
]

code_combat_questions = [
    {
        'question': 'What is the output of this code?\n\nx = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)',
        'options': ['[1, 2, 3, 4]', '[1, 2, 3]', '[1, 2, 3, 4, 4]', 'Error'],
        'answer': '[1, 2, 3, 4]'
    },
    {
        'question': 'What will be the output?\n\ndef func(a, b=[]):\n    b.append(a)\n    return b\n\nprint(func(1))\nprint(func(2))',
        'options': ['[1]\n[2]', '[1]\n[1, 2]', '[1, 2]\n[1, 2]', 'Error'],
        'answer': '[1]\n[1, 2]'
    },
    {
        'question': 'Predict the output:\n\nmy_list = [1, 2, 3, 4, 5]\nprint(my_list[1:3])',
        'options': ['[2, 3]', '[1, 2]', '[2, 3, 4]', '[1, 2, 3]'],
        'answer': '[2, 3]'
    },
    {
        'question': 'What is the value of `x`?\n\nx = (lambda a, b: a * b)(3, 4)',
        'options': ['12', '7', 'Error', 'None'],
        'answer': '12'
    },
    {
        'question': 'What is printed by this code?\n\nfor i in range(2):\n    print(i)\n    for j in range(3):\n        print(j)',
        'options': ['0\\n0\\n1\\n2\\n1\\n0\\n1\\n2', '0\\n1\\n2\\n0\\n1\\n2', '0\\n1\\n0\\n1\\n2\\n0\\n1\\n2', '0\\n0\\n1\\n1\\n2\\n2'],
        'answer': '0\\n0\\n1\\n2\\n1\\n0\\n1\\n2'
    },
    {
        'question': 'What is the output of:\n\nset1 = {1, 2, 3}\nset2 = {3, 4, 5}\nprint(set1.union(set2))',
        'options': ['{1, 2, 3, 4, 5}', '{1, 2, 3, 3, 4, 5}', '{1, 2, 4, 5}', '{3}'],
        'answer': '{1, 2, 3, 4, 5}'
    },
    {
        'question': 'What does this code output?\n\ndef my_func(*args):\n    return sum(args)\n\nprint(my_func(1, 2, 3, 4))',
        'options': ['10', 'Error', '1', 'None'],
        'answer': '10'
    },
    {
        'question': 'Predict the output:\n\nmy_dict = {\'a\': 1, \'b\': 2}\nprint(my_dict.get(\'c\', 3))',
        'options': ['3', 'None', 'Error', '1'],
        'answer': '3'
    },
    {
        'question': 'What is the output of this list comprehension?\n\n[x**2 for x in range(5) if x % 2 == 1]',
        'options': ['[1, 9]', '[1, 4, 9, 16]', '[1, 9, 25]', '[0, 1, 4, 9, 16]'],
        'answer': '[1, 9]'
    },
    {
        'question': 'What is the result of:\n\ntry:\n    print("try")\nexcept:\n    print("except")\nfinally:\n    print("finally")',
        'options': ['try\\nfinally', 'try', 'try\\nexcept\\nfinally', 'finally'],
        'answer': 'try\\nfinally'
    }
]

code_combat_easy = [
    {
        'question': 'What is the output of this code?\n\nx = [1, 2, 3]\nprint(len(x))',
        'options': ['3', '2', '4', 'Error'],
        'answer': '3'
    },
    {
        'question': 'Predict the output:\n\nprint("Hello" + " " + "World")',
        'options': ['Hello World', 'HelloWorld', 'Hello World', 'Error'],
        'answer': 'Hello World'
    },
    {
        'question': 'What is the value of `x`?\n\nx = 10 % 3',
        'options': ['1', '3', '0', '10'],
        'answer': '1'
    },
    {
        'question': 'What is the output of print("abc"[1])?',
        'options': ['b', 'a', 'c', 'Error'],
        'answer': 'b'
    },
    {
        'question': 'What is the output of print(2*2+2)?',
        'options': ['6', '8', '4', '2'],
        'answer': '6'
    },
    {
        'question': 'What is the output of print([i for i in range(2)])?',
        'options': ['[0, 1]', '[1, 2]', '[0, 1, 2]', '[1, 2, 3]'],
        'answer': '[0, 1]'
    },
    {
        'question': 'What is the output of print("a".upper())?',
        'options': ['A', 'a', 'Error', 'None'],
        'answer': 'A'
    },
    {
        'question': 'What is the output of print(3**2)?',
        'options': ['9', '6', '8', '12'],
        'answer': '9'
    },
    {
        'question': 'What is the output of print("hello".capitalize())?',
        'options': ['Hello', 'hello', 'HELLO', 'hELLO'],
        'answer': 'Hello'
    },
    {
        'question': 'What is the output of print(len("python"))?',
        'options': ['6', '5', '7', 'Error'],
        'answer': '6'
    },
    {
        'question': 'What is the output of print(10//3)?',
        'options': ['3', '3.33', '4', '3.0'],
        'answer': '3'
    },
    {
        'question': 'What is the output of print("a"*4)?',
        'options': ['aaaa', 'a4', '4a', 'Error'],
        'answer': 'aaaa'
    },
    {
        'question': 'What is the output of print([1,2,3][2])?',
        'options': ['3', '2', '1', 'Error'],
        'answer': '3'
    }
]

code_combat_intermediate = [
    {
        'question': 'What is the output of this code?\n\nx = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)',
        'options': ['[1, 2, 3, 4]', '[1, 2, 3]', '[1, 2, 3, 4, 4]', 'Error'],
        'answer': '[1, 2, 3, 4]'
    },
    {
        'question': 'Predict the output:\n\nmy_list = [1, 2, 3, 4, 5]\nprint(my_list[1:3])',
        'options': ['[2, 3]', '[1, 2]', '[2, 3, 4]', '[1, 2, 3]'],
        'answer': '[2, 3]'
    },
    {
        'question': 'What is the output of:\n\nset1 = {1, 2, 3}\nset2 = {3, 4, 5}\nprint(set1.intersection(set2))',
        'options': ['{3}', '{1, 2, 3, 4, 5}', '{1, 2, 4, 5}', '{}'],
        'answer': '{3}'
    },
    {
        'question': 'Predict the output:\n\nmy_dict = {\'a\': 1, \'b\': 2}\nprint(my_dict.get(\'c\', 3))',
        'options': ['3', 'None', 'Error', '1'],
        'answer': '3'
    },
    {
        'question': 'What is the output of print([i**2 for i in range(3)])?',
        'options': ['[0, 1, 4]', '[1, 4, 9]', '[0, 1, 2]', '[1, 2, 3]'],
        'answer': '[0, 1, 4]'
    },
    {
        'question': 'What is the output of print("abc".replace("a", "z"))?',
        'options': ['zbc', 'azc', 'abz', 'abc'],
        'answer': 'zbc'
    },
    {
        'question': 'What is the output of print({i: i*2 for i in range(2, 5)})?',
        'options': ['{2: 4, 3: 6, 4: 8}', '{2: 2, 3: 3, 4: 4}', '{2: 4, 3: 9, 4: 16}', '{4: 8, 3: 6, 2: 4}'],
        'answer': '{2: 4, 3: 6, 4: 8}'
    },
    {
        'question': 'What is the output of print("python"[::-1])?',
        'options': ['nohtyp', 'python', 'nothpy', 'htypno'],
        'answer': 'nohtyp'
    },
    {
        'question': 'What is the output of print([x for x in range(10) if x%3==0])?',
        'options': ['[0, 3, 6, 9]', '[3, 6, 9]', '[0, 3, 6]', '[1, 4, 7, 10]'],
        'answer': '[0, 3, 6, 9]'
    },
    {
        'question': 'What is the output of print("abc".count("a"))?',
        'options': ['1', '2', '0', '3'],
        'answer': '1'
    },
    {
        'question': 'What is the output of print([i for i in range(5) if i%2==0])?',
        'options': ['[0, 2, 4]', '[1, 3, 5]', '[2, 4, 6]', '[0, 1, 2, 3, 4]'],
        'answer': '[0, 2, 4]'
    },
    {
        'question': 'What is the output of print("python".find("t"))?',
        'options': ['2', '1', '0', '-1'],
        'answer': '2'
    },
    {
        'question': 'What is the output of print([i for i in range(6) if i%3==0])?',
        'options': ['[0, 3]', '[0, 3, 6]', '[3, 6]', '[0, 3, 6, 9]'],
        'answer': '[0, 3]'
    },
    {
        'question': 'What is the output of print("abc".isalpha())?',
        'options': ['True', 'False', 'None', 'Error'],
        'answer': 'True'
    }
]

code_combat_expert = [
    {
        'question': 'What is the output of print({i: i*i for i in range(2, 6)})?',
        'options': ['{2: 4, 3: 9, 4: 16, 5: 25}', '{2: 2, 3: 3, 4: 4, 5: 5}', '{2: 4, 3: 9, 4: 16}', '{4: 16, 3: 9, 2: 4, 5: 25}'],
        'answer': '{2: 4, 3: 9, 4: 16, 5: 25}'
    },
    {
        'question': 'What is the output of print("".join(sorted(set("banana"))))?',
        'options': ['abn', 'abnn', 'ab', 'abna'],
        'answer': 'abn'
    },
    {
        'question': 'What is the output of print([x for x in range(10) if x%4==0])?',
        'options': ['[0, 4, 8]', '[4, 8]', '[0, 4, 8, 12]', '[0, 2, 4, 6, 8]'],
        'answer': '[0, 4, 8]'
    },
    {
        'question': 'What is the output of print("python".replace("o", "a"))?',
        'options': ['pythan', 'python', 'pythona', 'pythn'],
        'answer': 'pythan'
    },
    {
        'question': 'What is the output of print([i**2 for i in range(3, 6)])?',
        'options': ['[9, 16, 25]', '[3, 4, 5]', '[6, 9, 12]', '[1, 4, 9]'],
        'answer': '[9, 16, 25]'
    },
    {
        'question': 'What is the output of print("python".count("y"))?',
        'options': ['1', '2', '0', '3'],
        'answer': '1'
    },
    {
        'question': 'What is the output of print([i for i in range(10) if i%5==0])?',
        'options': ['[0, 5]', '[5, 10]', '[0, 5, 10]', '[0, 2, 4, 6, 8]'],
        'answer': '[0, 5]'
    },
    {
        'question': 'What is the output of print("python"[1:4])?',
        'options': ['yth', 'pyt', 'tho', 'hon'],
        'answer': 'yth'
    },
    {
        'question': 'What is the output of print([i**3 for i in range(2, 5)])?',
        'options': ['[8, 27, 64]', '[2, 3, 4]', '[6, 9, 12]', '[1, 8, 27]'],
        'answer': '[8, 27, 64]'
    },
    {
        'question': 'What is the output of print("abc".find("d"))?',
        'options': ['-1', '0', '1', '2'],
        'answer': '-1'
    }
]

rapid_fire_easy_hindi = [
    {
        'question': 'Python में फ़ंक्शन को परिभाषित करने के लिए कौन सा कीवर्ड उपयोग होता है?',
        'options': ['def', 'func', 'function', 'define'],
        'answer': 'def'
    },
    {
        'question': '3 * 2 का परिणाम क्या है?',
        'options': ['6', '5', '9', '32'],
        'answer': '6'
    },
    {
        'question': 'कौन सा डेटा टाइप अपरिवर्तनीय (immutable) है?',
        'options': ['ट्यूपल', 'सूची', 'डिक्शनरी', 'सेट'],
        'answer': 'ट्यूपल'
    },
    {
        'question': 'What does `//` operator do?',
        'options': ['Floor Division', 'Division', 'Exponent', 'Modulo'],
        'answer': 'Floor Division'
    },
    {
        'question': 'How do you create a variable `x` with value 5?',
        'options': ['x = 5', 'x == 5', 'let x = 5', 'var x = 5'],
        'answer': 'x = 5'
    },
    {
        'question': 'What is the output of print(1+1)?',
        'options': ['2', '11', '1', '0'],
        'answer': '2'
    },
    {
        'question': 'Which function is used to get user input?',
        'options': ['input()', 'scan()', 'get()', 'read()'],
        'answer': 'input()'
    },
    {
        'question': 'What is the output of print("A"*2)?',
        'options': ['AA', 'A2', '2A', 'Error'],
        'answer': 'AA'
    },
    {
        'question': 'Which operator is used for subtraction?',
        'options': ['-', '+', '*', '/'],
        'answer': '-'
    },
    {
        'question': 'What is the output of print(6//2)?',
        'options': ['3', '2', '1', '0'],
        'answer': '3'
    },
    {
        'question': 'Which of these is a string?',
        'options': ['"hello"', '123', '[1,2,3]', 'True'],
        'answer': '"hello"'
    },
    {
        'question': 'What is the output of print(2*3)?',
        'options': ['6', '5', '23', '8'],
        'answer': '6'
    },
    {
        'question': 'Which function returns the type of an object?',
        'options': ['type()', 'typeof()', 'kind()', 'class()'],
        'answer': 'type()'
    },
    {
        'question': 'What is the output of print(9-4)?',
        'options': ['5', '13', '4', '9'],
        'answer': '5'
    },
    {
        'question': 'Which of these is a boolean value?',
        'options': ['True', '1', '"True"', 'None'],
        'answer': 'True'
    }
]

rapid_fire_intermediate_hindi = [
    {
        'question': 'print([i+1 for i in range(3)]) का आउटपुट क्या होगा?',
        'options': ['[1, 2, 3]', '[0, 1, 2]', '[2, 3, 4]', '[1, 3, 5]'],
        'answer': '[1, 2, 3]'
    },
    {
        'question': 'सूची का अंतिम आइटम प्राप्त करने के लिए कौन सी विधि उपयोग होती है?',
        'options': ['pop()', 'remove()', 'last()', 'end()'],
        'answer': 'pop()'
    },
    {
        'question': 'print("abc".lower()) का आउटपुट क्या होगा?',
        'options': ['abc', 'ABC', 'Abc', 'aBc'],
        'answer': 'abc'
    },
    {
        'question': 'Which of these is a tuple?',
        'options': ['(1, 2, 3)', '[1, 2, 3]', '{1, 2, 3}', 'tuple(1,2,3)'],
        'answer': '(1, 2, 3)'
    },
    {
        'question': 'What is the output of print(2 in [1, 2, 3])?',
        'options': ['True', 'False', 'None', 'Error'],
        'answer': 'True'
    },
    {
        'question': 'Which method adds an item to the end of a list?',
        'options': ['append()', 'add()', 'insert()', 'extend()'],
        'answer': 'append()'
    },
    {
        'question': 'What is the output of print("hello".title())?',
        'options': ['Hello', 'hello', 'HELLO', 'hELLO'],
        'answer': 'Hello'
    },
    {
        'question': 'Which function returns the maximum value?',
        'options': ['max()', 'min()', 'largest()', 'maximum()'],
        'answer': 'max()'
    },
    {
        'question': 'What is the output of print(list("xyz"))?',
        'options': ['["x", "y", "z"]', '[x, y, z]', 'xyz', '[xyz]'],
        'answer': '["x", "y", "z"]'
    },
    {
        'question': 'Which method reverses a list in place?',
        'options': ['reverse()', 'reversed()', 'flip()', 'invert()'],
        'answer': 'reverse()'
    }
]

rapid_fire_expert_hindi = [
    {
        'question': 'print({i: i*2 for i in range(2, 5)}) का आउटपुट क्या होगा?',
        'options': ['{2: 4, 3: 6, 4: 8}', '{2: 2, 3: 3, 4: 4}', '{2: 4, 3: 9, 4: 16}', '{4: 8, 3: 6, 2: 4}'],
        'answer': '{2: 4, 3: 6, 4: 8}'
    },
    {
        'question': 'इनमें से कौन सा वैध जनरेटर एक्सप्रेशन है?',
        'options': ['(x*x for x in range(3))', '[x*x for x in range(3)]', '{x*x for x in range(3)}', 'generator(x*x for x in range(3))'],
        'answer': '(x*x for x in range(3))'
    },
    {
        'question': 'print([i for i in range(7) if i%2==1]) का आउटपुट क्या होगा?',
        'options': ['[1, 3, 5]', '[0, 2, 4, 6]', '[2, 4, 6]', '[1, 2, 3, 4, 5]'],
        'answer': '[1, 3, 5]'
    },
    {
        'question': 'Which function returns the ceiling of a number?',
        'options': ['ceil()', 'floor()', 'int()', 'round()'],
        'answer': 'ceil()'
    },
    {
        'question': 'What is the output of print("python".count("o"))?',
        'options': ['1', '2', '0', '3'],
        'answer': '1'
    },
    {
        'question': 'Which method returns a deep copy of a list?',
        'options': ['copy.deepcopy()', 'copy()', 'clone()', 'replicate()'],
        'answer': 'copy.deepcopy()'
    },
    {
        'question': 'What is the output of print([x for x in range(10) if x%5==0])?',
        'options': ['[0, 5]', '[5, 10]', '[0, 5, 10]', '[0, 2, 4, 6, 8]'],
        'answer': '[0, 5]'
    },
    {
        'question': 'What is the output of print("python"[1:4])?',
        'options': ['yth', 'pyt', 'tho', 'hon'],
        'answer': 'yth'
    },
    {
        'question': 'Which method returns the number of items in a dictionary?',
        'options': ['len()', 'count()', 'size()', 'length()'],
        'answer': 'len()'
    }
]

code_combat_easy_hindi = [
    {
        'question': 'इस कोड का आउटपुट क्या होगा?\nx = [1, 2, 3]\nprint(len(x))',
        'options': ['3', '2', '4', 'त्रुटि'],
        'answer': '3'
    },
    {
        'question': 'आउटपुट का अनुमान लगाएँ:\nprint("Hello" + " " + "World")',
        'options': ['Hello World', 'HelloWorld', 'Hello World', 'त्रुटि'],
        'answer': 'Hello World'
    },
    {
        'question': '`x` का मान क्या होगा?\nx = 10 % 3',
        'options': ['1', '3', '0', '10'],
        'answer': '1'
    },
    {
        'question': 'What is the output of print("abc"[1])?',
        'options': ['b', 'a', 'c', 'Error'],
        'answer': 'b'
    },
    {
        'question': 'What is the output of print(2*2+2)?',
        'options': ['6', '8', '4', '2'],
        'answer': '6'
    },
    {
        'question': 'What is the output of print([i for i in range(2)])?',
        'options': ['[0, 1]', '[1, 2]', '[0, 1, 2]', '[1, 2, 3]'],
        'answer': '[0, 1]'
    },
    {
        'question': 'What is the output of print("a".upper())?',
        'options': ['A', 'a', 'Error', 'None'],
        'answer': 'A'
    },
    {
        'question': 'What is the output of print(3**2)?',
        'options': ['9', '6', '8', '12'],
        'answer': '9'
    },
    {
        'question': 'What is the output of print("hello".capitalize())?',
        'options': ['Hello', 'hello', 'HELLO', 'hELLO'],
        'answer': 'Hello'
    },
    {
        'question': 'What is the output of print(len("python"))?',
        'options': ['6', '5', '7', 'Error'],
        'answer': '6'
    },
    {
        'question': 'What is the output of print(10//3)?',
        'options': ['3', '3.33', '4', '3.0'],
        'answer': '3'
    },
    {
        'question': 'What is the output of print("a"*4)?',
        'options': ['aaaa', 'a4', '4a', 'Error'],
        'answer': 'aaaa'
    },
    {
        'question': 'What is the output of print([1,2,3][2])?',
        'options': ['3', '2', '1', 'Error'],
        'answer': '3'
    }
]

code_combat_intermediate_hindi = [
    {
        'question': 'इस कोड का आउटपुट क्या होगा?\nx = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)',
        'options': ['[1, 2, 3, 4]', '[1, 2, 3]', '[1, 2, 3, 4, 4]', 'त्रुटि'],
        'answer': '[1, 2, 3, 4]'
    },
    {
        'question': 'आउटपुट का अनुमान लगाएँ:\nmy_list = [1, 2, 3, 4, 5]\nprint(my_list[1:3])',
        'options': ['[2, 3]', '[1, 2]', '[2, 3, 4]', '[1, 2, 3]'],
        'answer': '[2, 3]'
    },
    {
        'question': 'इस कोड का आउटपुट क्या होगा?\nset1 = {1, 2, 3}\nset2 = {3, 4, 5}\nprint(set1.intersection(set2))',
        'options': ['{3}', '{1, 2, 3, 4, 5}', '{1, 2, 4, 5}', '{}'],
        'answer': '{3}'
    },
    {
        'question': 'Predict the output:\n\nmy_dict = {\'a\': 1, \'b\': 2}\nprint(my_dict.get(\'c\', 3))',
        'options': ['3', 'None', 'Error', '1'],
        'answer': '3'
    },
    {
        'question': 'What is the output of print([i**2 for i in range(3)])?',
        'options': ['[0, 1, 4]', '[1, 4, 9]', '[0, 1, 2]', '[1, 2, 3]'],
        'answer': '[0, 1, 4]'
    },
    {
        'question': 'What is the output of print("abc".replace("a", "z"))?',
        'options': ['zbc', 'azc', 'abz', 'abc'],
        'answer': 'zbc'
    },
    {
        'question': 'What is the output of print({i: i*2 for i in range(2, 5)})?',
        'options': ['{2: 4, 3: 6, 4: 8}', '{2: 2, 3: 3, 4: 4}', '{2: 4, 3: 9, 4: 16}', '{4: 8, 3: 6, 2: 4}'],
        'answer': '{2: 4, 3: 6, 4: 8}'
    },
    {
        'question': 'What is the output of print("python"[::-1])?',
        'options': ['nohtyp', 'python', 'nothpy', 'htypno'],
        'answer': 'nohtyp'
    },
    {
        'question': 'What is the output of print([x for x in range(10) if x%3==0])?',
        'options': ['[0, 3, 6, 9]', '[3, 6, 9]', '[0, 3, 6]', '[1, 4, 7, 10]'],
        'answer': '[0, 3, 6, 9]'
    },
    {
        'question': 'What is the output of print("abc".count("a"))?',
        'options': ['1', '2', '0', '3'],
        'answer': '1'
    },
    {
        'question': 'What is the output of print([i for i in range(5) if i%2==0])?',
        'options': ['[0, 2, 4]', '[1, 3, 5]', '[2, 4, 6]', '[0, 1, 2, 3, 4]'],
        'answer': '[0, 2, 4]'
    },
    {
        'question': 'What is the output of print("python".find("t"))?',
        'options': ['2', '1', '0', '-1'],
        'answer': '2'
    },
    {
        'question': 'What is the output of print([i for i in range(6) if i%3==0])?',
        'options': ['[0, 3]', '[0, 3, 6]', '[3, 6]', '[0, 3, 6, 9]'],
        'answer': '[0, 3]'
    },
    {
        'question': 'What is the output of print("abc".isalpha())?',
        'options': ['True', 'False', 'None', 'Error'],
        'answer': 'True'
    }
]

code_combat_expert_hindi = [
    {
        'question': 'print({i: i*i for i in range(2, 6)}) का आउटपुट क्या होगा?',
        'options': ['{2: 4, 3: 9, 4: 16, 5: 25}', '{2: 2, 3: 3, 4: 4, 5: 5}', '{2: 4, 3: 9, 4: 16}', '{4: 16, 3: 9, 2: 4, 5: 25}'],
        'answer': '{2: 4, 3: 9, 4: 16, 5: 25}'
    },
    {
        'question': 'print("".join(sorted(set("banana")))) का आउटपुट क्या होगा?',
        'options': ['abn', 'abnn', 'ab', 'abna'],
        'answer': 'abn'
    },
    {
        'question': 'print([x for x in range(10) if x%4==0]) का आउटपुट क्या होगा?',
        'options': ['[0, 4, 8]', '[4, 8]', '[0, 4, 8, 12]', '[0, 2, 4, 6, 8]'],
        'answer': '[0, 4, 8]'
    },
    {
        'question': 'What is the output of print("python".replace("o", "a"))?',
        'options': ['pythan', 'python', 'pythona', 'pythn'],
        'answer': 'pythan'
    },
    {
        'question': 'What is the output of print([i**2 for i in range(3, 6)])?',
        'options': ['[9, 16, 25]', '[3, 4, 5]', '[6, 9, 12]', '[1, 4, 9]'],
        'answer': '[9, 16, 25]'
    },
    {
        'question': 'What is the output of print("python".count("y"))?',
        'options': ['1', '2', '0', '3'],
        'answer': '1'
    },
    {
        'question': 'What is the output of print([i for i in range(10) if i%5==0])?',
        'options': ['[0, 5]', '[5, 10]', '[0, 5, 10]', '[0, 2, 4, 6, 8]'],
        'answer': '[0, 5]'
    },
    {
        'question': 'What is the output of print("python"[1:4])?',
        'options': ['yth', 'pyt', 'tho', 'hon'],
        'answer': 'yth'
    },
    {
        'question': 'What is the output of print([i**3 for i in range(2, 5)])?',
        'options': ['[8, 27, 64]', '[2, 3, 4]', '[6, 9, 12]', '[1, 8, 27]'],
        'answer': '[8, 27, 64]'
    },
    {
        'question': 'What is the output of print("abc".find("d"))?',
        'options': ['-1', '0', '1', '2'],
        'answer': '-1'
    }
]