def func(spam, eggs, toast = 0,  ham = 0):      # First 2 required
    print((spam, eggs, toast, ham))

func(1, 2)      # Output: (1, 2, 0, 0)
func(1, ham = 1, eggs = 0)      # Output: (1, 0, 0, 1)
func(spam = 1, eggs = 0)        # Output: (1, 0, 0, 0)
func(toast = 1, eggs = 2, spam = 3)         # Output: (3, 2, 1, 0)
func(1, 2, 3, 4)        # Output: (1, 2, 3, 4)