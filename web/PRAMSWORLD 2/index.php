<?php

include 'secret.php';

if (!isset($_GET['cmd'])) {
    highlight_file('./debug.php'); die();
}

$cmd = (string) $_GET['cmd'];
$decode = base64_decode($cmd);

// highlight_file(trim($decode));
echo $decode;
?>