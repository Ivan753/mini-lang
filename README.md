# mini-lang
Репозиторий создан для демонстрации примера использования языка Python для создания
простейшего интерпретатора, принимающего язык синтаксис и грамматика которого
отвечает следующим минимальным условиям:

>Входной язык содержит операторы условия (if ... then ... else ... end и if ... then ... end), и операторы print,
оканчивающиеся символом ; (точка с запятой). Операторы if в части условия содержат сравнение (>, <, =),
в котором слева и справа могут присутствовать идентификаторы и шестнадцатеричные числа.
Шестнадцатеричными числами считать последовательность цифр и символов a, b, c, d, e, f, начинающуюся
с цифры (например, 89, 45ac, 0abc). Оператор print имеет аргумент – шестнадцатеричное число.

## Пример работы

### Исхохдный код

```
x := 5;
y := 0;

if x > 0 then
    if y > 0 then
        print 1;
    else
        print 2;
    end;
end;
if x > 1 then print abc; end;
```

### Результат
Исключение: переменная `abc` не была определена

## Ресурсы

Лексический анализатор - `lexer.py`
Грамматические анализатор - `parser.py`
Интерпретатор AST - `Parser.eval_statement()` и `Parser.eval()` из `parser.py`
Грамматика языка - `./grammar`

## Запуск

```
python3 do example
```
