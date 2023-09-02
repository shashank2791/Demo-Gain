<?php
session_save_path('/Applications/XAMPP/xamppfiles/htdocs/shashank/PHP Assignment 31-08-2023');
session_start();

if (isset($_SESSION["preferences"])) {
    $userPreferences = $_SESSION["preferences"];

    echo "User Preferences:</br>";
    foreach ($userPreferences as $key => $value) {
        echo $key . ": " . $value . "</br>";
    }
} else {
    echo "No user preferences found.";
}

?>