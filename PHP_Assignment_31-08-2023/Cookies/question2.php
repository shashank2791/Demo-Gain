<?php
$cookieName = "username";

if (isset($_COOKIE[$cookieName])) {
    $cookieValue = $_COOKIE[$cookieName];
    echo "Value of cookie 'username': " . $cookieValue;
} else {
    echo "Cookie 'username' not found.";
}
?>