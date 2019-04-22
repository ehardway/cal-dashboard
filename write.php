<?php
$json_data = json_encode($_POST);
$ret = file_put_contents('tmp/changes.json', $json_data);
echo "$ret bytes written to file";
