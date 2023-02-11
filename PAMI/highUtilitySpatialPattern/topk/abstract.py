#  Copyright (C)  2021 Rage Uday Kiran
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.

from abc import ABC, abstractmethod
import time
import validators
from urllib.request import urlopen
import csv
import pandas as pd
from collections import defaultdict
from itertools import combinations as c
import os
import os.path
import psutil
import sys
import validators
from urllib.request import urlopen


class utilityPatterns(ABC):
    """ This abstract base class defines the variables and methods that every topk spatial high utility pattern mining algorithm must
        employ in PAMI


    Attributes :
    ----------
        iFile : str
            Input file name or path of the input file
        k: integer
            The user can specify k (top-k)
        sep : str
            This variable is used to distinguish items from one another in a transaction. The default seperator is tab space or \t.
            However, the users can override their default separator
        startTime:float
            To record the start time of the algorithm
        endTime:float
            To record the completion time of the algorithm
        finalPatterns: dict
            Storing the complete set of patterns in a dictionary variable
        oFile : str
            Name of the output file to store complete set of frequent patterns
        memoryUSS : float
            To store the total amount of USS memory consumed by the program
        memoryRSS : float
            To store the total amount of RSS memory consumed by the program

    Methods :
    -------
        startMine()
            Calling this function will start the actual mining process
        getPatterns()
            This function will output all interesting patterns discovered by an algorithm
        save(oFile)
            This function will store the discovered patterns in an output file specified by the user
        getPatternsAsDataFrame()
            The function outputs the patterns generated by an algorithm as a data frame
        getMemoryUSS()
            This function outputs the total amount of USS memory consumed by a mining algorithm
        getMemoryRSS()
            This function outputs the total amount of RSS memory consumed by a mining algorithm
        getRuntime()
            This function outputs the total runtime of a mining algorithm
    """

    def __init__(self, iFile, nFile, k, sep="\t"):
        """
        :param iFile: Input file name or path of the input file
        :type iFile: str
        :param nFile: Input file name or path of the neighbourhood file
        :type nFile: str
        :param k: The user can specify k in count
        :type k: int
        :param sep: separator used to distinguish items from each other. The default separator is tab space. However, users can override the default separator
        :type sep: str
        """

        self.iFile = iFile
        self.sep = sep
        self.nFile = nFile
        self.k = k

    @abstractmethod
    def iFile(self):
        """Variable to store the input file path/file name"""
        pass

    @abstractmethod
    def nFile(self):
        """Variable to store the neighbourhood file path/file name"""
        pass

    @abstractmethod
    def startTime(self):
        """Variable to store the start time of the mining process"""
        pass

    @abstractmethod
    def endTime(self):
        """Variable to store the end time of the complete program"""
        pass

    @abstractmethod
    def memoryUSS(self):
        """Variable to store USS memory consumed by the program"""
        pass

    @abstractmethod
    def memoryRSS(self):
        """Variable to store RSS memory consumed by the program"""
        pass

    @abstractmethod
    def finalPatterns(self):
        """Variable to store the complete set of patterns in a dictionary"""
        pass

    @abstractmethod
    def oFile(self):
        """Variable to store the name of the output file to store the complete set of frequent patterns"""
        pass

    @abstractmethod
    def startMine(self):
        """Code for the mining process will start from this function"""
        pass

    @abstractmethod
    def getPatterns(self):
        """Complete set of patterns generated will be retrieved from this function"""
        pass

    @abstractmethod
    def save(self, oFile):
        """Complete set of patterns will be saved in to an output file from this function
        :param oFile: Name of the output file
        :type oFile: file
        """
        pass

    @abstractmethod
    def getPatternsAsDataFrame(self):
        """Complete set of generated patterns will be loaded in to data frame from this function"""
        pass

    @abstractmethod
    def getMemoryUSS(self):
        """Total amount of USS memory consumed by the program will be retrieved from this function"""
        pass

    @abstractmethod
    def getMemoryRSS(self):
        """Total amount of RSS memory consumed by the program will be retrieved from this function"""
        pass


    @abstractmethod
    def getRuntime(self):
        """Total amount of runtime taken by the program will be retrieved from this function"""
        pass

    @abstractmethod
    def printResults(self):
        """ To print all the results of execution"""

        pass
