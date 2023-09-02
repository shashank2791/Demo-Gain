<!DOCTYPE html>
<html>

<head>
    <title>Orthogonal Check Result</title>
</head>

<body>
    <h1>Orthogonal Check Result</h1>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        function is_orthogonal($x1, $y1, $x2, $y2)
        {
            $dot_product = $x1 * $x2 + $y1 * $y2;
            return $dot_product == 0;
        }

        $xp = floatval($_POST["xp"]);
        $yp = floatval($_POST["yp"]);
        $xq = floatval($_POST["xq"]);
        $yq = floatval($_POST["yq"]);
        $xr = floatval($_POST["xr"]);
        $yr = floatval($_POST["yr"]);
        $xs = floatval($_POST["xs"]);
        $ys = floatval($_POST["ys"]);

        $vector_AB = [$xq - $xp, $yq - $yp];
        $vector_CD = [$xs - $xr, $ys - $yr];

        if (is_orthogonal($vector_AB[0], $vector_AB[1], $vector_CD[0], $vector_CD[1])) {
            echo "AB and CD are orthogonal.";
        } else {
            echo "AB and CD are not orthogonal.";
        }
    }
    ?>
    <p><a href="index_orthogonal.html">Go back</a></p>
</body>

</html>