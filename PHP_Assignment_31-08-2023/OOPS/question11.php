<?php
class Person
{
    protected $name;
    protected $age;

    public function __construct($name, $age)
    {
        $this->name = $name;
        $this->age = $age;
    }

    public function __toString()
    {
        return "Name: " . $this->name . "\n" .
            "Age: " . $this->age . "\n";
    }
}

class Employee extends Person
{
    private $salary;
    private $position;

    public function __construct($name, $age, $salary, $position)
    {
        parent::__construct($name, $age);
        $this->salary = $salary;
        $this->position = $position;
    }

    public function getSalary()
    {
        return $this->salary;
    }

    public function getPosition()
    {
        return $this->position;
    }

    public function displayDetails()
    {
        echo "Name: " . $this->name . "</br>";
        echo "Age: " . $this->age . "</br>";
        echo "Salary: " . $this->salary . "</br>";
        echo "Position: " . $this->position . "</br>";
    }
}

$employee = new Employee("Shashank Madhwal", 23, 600000, "ASDET");
$employee->displayDetails();

?>