<?php
// Set the session save path
session_save_path('/Applications/XAMPP/xamppfiles/htdocs/shashank/PHP Assignment 31-08-2023');


// Get the session save path directory
$sessionSavePath = session_save_path();

// Get all session files in the save path directory
$sessionFiles = glob($sessionSavePath . '/*');

// Initialize the session counter
$activeSessions = 0;

// Iterate through the session files
foreach ($sessionFiles as $sessionFile) {
    // Check if the session file is valid
    if (is_file($sessionFile) && filectime($sessionFile) + ini_get('session.gc_maxlifetime') > time()) {
        $activeSessions++;
    }
}
echo "Number of active sessions: " . $activeSessions;
?>