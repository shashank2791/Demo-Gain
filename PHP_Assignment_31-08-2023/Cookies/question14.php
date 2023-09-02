<?php
// Set the session save path
session_save_path('/Applications/XAMPP/xamppfiles/htdocs/shashank/PHP Assignment 31-08-2023');


session_start();

// Regenerate the session ID
session_regenerate_id(true);

echo "Session ID has been regenerated.";

?>