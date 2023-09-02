<?php
$cookieName = "mera_Cookie";
$cookieValue = "mera_Cookie_value";
$expirationTime = time() + 3600; // current time + 1 hour
$secureOnly = true; // Set the cookie to be transmitted only over HTTPS

setcookie($cookieName, $cookieValue, $expirationTime, "/", "", $secureOnly, true);

echo "Secure cookie named 'mera_Cookie' has been set.";
?>