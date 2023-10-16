def bubble_sort(input_list):
    len_input_list  = len(input_list)
    for i in range(len_input_list):
        for j in range(len_input_list-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]

    return input_list

def main(unsoerted_list):
    print(bubble_sort(unsoerted_list))

def test_bubble_srot(unsoerted_list):
    assert bubble_sort(unsoerted_list) == sorted(unsoerted_list)

if __name__ == "__main__":
    unsoerted_list = [64, 34, 25, 12, 22, 11, 90]
    main(unsoerted_list)
    test_bubble_srot(unsoerted_list)