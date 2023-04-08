import types

# функция для решения задачи №2
def flat_generator(list_of_lists):
    for lst in list_of_lists:
        for el in lst:
            yield el


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

# для проверки кода
list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

# вспомогательная функция для проверки правильности решения задачи №2
def check_flat_list_from_task_2(lst):
    for el in flat_generator(lst):
        print(el, end=' ')


if __name__ == '__main__':
    test_2()

    check_flat_list_from_task_2(list_of_lists_1)
