# -*- coding: utf8 -*-
MAX_SIZE_ARR = 10				# Максимальный размер массива
MAX_SIZE_VAR = 100				# Максимальный размер элемента массива

def swap(arr, start ,end):		# Функция меняющая элементы массива местами
	if(start != end):
		arr[start],arr[end] = arr[end],arr[start]


def bubble_sort(list):			# Алгоритм сортировки пузырьком
	length = len(list) - 1
	sorted = False
	while not sorted:
		sorted = True
		for i in range(length):
			if list[i] > list[i + 1]:
				sorted = False
				list[i], list[i + 1] = list[i + 1], list[i]
	return list


def Interface():				# Общение с пользователями
	array = []
	num_error = 1
	arr_error = 1
	while(num_error == 1):		# Проверка на то, что пользователь корректную величину массива
		try:
			num = input("Введите размер массива(<" + str(MAX_SIZE_ARR)+"): ")
			num = int(num)
			if(num > MAX_SIZE_ARR):
				print("Максимальный размер массива: " + str(MAX_SIZE_ARR))
				err = int("err")

			num_error = 0
		except ValueError:
			print("Вы ввели не корректные данные. Сделайте выбор заново.")
			print("================================================================")
		continue

	for i in range(num):		# Заполнение массива + проверка
			while (arr_error == 1):
				try:
					x = input("Введите элемент №" + str(i) + ": ")
					x = int(x)
					if (x > MAX_SIZE_VAR):
						print("Максимальный размер элемента массива: " + str(MAX_SIZE_VAR))
						err = int("err")
					array.append(x)
					arr_error = 0
				except ValueError:
					print("Вы ввели не корректные данные. Сделайте выбор заново.")
					print("================================================================")
				continue
			arr_error = 1
	return array


if __name__ == "__main__":
	mas = Interface()
	print("\n\nSource array: " + str(mas))
	bubble_sort(mas)
	print("\nSource array: " + str(mas))
	end = input()