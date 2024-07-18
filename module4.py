def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


inner_function() # Попытка вызвать inner_function вне test_function вызовет ошибку NameError, поскольку 
                # inner_function не существует в глобальной области видимости.
