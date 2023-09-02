<?php
session_save_path('/Applications/XAMPP/xamppfiles/htdocs/shashank/PHP Assignment 31-08-2023');
session_start();

// Unset all session variables
$_SESSION = [];

// Destroy the session
session_destroy();

echo "Session destroyed. All session variables have been unset.";
?>