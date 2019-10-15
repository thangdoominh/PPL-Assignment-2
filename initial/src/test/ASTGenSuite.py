import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int a;"""
        expect = str(Program([VarDecl("a",IntType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_declaration_301(self):
        input = """string a, b;"""
        expect = str(Program([VarDecl("a",StringType()),VarDecl("b",StringType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_VarDec_302(self):
        input = """int x,a[3];"""
        expect = str(Program([VarDecl("x",IntType()),VarDecl("a",ArrayType(3,IntType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_VarDec_Float_303(self):
        input = """float a,b,c;"""
        expect = str(Program([VarDecl("a",FloatType()),
                              VarDecl("b",FloatType()),
                              VarDecl("c",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_VarDec_304(self):
        input = """float x, y[10], z"""
        expect = str(Program([VarDecl("x",FloatType()),
                              VarDecl("y",ArrayType(10,FloatType())),
                              VarDecl("z",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_VarDec_305(self):
        input = """int abc;
                   string xyz; 
                   float qwe;
                """
        expect = str(Program([VarDecl("abc",IntType()),
                              VarDecl("xyz",StringType()),
                              VarDecl("qwe",FloatType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    def test_vardec_306(self):
        input = """
                int a;
                float b;
                string c[1];
                boolean d;
                """
        expect = str(Program([VarDecl("a",IntType()),
                              VarDecl("b",FloatType()),
                              VarDecl("c",ArrayType(1,StringType())),
                              VarDecl("d",BoolType())]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_VarDec_307(self):
        input = """
                boolean _a_[3], b;
                string thang[10], thuan[12], Phong[9];
                """
        expect = str(Program([VarDecl("_a_",ArrayType(3,BoolType())),
                              VarDecl("b",BoolType()),
                              VarDecl("thang",ArrayType(10,StringType())),
                              VarDecl("thuan",ArrayType(12,StringType())),
                              VarDecl("Phong",ArrayType(9,StringType()))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_func_decl16(self):
        input = """void main(){}
                boolean[] func(int b, float x[]){}
                float b[3];"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([])),
                              FuncDecl(Id("func"),
                              [VarDecl("b", IntType()),VarDecl("x", ArrayPointerType(FloatType()))],
                              ArrayPointerType(BoolType()),
                              Block([])),
                              VarDecl("b", ArrayType(3, FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test__(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, ))

    def test__(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, ))

    def test__(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, ))

    def test__(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, ))

    def test__(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, ))

    def test__(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, ))