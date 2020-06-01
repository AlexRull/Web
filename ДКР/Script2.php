<?php

require_once('phpmailer/PHPMailerAutoload.php');

$mail = new PHPMailer;

$name = $_POST['user_name'];
$phone = $_POST['user_phone'];
$product = $_POST['product'];
	
$to      = 'sale@ligna.com.ua';
$subject = 'Замовлення';
$message = '' .$name . '<br>Залишив заявку на товар : '.$product . '<br>Номер телефона : ' .$phone;

$headers = "Content-type: text/html; charset=\"utf-8\"";

 if(mail($to, $subject, $message, $headers)) {
    header('location: Thank_page.html');
} else {
    echo 'Error';
}
?>