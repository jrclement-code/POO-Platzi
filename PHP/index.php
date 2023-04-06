<?php
require_once('car.php');
require_once('uberX.php');
require_once('uberPool.php');
require_once('uberVan.php');
require_once('account.php');


$uberX = new UberX("AMQ123", new Account("Andres Herrera", "ANDA876"), "Chevrolet", "Spark");
$uberX->setPassenger(4);
$uberX->printDataCar();

$uberPool = new UberPool("RET436", new Account("Jose Manrrique", "ANDV583"), "Dodge", "Attitude");
$uberPool->setPassenger(2);
$uberPool->printDataCar();

$uberVan = new UberVan("OJL395", new Account("Raúl Ramírez", "AND456"), "Nissan", "Versa");
$uberVan->setPassenger(6);
$uberVan->printDataCar();