<?php
unset($_POST['submit']);
$json_data = json_encode($_POST);
$ret = file_put_contents('tmp/changes.json', $json_data);
echo "$ret bytes written to file";
system("/var/www/html/reports/dash/update_content.py");
system("/var/www/html/reports/dash/dashboard.py > tmp/test.html");
echo "<br>";
echo "<a href=form.html> Go Back To Form </a>"; 
echo "<br>";
echo "<a href=tmp/test.html> Go To DashBoard </a>";
