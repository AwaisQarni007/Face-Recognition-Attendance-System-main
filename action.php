<!-- action.php -->
<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
// Get the submitted username and password from the form
$username = $_POST['loginUsername'];
$password = $_POST['loginPassword'];
// Check if the username and password match the expected values
if ($username === 'Admin' && $password === 'Admin') {
    // Execute the Python script using system command
    echo ("Username  Password Correct");
    $command = 'python AMS_Run.py';
    $output = shell_exec($command);
    
    // Output the result of the Python script
    echo "Python script executed successfully. Result: " . $output;
} else {
    echo "Invalid username or password.";
}
?>
