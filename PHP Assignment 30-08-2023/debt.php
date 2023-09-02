<!DOCTYPE html>
<html>

<head>
    <title>Debt Calculation Result</title>
</head>

<body>
    <h1>Debt Calculation Result</h1>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $months = intval($_POST["months"]);

        if ($months < 0 || $months > 100) {
            echo "<p>Please enter a valid number of months (0 to 100).</p>";
        } else {
            $borrowingAmount = 100000;
            $interestRate = 0.05;

            $debt = $borrowingAmount;
            for ($i = 0; $i < $months; $i++) {
                $interest = round($debt * $interestRate);
                $debt += $interest;

                // Round up to the nearest 1000
                $debt = ceil($debt / 1000) * 1000;
            }

            echo "<p>Amount of debt after $months months: $debt</p>";
        }
    }
    ?>
    <p><a href="index_debt.html">Go back</a></p>
</body>

</html>