class FlatIterator:
# класс для решения задачи №1
    def __init__(self, list_of_list):
        self.input_list = list_of_list

    def __iter__(self):
        self.top_counter = 0
        self.inner_counter = 0
        self.all_done = False
        return self

    def __next__(self):
        ''' счетчиком top_counter проходим по всем элементам листа input_list, а счетчиком inner_counter по всем
        элементам каждого вложенного листа'''
        if not self.all_done:
            while self.top_counter < len(self.input_list):
                cur_list = self.input_list[self.top_counter]
                if self.inner_counter < len(cur_list):
                    item = cur_list[self.inner_counter]
                    self.inner_counter += 1
                    return item
                self.top_counter += 1
                self.inner_counter = 0
            self.all_done = True
        raise StopIteration

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


# для проверки кода
list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
]

# вспомогательная функция для проверки правильности решения задачи №1
def check_flat_list_from_task_1(lst):
    for el in FlatIterator(lst):
        print(el, end=' ')


if __name__ == '__main__':
    test_1()

    check_flat_list_from_task_1(list_of_lists_1)
