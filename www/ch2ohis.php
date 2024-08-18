<?php

$num = 24*3*5;
$datfile = '/home/xhyh/app/ch2o.log';


function get_last_n_lines($filename, $n) {

    // 检查文件是否存在
    if (!file_exists($filename)) {
        return false;
    }

    // 读取整个文件
    $lines = file($filename, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

    // 如果文件行数少于请求的行数，则返回所有行
    if (count($lines) <= $n) {
        return $lines;
    }

    // 截取最后 n 行
    $lastNLines = array_slice($lines, -($n));

    return $lastNLines;
}


$d = get_last_n_lines($datfile, $num);

if($d !== false){
    foreach ($d as $line) {
        echo $line . "|";
    }
} else {
    echo '';
}

?>