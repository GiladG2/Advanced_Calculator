# Advanced_Calculator
 An advanced calculator that can evaluate mathematical equations 

 ## Supported features
 
 ## Addition(+)
 # 1+3 => 2

 ## Subtraction (-)
 # 2-5 => -3

 ## Division (/)
 ```sh
  5/2 => 2.5
```
## Multiplication (*)

```sh
5*2*5 => 50
```
 ## Implicit mul 
 ```sh
2(50) => 100
2(50+50) => 200
```
## Minus negation (-) 
```sh
-40+20 => -20
```
## Power (^)
```sh
4^3^2 => 4096
```
## Modulo (%)
```sh
4%2 => 0
```
## Max ($)
### A$B => Max(a,b)
```sh
5$2 =>5
```
## Min (&)
### A&b => Min(a,b)
```sh
5&2 = > 2
```
## Avg (@)
### A@B => Avg(a,b)
```sh
5@2 = > 3.5
```
## Tilde (~)
### Tilde is an unary negation op
### Tilde should start negation and is left associative and is unary
```sh
Correct use:
~3 = -3
~-3 = 3
Incorrect use:
3~ => Tilde is left associative
-~3 => Tilde should start negation
3~2 => Tilde cannot be used as a binary operator
```
## Factorial (!)
### Factorial is left associative, the value that is being factored has to be positive and a whole integer and is unary
```sh
Examples:

Correct use:
3! =>6
-3! => -6
Incorrect use:
!3 => Factorial is right associative
~3! => (-3)! => Error, cannot factor negative values
2.5! => Error, cannot factor decimals
4!3 => Factorial cannot be used as binary operator
```
## Hashtag (#)
### Hashtag is right associative, the value that the hashtag function gets has to be positive and a whole integer and is unary
#### The hashtag function sums the digit of a number
```
Examples:

Correct use:
123# => 6
-123# => -6
3+123# => 9

Incorrect use:
~123# => (-123)# => Error, cannot hashtag negative values
2.5# => Error, cannot hashtag decimals 
```
``
````
