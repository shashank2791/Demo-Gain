<?php
// Set the session save path
session_save_path('/Applications/XAMPP/xamppfiles/htdocs/shashank/PHP Assignment 31-08-2023');

session_start();

if (isset($_SESSION['last_access_time'])) {
    $lastAccessTime = $_SESSION['last_access_time'];
    echo "Last access time: " . date('Y-m-d H:i:s', $lastAccessTime);
    $_SESSION['last_access_time'] = time(); // Update the last access time
} else {
    $_SESSION['last_access_time'] = time();
    echo "Session started. First access.";
}

?>