<?php
session_save_path('/Applications/XAMPP/xamppfiles/htdocs/shashank/PHP_Assignment_31-08-2023/Cookies');
session_start();
if (isset($_SESSION["userid"])) {
    $userid = $_SESSION["userid"];
    echo "Value of session variable 'userid': " . $userid;
} else {
    echo "Session variable 'userid' not found.";
}
?>