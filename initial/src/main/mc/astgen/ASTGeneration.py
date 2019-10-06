#
#   Student's Name    : Do Minh Thang
#   Student's ID      : 1713217
#

from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    def visitProgram(self,ctx:MCParser.ProgramContext):
        return Program(self.visit(x) for x in ctx.declaration())

    def visitDeclaration(self, ctx:MCParser.DeclarationContext):
        return self.visit(ctx.getChild(0))

    def visitVardeclaration(self, ctx:MCParser.VardeclarationContext):
        return VarDecl(self.visit(ctx.idlist()),self.visit(ctx.singletype()))

    def visitSingletype(self, ctx:MCParser.SingletypeContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return VoidType()
        elif ctx.BOOLTYPE():
            return BoolType()
        else:
            return StringType()

    def visitIdlist(self, ctx:MCParser.IdlistContext):
        return [self.visit(x) for x in ctx.idtail()]

    def visitIdtail(self, ctx:MCParser.IdtailContext):
        return self.visit(ctx.getChild(0))

    # def visitMctype(self,ctx:MCParser.MctypeContext):
    #     if ctx.INTTYPE():
    #         return IntType
    #     else:
    #         return VoidType
    #
    # def visitBody(self,ctx:MCParser.BodyContext):
    #     return self.visit(ctx.funcall())
    #
  	#
    # def visitFuncall(self,ctx:MCParser.FuncallContext):
    #     return CallExpr(Id(ctx.ID().getText()),[self.visit(ctx.exp())] if ctx.exp() else [])
    #
    # def visitExp(self,ctx:MCParser.ExpContext):
    #     if (ctx.funcall()):
    #         return self.visit(ctx.funcall())
    #     else:
    #         return IntLiteral(int(ctx.INTLIT().getText()))