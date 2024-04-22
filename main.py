def test_function():

    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

test_function()
inner_function()    # При вызове функции inner_function() вне функции test_function(), происходит ощибка
                    # т.к. функия inner_function() определена  только в области видмости
                    # функиии test_function() 