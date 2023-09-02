<?php
class Logger
{
    public static $logCount = 0;

    public static function log($message)
    {
        echo $message . "</br>";
        self::$logCount++;
    }
}
Logger::log("Log message 1");
Logger::log("Log message 2");
Logger::log("Log message 3");

echo "Total log count: " . Logger::$logCount . "</br>";

?>