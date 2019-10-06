import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int a;"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType,Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_declaration_301(self):
        """Simple program: int main() {} """
        input = """string a, b;"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType,Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))