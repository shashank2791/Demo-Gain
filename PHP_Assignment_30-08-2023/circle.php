<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Circle Relationship Calculator</title>
</head>

<body>
    <h1>Circle Relationship Calculator</h1>
    <p>Enter the radius and coordinates of two circles:</p>
    <form method="post" action="">
        <label for="circle">C1 Radius and Coordinates (r1, x1, y1) and C2 Radius and Coordinates (r2, x2, y2):</label>
        <input type="text" name="circle" id="circle" required><br><br>
    </form>

    <?php
    function checkCircleRelationship($x1, $y1, $r1, $x2, $y2, $r2)
    {
        $r = sqrt(($x2 - $x2) * ($x2 - $x2) + ($y2 - $y1) * ($y2 - $y1));
        if ($r + $r1 < $r2) {
            return "C1  is in C2\n";
        }
        if ($r + $r2 < $r1) {
            return "C2  is in C1.\n";
        }

        if ($r <= $r1 + $r2) {
            return "Circumference of C1  and C2  intersect.";

        }
        return "C1 and C2 do not overlap.\n";
    }

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $circleInput = $_POST["circle"];

        $circleTokens = explode(" ", $circleInput);

        if (count($circleTokens) != 6) {
            echo "<p style='color: red;'>Invalid input format. Please enter 3 real numbers separated by a space for each circle.</p>";
        } else {
            $r1 = floatval($circle1Tokens[0]);
            $x1 = floatval($circle1Tokens[1]);
            $y1 = floatval($circle1Tokens[2]);
            $r2 = floatval($circle2Tokens[3]);
            $x2 = floatval($circle2Tokens[4]);
            $y2 = floatval($circle2Tokens[5]);

            $result = checkCircleRelationship($x1, $y1, $r1, $x2, $y2, $r2);
            echo "<p><strong>Result:</strong> $result</p>";
        }
    }
    ?>
</body>

</html>