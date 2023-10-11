from algorithms import NonConstructibleChange


def run_script():
    result = NonConstructibleChange.non_constructible_change(
        coins=[5, 7, 1, 1, 2, 3, 22]
    )
    print(result)


if __name__ == '__main__':
    run_script()
