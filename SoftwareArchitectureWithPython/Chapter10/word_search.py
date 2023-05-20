"""
调试思想：
1. 提出假设
2. 测试假设
3. 要么成功
4. 要么循环，测试下一个假设

"""

def grep_word(word, filenames)->list:
    """
    词搜索器：搜索给定文件列表中包含特定关键字的行
    :param word:
    :param filenames:
    :return:
    """
    lines = []
    results = []
    for filename in filenames:
        lines += open(filename, "r").readlines()

    for line in lines:
        if word.lower() in line.lower():
            results.append(line.strip())
    return sorted(results, key=len)

if __name__ == "__main__":
    from glob import glob
    print(grep_word("类", glob("../*/*.py")))