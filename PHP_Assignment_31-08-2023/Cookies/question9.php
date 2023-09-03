<?php
session_start();

// Array of user preferences
$userPreferences = array(
    'theme' => 'dark',
    'language' => 'UK English',
    'notifications' => true
);

$_SESSION['preferences'] = $userPreferences;

echo "User preferences have been stored in the session variable 'preferences'.";

?>