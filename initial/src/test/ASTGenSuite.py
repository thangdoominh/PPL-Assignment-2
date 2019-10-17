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

    def test_func_dec_320(self):
        input = """void main(){}
                float b[3];"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([])),
                               VarDecl("b", ArrayType(3, FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_func_decl_321(self):
        input = """void main(){}
                boolean[] func(int b, float x[]){}
                float b[3];"""
        expect = str(Program([FuncDecl(Id("main"), [], VoidType(), Block([])), FuncDecl(Id("func"),
                             [VarDecl("b", IntType()),
                             VarDecl("x", ArrayPointerType(FloatType()))],
                             ArrayPointerType(BoolType()),
                             Block([])),
                             VarDecl("b", ArrayType(3, FloatType()))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_func_nonblock_322(self):
        input = """
                void main(){}
                int a[1], b;
                string[] foo(){}
                """
        expect = str(Program([
            FuncDecl(Id("main"), [], VoidType(),Block([])),
            VarDecl("a", ArrayType(1,IntType())),
            VarDecl("b",IntType()),
            FuncDecl(Id("foo"),[],ArrayPointerType(StringType()),Block([]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_func_nonblock_323(self):
        input = """
                        string a[3], b[0];
                        float[] foo(int c, float d[], string f[]){}                
                        """
        expect = str(Program([VarDecl("a", ArrayType(3, StringType())),
                              VarDecl("b", ArrayType(0, StringType())),
                              FuncDecl(Id("foo"),
                                       [VarDecl("c", IntType()),
                                        VarDecl("d", ArrayPointerType(FloatType())),
                                        VarDecl("f", ArrayPointerType(StringType()))],
                                       ArrayPointerType(FloatType()),
                                       Block([])
                                      )]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_func_block_ifstm_324(self):
        input = """
                void main(int a, int b){
                    if (a = b)
                        {string c;}
                }
                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))

    def test_func_block_ifstm_325(self):
        input = """
                int sum(float a, float b){
                    if (a = b)
                        {}
                    else 
                        {string c;}
                }
                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_func_block_dowhile_326(self):
        input = """
                float haiz(string a[], boolean b){
                    do{}{}
                    while a = b;
                }
                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_func_block_for_327(self):
        input = """
                string[] abc(int a, float b[])
                {
                    for (a || b; a= b;a=b )
                    {
                    }
                } 
                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))

    def test_and_op_328(self):
        input = """
                string[] abc(int a, float b[])
                {
                    if (a && b)
                    {
                        float d;
                    }
                } 
                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_equal_op_329(self):
        input = """
                float[] xyz(int a, float b[])
                {
                    if (a == b)
                    {
                        float d;
                        string f;
                    }
                }
                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))