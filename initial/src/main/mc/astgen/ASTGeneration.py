#
#   Student's Name    : Do Minh Thang
#   Student's ID      : 1713217
#

from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    def visitProgram(self,ctx:MCParser.ProgramContext):
        list_declaration = [self.visit(ctx.getChild(i)) for i in range(ctx.getChildCount()-1)]
        declarations = []
        for x in list_declaration:
            if isinstance(x, list):
                declarations += x
            else:
                declarations += [x]
        return Program(declarations)

    # ------------  Vardeclaration  ------------------
    def visitDeclaration(self, ctx:MCParser.DeclarationContext):
        return self.visit(ctx.getChild(0))

    def visitVardeclaration(self, ctx:MCParser.VardeclarationContext):
        listVardec = []
        typeVariable =  self.visit(ctx.singletype())
        list_id = self.visit(ctx.idlist())
        for x in list_id:
            if not isinstance(x, list):
                listVardec += [VarDecl(x, typeVariable)]

            else:
                listVardec += [VarDecl(x[0], ArrayType(x[1], typeVariable))]
        return listVardec

    def visitSingletype(self, ctx:MCParser.SingletypeContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.FLOATTYPE():
            return FloatType()
        elif ctx.BOOLTYPE():
            return BoolType()
        else:
            return StringType()

    def visitIdlist(self, ctx:MCParser.IdlistContext):
        return [self.visit(x) for x in ctx.idtail()]

    def visitIdtail(self, ctx:MCParser.IdtailContext):
        return self.visit(ctx.getChild(0))

    # # idarray: ID LSB INTLIT RSB;
    def visitIdarray(self, ctx:MCParser.IdarrayContext):
        return [ctx.ID().getText(), ctx.INTLIT().getText()]

    def visitIdsingle(self, ctx:MCParser.IdsingleContext):
        return ctx.ID().getText()

    # ------------  Funcdeclaration  ------------------
    def visitFuncdeclaration(self,ctx:MCParser.FuncdeclarationContext):
        if ctx.VOIDTYPE():
            typeFunc = VoidType()
        else:
            typeFunc = self.visit(ctx.getChild(0))

    # ---- Array Pointer Type  -----
    def visitArraypointertype(self,ctx:MCParser.ArraypointertypeContext):
        if ctx.