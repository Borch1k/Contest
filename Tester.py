from generators import *
import subprocess
import os
import time
import shutil
from multiprocessing.pool import Pool
import time


class Content:
    def __init__(self, student_program, reference_program, test_string, custom_tester):
        self._1 = student_program
        self._2 = reference_program
        self._3 = test_string
        self._4 = custom_tester

    def unpack(self):
        return self._1, self._2, self._3, self._4


def Tester(student_program, reference_program, test_string, custom_tester):
    with Pool(3) as p:
        content = Content(student_program, reference_program, test_string, custom_tester)
        verdict = p.map(run_test, [content]*3)
    for v in verdict:
        if not v[0]:
            return v
    return verdict[0]


def communicate(program, test_data, cwd):
    test = subprocess.Popen(['python', '../../' + program], stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE, text=True, cwd=cwd, encoding='utf-8')
    answer, err = test.communicate(test_data)
    # print(err)
    if os.path.exists(cwd + 'output.txt'):
        with open(cwd + 'output.txt') as f:
            ref_file = f.read()
            if ref_file:
                answer = ref_file
        os.remove(cwd + 'output.txt')
    return answer, err


def is_save(file_name):
    banned_modules = [' sys ', ' os ', ' subprocess ', ' webbrowser ']
    allowed_functions = ['sys.stdin']
    with open(file_name, 'r', encoding='utf-8') as code_file:
        code = code_file.read()

    for module in banned_modules:
        if module in code:
            for function in allowed_functions:
                if function not in code:
                    return False
    return True


def run_test(content):
    """student_program, reference_program is path and test_string is strings"""
    student_program, reference_program, test_string, custom_tester = content.unpack()
    if not is_save(student_program):
        return -3, 'No test for you', 'No answer for you', 'BorisError: Function is not allowed.'
    start = time.time()
    for i in range(10):
        if time.time() - start > 30:
            return -4, None, None, None
        test_data = ''
        if test_string:
            test_data = eval(test_string)

        hex_code = hex(time.time_ns()) + random_string(10)
        cwd = os.path.join('temp/', hex_code+'/')

        os.mkdir(cwd)
        f = open(cwd+'input.txt', 'x', encoding='utf-8')
        f.write(test_data)
        f.close()

        reference_answer, err = communicate(reference_program, test_data, cwd)

        student_answer, err = communicate(student_program, test_data, cwd)

        shutil.rmtree(cwd)

        if 'Non-UTF-8' in err:
            return -2, None, None, None

        if err:
            return -1, test_data, reference_answer, student_answer + '\n' + err

        # print(reference_answer, student_answer)

        if custom_tester:
            if eval(custom_tester)(reference_answer) == eval(custom_tester)(student_answer):
                return 1, None, None, None
            else:
                return False, test_data, reference_answer, student_answer
        if reference_answer.strip() != student_answer.strip():
            return 0, test_data, reference_answer, student_answer
    return 1, None, None, None


def sum_tester(s):
    _sum = sum(list(map(int, s.split())))
    return _sum

def set_tester(s):
    _set = set(s.split())
    return _set

def no_tester(s):
    return ''

def cut_tester(s):
    if s.find('.') != -1:
        return s[s.find('.'):s.find('.')+3]
    return s


if __name__ == "__main__":
    pass
