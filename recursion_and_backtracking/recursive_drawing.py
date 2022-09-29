number = int(input())
first_half = input()
second_half = input()


def recursive_draw(first_char, second_char, repeat_times):
    # pre post recursive behavior
    if repeat_times <= 0:
        return
    print(first_char * repeat_times)
    recursive_draw(first_char, second_char, repeat_times - 1)
    print(second_char * repeat_times)


recursive_draw(first_half, second_half, number)
