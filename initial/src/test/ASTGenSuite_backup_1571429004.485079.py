import unittest
from TestUtils import TestAST
from ExpectAST import *

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

    def test_308(self):
        input = """
                int abc;
                   string xyz; 
                   float qwe;
                """
        expect = str()
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_309(self):
        input = """
int abc;
                   string xyz; 
                   float qwe;
                """
        expect = str()
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_310(self):
        input = """
int abc;
                   string xyz; 
                   float qwe;
                """
        expect = str()
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_311(self):
        input = """
int a;

                """
        expect = str()
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_312(self):
        input = """
int a;

                """
        expect = str()
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_313(self):
        input = """
int a;

                """
        expect = str()
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_314(self):
        input = """
int a;
                """
        expect = str()
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_315(self):
        input = """
int a;

                """
        expect = str()
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_316(self):
        input = """
int a;

                """
        expect = str()
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_317(self):
        input = """
int a;

                """
        expect = str()
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_318(self):
        input = """
int a;

                """
        expect = str()
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_319(self):
        input = """
int a;

                """
        expect = str()
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

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
        expect = str(Program([
                                FuncDecl(
                                            Id("main"),
                                            [
                                                VarDecl("a",IntType()),
                                                VarDecl("b", IntType())
                                            ],
                                            VoidType(),
                                            Block([
                                                    If(
                                                        BinaryOp("=",Id("a"), Id("b")),
                                                        Block([VarDecl("c",StringType())]))])
                                        )
                            ])
                    )
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
        expect = str()
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_assign_op_326(self):
        input = """
                float haiz(string a[], boolean b){
                    do{}{}
                    while a = b;
                }
                """
        expect = str()
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_or_op_327(self):
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

    def test_not_equal_op_330(self):
        input = """
                float[] xyz(int a, float b[])
                {
                    if (a != b)
                    {
                        float d;
                        string f;
                    }
                }
                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))

    def test_less_op_331(self):
        input = """
                float[] xyz(int a, float b[])
                {
                    if (a < b)
                    {
                        float d;
                        string f;
                    }
                }
                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))

    def test_less_equal_op_332(self):
        input = """
                float[] xyz(int a, float b[])
                {
                    if (a <= b)
                    {
                        float d;
                        string f;
                    }
                }
                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))

    def test_greater_op_333(self):
        input = """
                float[] xyz(int a, float b[])
                {
                    if (a > b)
                    {
                        float d;
                        string f;
                    }
                }
                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_greater_equal_op_334(self):
        input = """
                float[] xyz(int a, float b[])
                {
                    if (a >= b)
                    {
                        float d;
                        string f;
                    }
                }
                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))

    #------------------------------------
    def test_funcdec_345(self):
        input = """ void foo(int x, int y, float z, string s, int a[]) {
                x = y+c+d;
            }
    		"""
        expect = str(Program([FuncDecl(Id("foo"),
                                       [VarDecl("x", IntType()), VarDecl("y", IntType()), VarDecl("z", FloatType()),
                                        VarDecl("s", StringType()), VarDecl("a", ArrayPointerType(IntType()))],
                                       VoidType(), Block(
                [BinaryOp("=", Id("x"), BinaryOp("+", BinaryOp("+", Id("y"), Id("c")), Id("d")))]))]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_(self):
        input = """
                    
                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))
    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))


    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_(self):
        input = """

                """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))