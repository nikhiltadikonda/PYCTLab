<?php
echo "Hello<br>";
$a=2;
$b=3;
echo "<br>Sum is ";
echo $a+$b;

//Factorial
$a=1;
$x=5;
echo "<br><br>Factorial is ";
while($x>0){
    $a=$x*$a;
    $x--;
}
echo " ".$a;

//Indexed Arrays
$cars = array("Volvo", "BMW", "Toyota");
echo "<br><br>I like " . $cars[0] . ", " . $cars[1] . " and " . $cars[2] . ".";

//Associative Arrays
$age = array("Peter"=>"35", "Ben"=>"37", "Joe"=>"43");
echo "<br><br>Peter is " . $age['Peter'] . " years old.";

$num=array(8,7,6,5,4,3,2,1);
//Functions
function printNumbers($numbers){

    //Array of Numbers
$numbers=array(8,7,6,5,4,3,2,1);
sort($numbers);//sort

//For-Each Loop
$sumn=0;
echo "<br><br>Sorted Array is:";
foreach($numbers as $a){
    $sumn+=$a;
    echo $a." ";
}

rsort($numbers);
//Reverse Sort

echo "<br><br>Reverse Sorted Array is:";
foreach($numbers as $a){
    echo $a." ";
}
echo "<br><br>Sum of elements of array is: ".$sumn;
echo "<br>";
}
printNumbers($num);
?>