import math
class Calculator:
    """
    This class consist of many functions for numerical operation.

    functions:
        add(int,int)->int
        divide(int,int)->int
        subtract(int,int)->int
        multiply(int,int)->int

    """
   

    def add(self,a: int,b : int) -> int :
        """
        Add function added two number
        
        Args:
            a (int) : first number
            b (int) : second number

        Return:
            int : return sum of a and b
        """
        return a+b
    
    def divide(self , a: int,b: int) -> int:
        """
        divide function divide two number
        
        Args:
            a (int) : first number
            b (int) : second number

        Return:
            int : return quotient of a and b
        """
        return a/b

    def multiply(self, a: int, b: int) -> int:
        """
        multiply function multiply two number
        
        Args:
            a (int) : first number
            b (int) : second number

        Return:
            int : return product of a and b
        """
        return a*b
    
    def subtract(self, a: int,b: int) -> int:
        """
        Subtract function subtract two number
        
        Args:
            a (int) : first number
            b (int) : second number

        Return:
            int : return difference of a and b
        """
        return a-b