#!/usr/bin/env python3
"""Task 1: Shapes, Interfaces, and Duck Typing"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract base class for geometric shapes"""
    
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape
        
        Returns:
            float: The calculated area
        """
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape
        
        Returns:
            float: The calculated perimeter
        """
        pass

class Circle(Shape):
    """Circle implementation of Shape with radius-based calculations"""
    
    def __init__(self, radius: float):
        """Initialize with radius
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """Rectangle implementation of Shape with width/height-based calculations"""
    
    def __init__(self, width: float, height: float):
        """Initialize with width and height
        
        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
        """
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

def shape_info(shape: Shape):
    """Print area and perimeter of any shape-like object
    
    Args:
        shape (Shape): An object implementing area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Testing section
if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
