<?php
echo "Coba cari RCE nya<br><br>";
 
if (isset($_GET['pat']) && isset($_GET['rep']) && isset($_GET['sub'])) {
 
  $pattern = $_GET['pat'];
  $replacement = $_GET['rep'];
  $subject = $_GET['sub'];
 
  echo "original : ".$subject ."</br>";
  echo "replaced : ".preg_replace($pattern, $replacement, $subject);
}else{
    die();
}
?>