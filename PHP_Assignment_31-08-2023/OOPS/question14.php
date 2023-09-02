<?php
class Math
{
    public static function add($num1, $num2)
    {
        return $num1 + $num2;
    }

    public static function subtract($num1, $num2)
    {
        return $num1 - $num2;
    }

    public static function multiply($num1, $num2)
    {
        return $num1 * $num2;
    }
}

$result1 = Math::add(4, 3);
$result2 = Math::subtract(14, 4);
$result3 = Math::multiply(8, 2);

echo "Addition: " . $result1 . "</br>";
echo "Subtraction: " . $result2 . "</br>";
echo "Multiplication: " . $result3 . "</br>";
?>