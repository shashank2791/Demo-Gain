<?php
interface Comparable
{
    public function compareTo($other);
}

class Product implements Comparable
{
    private $name;
    private $price;

    public function __construct($name, $price)
    {
        $this->name = $name;
        $this->price = $price;
    }

    public function getName()
    {
        return $this->name;
    }

    public function getPrice()
    {
        return $this->price;
    }

    public function compareTo($other)
    {
        if ($other instanceof Product) {
            if ($this->price < $other->getPrice()) {
                return -1;
            } elseif ($this->price > $other->getPrice()) {
                return 1;
            } else {
                return 0;
            }
        } else {
            throw new Exception("Invalid comparison object.");
        }
    }
}

$product1 = new Product("Desktop", 120000);
$product2 = new Product("Laptop", 100000);

$result = $product1->compareTo($product2);

if ($result < 0) {
    echo $product1->getName() . " is cheaper than " . $product2->getName() . "</br>";
} elseif ($result > 0) {
    echo $product1->getName() . " is more expensive than " . $product2->getName() . "</br>";
} else {
    echo $product1->getName() . " and " . $product2->getName() . " have the same price.</br>";
}

?>