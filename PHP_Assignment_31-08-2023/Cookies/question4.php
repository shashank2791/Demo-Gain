<?php
// session_save_path('/Applications/XAMPP/xamppfiles/htdocs/shashank/PHP_Assignment_31-08-2023/Cookies');
session_start();

$_SESSION["userid"] = 10020;

echo "Session variable 'userid' has been set with the value 10020.";
?>