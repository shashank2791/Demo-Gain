<?php
class Calculator
{
    private $result;

    public function __construct()
    {
        $this->result = 0;
    }

    public function getResult()
    {
        return $this->result;
    }

    public function add($number)
    {
        $this->result += $number;
    }

    public function subtract($number)
    {
        $this->result -= $number;
    }
}

$calculator = new Calculator();

$calculator->add(4);
$calculator->add(5);
$calculator->subtract(3);

$result = $calculator->getResult();
echo "Result: " . $result;
?>